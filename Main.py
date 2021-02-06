import sys

from prettytable import PrettyTable

from CovidRecord import process_as_date, CovidRecord
from Display import Display
from FileUtiles import FileUtils


class Main:
    def __init__(self):
        self.display = None
        self.filename = "covid19-download.csv"
        self.filename_write = "covid19-new.csv"
        self.covidRecord = []

    def start(self):
        self.display = Display()
        self.display.print_headline()
        self.display.print_menu()
        self.logic(self.get_user_input("Your input: "))

    @staticmethod
    def get_user_input(x):
        return int(input(x))

    def logic(self, users_input=None):
        file_utils = FileUtils()

        # Print All records
        if users_input == 1:
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
            self.display.print_menu()
            self.logic(self.get_user_input("Your input: "))

        # Load/Reload data from file
        elif users_input == 2:

            try:
                self.covidRecord = file_utils.get_content(self.filename)
                print("Records has been updated!\n")
            except IOError:
                print("Something went wrong while updating records\n")

            self.display.print_menu()
            self.logic(self.get_user_input("Your input: "))

        # Create new CSV file
        elif users_input == 3:
            x = self.get_user_input("Are you sure you want to create a new file? \n"
                                    "If yes enter 1: ")
            if x == 1:
                file_utils.write_content(self.filename_write, self.covidRecord)
                print("File created successfully!\n")

            else:
                print("File creation aborted!\n")

            self.display.print_menu()
            self.logic(self.get_user_input("Your input: "))

        #  Display selected records
        elif users_input == 4:

            row_number = self.get_user_input("Please enter row number: ")

            while row_number > len(self.covidRecord):
                row_number = self.get_user_input("Record does not exist. Please re-enter: ")

            selected = self.covidRecord[row_number - 1]
            t = PrettyTable(
                ["pruid", "prname", "prname_fr", "date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
                 "ratetotal"])
            t.add_row([selected.pruid, selected.prname, selected.prname_fr, selected.date.strftime("%b %d %Y"),
                       selected.numconf, selected.numprob,
                       selected.numdeaths, selected.numtotal, selected.numtoday, selected.ratetotal])

            print(t)
            self.display.print_menu()
            self.logic(self.get_user_input("Your input: "))

        # Create a new record
        elif users_input == 5:
            print("Please enter the following information to create new record.")
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

            self.covidRecord.append(new_record)

            print("Record created successfully")
            self.display.print_menu()
            self.logic(self.get_user_input("Your input:"))

        # Edit record
        elif users_input == 6:
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

            self.display.print_menu()
            self.logic(self.get_user_input("Your input: "))

        # Delete record
        elif users_input == 7:
            x = self.get_user_input("Please enter a row number you want to delete: ")
            y = self.get_user_input("Are you sure you want to delete this record?\n Enter 1 for YES: ")
            if x <= len(self.covidRecord) and y == 1:
                self.covidRecord.pop(x - 1)

            self.display.print_menu()
            self.logic(self.get_user_input("Your input:"))

        # Information by province
        elif users_input == 8:
            province = input("\nPlease enter province name or \"Canada\" for the whole country: ")
            t = PrettyTable(
                ["date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday", "ratetotal"])

            for rec in self.covidRecord:
                if rec.prname.lower() == province.lower():
                    t.add_row(
                        [rec.date.strftime("%b %d %Y"), rec.numconf, rec.numprob, rec.numdeaths, rec.numtotal,
                         rec.numtoday, rec.ratetotal])
                    print(t)
            self.display.print_menu()
            self.logic(self.get_user_input("Your input:"))

        # Information by date
        elif users_input == 9:

            date = process_as_date(input("\nPlease enter a date (Jan 1, 2020 to Jan 9, 2021)(mm/dd/yyyy): "))
            t = PrettyTable(
                ["pruid", "prname", "prname_fr", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
                 "ratetotal"])

            for rec in self.covidRecord:
                if rec.date == date:
                    t.add_row(
                        [rec.pruid, rec.prname, rec.prname_fr, rec.numconf, rec.numprob, rec.numdeaths, rec.numtotal,
                         rec.numtoday, rec.ratetotal])
                    print(t)
                    self.display.print_menu()
                    self.logic(self.get_user_input("Your input:"))

        # Exit
        else:
            print("Goodbye!")
            sys.exit()
