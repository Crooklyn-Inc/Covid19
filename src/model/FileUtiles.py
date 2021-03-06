import csv
import sys
from threading import Thread

from model.CovidRecordDTO import CovidRecord, process_as_date


# file reader class to read from csv document
class FileUtils:
    covidRecord = []

    def _open_file(self, filename):

        ctr = 0
        try:
            with open(filename, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    record = CovidRecord(
                        line.get("pruid"),
                        line.get("prname"),
                        line.get("prnameFR"),
                        process_as_date(line.get("date"), False),
                        line.get("numconf"),
                        line.get("numprob"),
                        line.get("numdeaths"),
                        line.get("numtotal"),
                        line.get("numtoday"),
                        line.get("ratetotal")
                    )
                    self.covidRecord.append(record)
                    # simple counter to read 'n' number of records
                    # ctr += 1
                    # if ctr >= 10:
                    #     break

            return self.covidRecord
        except IOError:
            print("File is unavailable or missing ")
            sys.exit()

    def _write_file(self, filename, covid_record):
        with open(filename, 'w+', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["pruid", "prname", "prname_fr", "date", "numconf", "numprob", "numdeaths", "numtotal",
                             "numtoday", "ratetotal"])
            for record in covid_record:
                writer.writerow(
                    [record.pruid, record.prname, record.prname_fr, record.date.strftime("%b %d %Y"),
                     record.numconf, record.numprob,
                     record.numdeaths, record.numtotal, record.numtoday, record.ratetotal])

    def get_content(self, filename=None):
        thread = Thread(target=self._open_file, args=("Covid19/data/" + filename,))
        thread.name = "Thread to read"
        thread.start()
        thread.join()
        return self.covidRecord

    def write_content(self, filename=None, covid_record=None):
        thread = Thread(target=self._write_file, args=("Covid19/data/" + filename, covid_record,))
        thread.name = "Thread to write"
        thread.start()
        thread.join()
