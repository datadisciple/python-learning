#
# Example file for working with conditional statements
#


def main():
    x, y = 115, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    elif (x == y):  # note: there is currently no switch/case statement functionality in python and you must use elif
        st = "x is the same as y"
    else:
        st = "x is greater than y"
   
    print (st) 
   
    # conditional statements let you use "a if C else b"
    # this is just a more concise option available for writing an if/else statement
    st = "x is less than y" if (x<y) else "x is greater than or the same as y"
    print (st)

   
