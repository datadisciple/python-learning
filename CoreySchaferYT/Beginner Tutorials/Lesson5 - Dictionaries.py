#
# Overview on dictionaries and working with key value pairs
# https://youtu.be/daefaLgNkw0
#

#Key value pairs - two linked values where key is a unique value used to find data. The value is that data.

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# get value of a specific key
print(student['name'])

# if you try to access a key that doesn't exist, you will get a key error
# a better way to handle this is to use the get() method
# if no key is found it will just return 'None' instead of an error
print(student.get('name'))
print(student.get('phone')) # key doesn't exist so returns 'None'
print(student.get('phone', 'Not Found'))    # can also specify your own default value for keys that don't exist in the get() method

student['phone'] = '555-5555'   # assigns a new phone key to student
print(student)

# update a key value
student['name'] = 'Jane'
print(student)

# can also update values using the update() method
# this is useful when updating multiple values at once
student.update({'name': 'Mark', 'age': 26, 'phone': '234-6732'})
print(student)

# delete a specific key and its value using 'del' keyword
del student['age']
print(student)

# pop() also allows you to remove a key and return the deleted value
student['age'] = 26 # just adding age back in here since it was deleted
age = student.pop('age')    # popping off age
print(student)
print(age)
print('\n')

# loop through all the keys and values of dict
print(len(student)) # tells how many keys are in dictionary
print(student.keys())   # lists all keys of dictionary
print(student.values()) # lists all values
print(student.items())  # lists key value pairs (key, value)
print('\n')

# needs to use items method in order to loop through both keys AND values
for key, value in student.items():
    print(key,value)
