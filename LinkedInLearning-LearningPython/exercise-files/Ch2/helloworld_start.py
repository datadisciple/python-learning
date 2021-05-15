#
# Example file for HelloWorld
#

# def is how you define a function in python
# the indentations under the function are important - python uses whitespace to figure out which lines of codes belong in scope blocks (functions, if statements, etc.)
def main():
  print("Hello World")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

#if python function is main() then run main
#this is mostly useful if you want to execute the function by calling the filename it is stored in from the terminal
#without this, the main function wouldn't output anything to the terminal unless there is a seperate line that calls the funciton and tells it to run

if __name__ == "__main__":
  main()