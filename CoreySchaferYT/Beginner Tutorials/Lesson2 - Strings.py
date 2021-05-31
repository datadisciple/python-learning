#
# Overview on using strings and textual data in Python
# https://youtu.be/k9TUPpGqYTo
#

message = 'Hello World'
print(message)

# can use either single quotes or double quotes for strings
# what quote format is best to use is dependent upon the string
message2 = "Bobby's World"
print(message2)

# create a multi-line string by useing 3 quotes
message3 = """Bobby's world was a
good cartoon in the 1990's"""
print(message3)
print ("\n") #adding new line to for topic switch

#count length of string
print(len(message))

# access specific character of a string by using that character's index
# first character is index 0 
print(message[0])

#last character is at index 10 (total length -1)
print(message[10])

#access a range of characters
print(message[0:5]) #provides an index range. 0 is inclusive, but 5 is not.
print(message[:5]) #if no start index is provided, python will automatically index from 0
print(message[6:]) #similarly, if no end index is provided, python will index to end
print("\n")


### String Methods ###

print(message.lower())  # all lowercase
print(message.upper())  # all uppercase

print(message.count('Hello'))   # returns # of times 'Hello' appears in message
print(message.count('l'))   # returns # of times 'l' appears in message
print(message.count('L'))   # returns 0 since Python is a case sensitive language

print(message.find('Hello'))    # returns start index where first instance of phrase occurs
print(message.find('nowhere'))  # returns -1 if it cannot find phrase in string
print ("\n")

#Replace characters in string with other characters → replace method
message = message.replace('World', 'Universe')  # (what to replace, what to replace with)
print(message)

# Adding aka Concatenating Strings
greeting = 'Hello'
name = 'Michael'

# Different ways to cocantenate strings (all 3 the same cocatenated string)
message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name) # formatted string
message = f'{greeting}, {name}. Welcome!'   # formatted via f-string (available in Python 3.6+)
print(message)

# benefit of f-strings is that you can right code w/in the placeholder
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
print('\n')

# shows all attributes & methods that you have access to for a given variable
print(dir(name))

# use help function to get more info on what function or method actually does
print(help(str.lower))