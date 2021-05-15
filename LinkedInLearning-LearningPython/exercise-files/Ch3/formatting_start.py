#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

    
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current year is: %Y"))
  print(now.strftime("%a, %d %B, %y")) # prints abbrev day name , day of month & full month name, then an abbrev 2digit yr

  # %c - locale's date and time, %x - locale's date, %X - locale's time (known as control codes)
  # also puts it into the standard local formatting (ie. Europe puts days before month, but in US month comes first)
  print(now.strftime("Locale date and time: %c"))
  print(now.strftime("Locale date: %x"))
  print(now.strftime("Locale time: %X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("24-hour time: %H:%M"))

if __name__ == "__main__":
  main()
