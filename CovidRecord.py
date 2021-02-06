import datetime


# Data Transfer Object
class CovidRecord:
    def __init__(self, pruid, prname, prname_fr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        self.pruid = pruid
        self.prname = prname
        self.prname_fr = prname_fr
        self.date = date
        self.numconf = numconf
        self.numprob = numprob
        self.numdeaths = numdeaths
        self.numtotal = numtotal
        self.numtoday = numtoday
        self.ratetotal = ratetotal


# function to covert string to datetime object
def process_as_date(date_string):
    x = [int(numeric_string) for numeric_string in date_string.split("/")]
    return datetime.datetime(x[2], x[0], x[1])
