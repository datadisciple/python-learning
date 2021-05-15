#
# Example file for working with classes
#

class myClass():
    # first argument to any methods of a class is usually 'self'
    # similar to 'this' in javascript / refers to the object itself
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass): # creates 'anotherClass' that is based on 'myClass'
    def method1(self):
        # calls the inherited method on the super class
        myClass.method1(self) #need to pass the 'self' around because it is inside the class now
        print("anotherClass method1")

    def method2(self, someString): #overrides existing method2 in the base class and does it's own thing
        print("anotherClass method2 ")

def main():
    c = myClass() # instantiates an object instance of myClass
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()
