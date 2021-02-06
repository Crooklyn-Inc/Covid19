class Display:
    def __init__(self):
        self.author = "YEHOR SHRAMCHENKO"

    def print_headline(self):
        print("COVID DATASET")
        print("Program prepared by: ", self.author)

    @staticmethod
    def print_menu():
        print("Please select:")
        print("1.Print all records ")
        print("2.Load/Reload data from file ")
        print("3.Create new CSV from in memory data")
        print("4.Display selected records ")
        print("5.Create a new record ")
        print("6.Edit record")
        print("7.Delete record ")
        print("8.Information by province")
        print("9.Information by date")
        print("0.Exit")
