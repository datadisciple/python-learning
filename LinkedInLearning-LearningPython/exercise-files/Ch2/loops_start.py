#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
    print (x)
    x = x+1

  # define a for loop
  for x in range(5,10): #sequence of numbers starting at 5 and stopping BEFORE 10
    print(x)
  

  # use a for loop over a collection
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

  for d in days:
    print(d)
  
  # use the break and continue statements
  for x in range(5,10):
    if (x % 2 == 0): continue #if this is true then go to the next number of the loop and don't do any statements below it. this is a modulo aka remainder calc
    if (x == 9): break
    print(x)

  #using the enumerate() function to get index
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):
    print(i, d)
  

if __name__ == "__main__":
  main()
  
