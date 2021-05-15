#
# Example file for working with date information
#

#from datetime standard module import these classes
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is ", today)

  # print out the date's individual components
  print("Date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is: ", today.weekday())
  
  # user weekday number to index into an array and print the abbrev. day
  days = ["mon","tue","wed","thu","fri","sat","sun"]
  print ("Which is a: ", days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is: ", today)
  
  # Get the current time
  t = datetime.time(datetime.now()) # takes a now object from the datetime class and passes into the time function to give back the current time
  print(t)

  
if __name__ == "__main__":
  main();
  