import sys
import time

from prettytable import PrettyTable

from model.CovidRecordDTO import process_as_date, CovidRecord
from view.Display import Display
from model.FileUtiles import FileUtils


class Main:

    def __init__(self):
        self.display = None
        self.filename = "../../data/covid19-download.csv"
        self.filename_write = "../../data/covid19-new.csv"
        self.covidRecord = []
        self.fileUtils = FileUtils()

    def start(self):
        self.display = Display()
        self.display.print_headline()
        self.display.print_menu()
        self.logic(self.get_user_input("Your input: "))

    @staticmethod
    def get_user_input(msg):
        u_input = input(msg)
        if u_input.isnumeric():
            return int(u_input)
        else:
            print("Input must be a numeric value.")
            return Main.get_user_input(msg)

    def logic(self, users_input=None):

        # Print All records
        if users_input == 1:
            self.print_all_records()
            self.start()

        # Load/Reload data from file
        elif users_input == 2:
            self.load_data_from_csv()
            self.start()

        # Create new CSV file
        elif users_input == 3:
            self.create_new_csv()
            self.start()

        #  Display selected records
        elif users_input == 4:
            self.display_selected_record()
            self.start()

        # Create a new record
        elif users_input == 5:
            self.create_new_record()
            self.start()

        # Edit record
        elif users_input == 6:
            self.edit_record()
            self.start()

        # Delete record
        elif users_input == 7:
            self.delete_record()
            self.start()

        # Information by province
        elif users_input == 8:
            self.information_by_province()
            self.start()

        # Information by date
        elif users_input == 9:
            self.information_by_date()
            self.start()

        elif users_input == 10:
            self.information_by_date_and_province()
            self.start()

        elif users_input == 11:
            self.information_by_number_of_deaths_by_region()
            self.start()

        # Exit
        else:
            print("Goodbye!")
            sys.exit()

    def print_all_records(self):
        ctr = 1
        t = PrettyTable(
            ["No.", "pruid", "prname", "prname_fr", "date", "numconf", "numprob", "numdeaths", "numtotal",
             "numtoday",
             "ratetotal"])

        for rec in self.covidRecord:
            t.add_row(
                [ctr, rec.pruid, rec.prname, rec.prname_fr, rec.date.strftime("%b %d %Y"), rec.numconf, rec.numprob,
                 rec.numdeaths, rec.numtotal, rec.numtoday, rec.ratetotal])
            ctr += 1

        print(t)

    def load_data_from_csv(self):
        try:
            self.covidRecord = self.fileUtils.get_content(self.filename)
            print("Records has been updated!\n")
        except IOError:
            print("Something went wrong while updating records\n")

    def create_new_csv(self):
        if len(self.covidRecord) < 1:
            print("No records found. Please load data.")
            time.sleep(3)
        else:
            x = self.get_user_input("Are you sure you want to create a new file? \n"
                                    "If yes enter 1: ")
            if x == 1:
                self.fileUtils.write_content(self.filename_write, self.covidRecord)
                print("File created successfully!\n")

            else:
                print("File creation aborted!\n")

    def display_selected_record(self):
        if len(self.covidRecord) < 1:
            print("No records found. Please load data.")
            time.sleep(3)

        else:
            row_number = self.get_user_input("Please enter row number: ")
            while row_number > len(self.covidRecord) and row_number > 0:
                row_number = self.get_user_input("Record does not exist. Please re-enter: ")

            selected = self.covidRecord[row_number - 1]
            t = PrettyTable(
                ["pruid", "prname", "prname_fr", "date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
                 "ratetotal"])
            t.add_row([selected.pruid, selected.prname, selected.prname_fr, selected.date.strftime("%b %d %Y"),
                       selected.numconf, selected.numprob,
                       selected.numdeaths, selected.numtotal, selected.numtoday, selected.ratetotal])

            print(t)

    def create_new_record(self):
        print("Please enter the following information to create new record.")
        pruid = self.get_user_input("pruid: ")
        prname = input("prname: ")
        prname_fr = input("prname_fr: ")
        date = input("date(mm/dd/yyyy): ")
        numconf = self.get_user_input("numconf: ")
        numprob = self.get_user_input("numprob: ")
        numdeaths = self.get_user_input("numdeaths: ")
        numtotal = self.get_user_input("numtotal: ")
        numtoday = self.get_user_input("numtoday: ")
        ratetotal = input("ratetotal: ")

        new_record = CovidRecord(
            pruid,
            prname,
            prname_fr,
            process_as_date(date),
            numconf,
            numprob,
            numdeaths,
            numtotal,
            numtoday,
            ratetotal
        )

        self.covidRecord.append(new_record)
        print("Record created successfully")

    def edit_record(self):
        x = self.get_user_input("Please enter a row number you want to edit: ") - 1
        t = PrettyTable(
            ["pruid", "prname", "prname_fr", "date", "numconf", "numprob", "numdeaths", "numtotal",
             "numtoday",
             "ratetotal"])
        t.add_row(
            [self.covidRecord[x].pruid, self.covidRecord[x].prname, self.covidRecord[x].prname_fr,
             self.covidRecord[x].date.strftime("%b %d %Y"), self.covidRecord[x].numconf,
             self.covidRecord[x].numprob,
             self.covidRecord[x].numdeaths, self.covidRecord[x].numtotal, self.covidRecord[x].numtoday,
             self.covidRecord[x].ratetotal])

        print(t)

        pruid = self.get_user_input("pruid: ")
        prname = input("prname: ")
        prname_fr = input("prname_fr: ")
        date = input("date: ")
        numconf = self.get_user_input("numconf: ")
        numprob = self.get_user_input("numprob: ")
        numdeaths = self.get_user_input("numdeaths: ")
        numtotal = self.get_user_input("numtotal: ")
        numtoday = self.get_user_input("numtoday: ")
        ratetotal = input("ratetotal: ")

        new_record = CovidRecord(
            pruid,
            prname,
            prname_fr,
            process_as_date(date),
            numconf,
            numprob,
            numdeaths,
            numtotal,
            numtoday,
            ratetotal
        )

        self.covidRecord[x] = new_record

    def delete_record(self):
        x = self.get_user_input("Please enter a row number you want to delete: ")
        y = self.get_user_input("Are you sure you want to delete this record?\n Enter 1 for YES: ")
        if x <= len(self.covidRecord) and y == 1:
            self.covidRecord.pop(x - 1)

    def information_by_province(self):
        province = input("\nPlease enter province name or \"Canada\" for the whole country: ")
        t = PrettyTable(
            ["date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday", "ratetotal"])

        for rec in self.covidRecord:
            if rec.prname.lower() == province.lower():
                t.add_row(
                    [rec.date.strftime("%b %d %Y"), rec.numconf, rec.numprob, rec.numdeaths, rec.numtotal,
                     rec.numtoday, rec.ratetotal])

        print(t)

    def information_by_date(self):
        date = process_as_date(input("\nPlease enter a date (Jan 1, 2020 to Jan 9, 2021)(mm/dd/yyyy): "), False)
        t = PrettyTable(
            ["pruid", "prname", "prname_fr", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
             "ratetotal"])

        for rec in self.covidRecord:
            if rec.date == date:
                t.add_row(
                    [rec.pruid, rec.prname, rec.prname_fr, rec.numconf, rec.numprob, rec.numdeaths, rec.numtotal,
                     rec.numtoday, rec.ratetotal])
        print(t)

    def information_by_date_and_province(self):
        province = input("\nPlease enter province name or \"Canada\" for the whole country: ")
        date = process_as_date(input("\nPlease enter a date (Jan 2020 to Jan 2021)(mm/yyyy): "), True)
        t = PrettyTable(
            ["date", "pruid", "prname", "prname_fr", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
             "ratetotal"])

        for rec in self.covidRecord:
            if rec.date.month == date.month and rec.prname.lower() == province.lower():
                t.add_row(
                    [rec.date.strftime("%b %d %Y"), rec.pruid, rec.prname, rec.prname_fr, rec.numconf, rec.numprob,
                     rec.numdeaths, rec.numtotal, rec.numtoday, rec.ratetotal])
        print(t)

    # this method will return record with a maximum number of deaths by selected province
    def information_by_number_of_deaths_by_region(self):
        province = input("\nPlease enter province name or \"Canada\" for the whole country: ")
        t = PrettyTable(
            ["date", "pruid", "prname", "prname_fr", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
             "ratetotal"])

        num_of_death = 0

        result = []

        for rec in self.covidRecord:
            if rec.prname.lower() == province.lower():
                if int(rec.numdeaths) > num_of_death:
                    self.num_of_death = rec.numdeaths
                    result.clear()
                    result.append(rec)

        t.add_row(
            [result[0].date.strftime("%b %d %Y"), result[0].pruid, result[0].prname, result[0].prname_fr,
             result[0].numconf,
             result[0].numprob,
             result[0].numdeaths, result[0].numtotal, result[0].numtoday, result[0].ratetotal])
        print(t)
