#
# Overview on using lists, tuples, and sets in Python
# https://youtu.be/W8KRzm-HUcc
#

# Lists & Tuples → sequential data
# Sets → unordered collections of values w/ no duplicates

#---------------------------------------------------------------------------------------------------------#

### Lists (these have the most functionality)
print('[LISTS]\n')

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses)) # length of list
print(courses[3]) # gets CompSci (the last item in list)
print(courses[-1]) # negative indexes start at the end of the list and go backwards
print(courses[0:2]) # return list over a specific index range (slicing)
print('\n')


# List Methods

# append() - adds to end of list
courses.append('Art')
print(courses)

# insert() - inserts into specific index of list
courses.insert(0, 'Calculus')   # first input is the index to insert at
print(courses)

# extend() - adds lists together
courses_2 = ['Biology', 'Environmental Science']
courses.insert(0, courses_2)
print(courses)  # inserts courses_2 list within courses list / creates a multi-level list (not what we want here)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)   # adds values from courses_2 list into courses list (everything is on same level)
print(courses)
print('\n')

# remove() - removes items from list
courses.remove('Math')
print(courses)

# pop() - removes last value from list
# useful in using list as a stack or queue
# pop returns the value it removed
popped = courses.pop()
print("Course removed: " + popped)
print(courses)

# revere() - reverses list
courses.reverse()
print(courses)

# sort() - sorts list (alphabetical order for strings, ascending order for numbers)
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

nums2 = [5, 3, 6, 4, 9]
nums2.sort(reverse=True)    # sorts list in reverse order
print(nums2)
print('\n')

# sorted() - returns a sorted version of list w/o altering original list
coursesV2 = ['History', 'Math', 'Physics', 'CompSci']
sorted_coursesV2 = sorted(coursesV2)
print(coursesV2)    # original list is unaffected
print(sorted_coursesV2) # new sorted list output
print('\n')

# min() & max() - minimum or maximum value in a list
nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))

# sum() - sums list
print(sum(nums))
print('\n')

# find index of a certain value in list
print(coursesV2.index('Math'))

# check if a value is in list → returns a true/false result
# this is useful for conditionals in if/else statements
print('Math' in coursesV2)
print('Art' in coursesV2)
print('\n')

# use a for loop to individually check each item of list
for course in coursesV2:
    print(course)

# use enumerate() function to also return the index of the course
for index, course in enumerate(coursesV2):
    print(index, course)
print('\n')

# can also pass in a start value to enumerate function
for index, course in enumerate(coursesV2, start=1):
    print(index, course)
print('\n')

# join() - joins list values into one long string seperated by user declared value - in this case → ', '
course_str = ', '.join(coursesV2)
print(course_str)

# split() - reverse of join() - splits string into a list based off a delimiter value
new_list = course_str.split(', ')
print(new_list)
print('-----------------------------------------------------------------\n')

#---------------------------------------------------------------------------------------------------------#

### Tuples - very similar to lists EXCEPT they cannot be modified aka they are "Immutable"
# Tuples use () instead of []
print('[TUPLES]\n')

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print("These are lists for reference:")
print(list_1)
print(list_2)

# changing the value of index0 of list_1 ALSO changes the value of index0 of list_2 bc they are the same mutable object
list_1[0] = 'Art'   

print(list_1)
print(list_2)
print('\n')


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print("These are tuples:")  # trying to modify a tuple will cause an error since they are immutable
print(tuple_1)
print(tuple_2)
print('-----------------------------------------------------------------\n')

#---------------------------------------------------------------------------------------------------------#

### SETS - unordered collections of values w/ no duplicates
# sets use {} instead of [] or ()
print('[SETS]\n')

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)   # notice that the order of printout likely doesn't match order entered

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} # add second instance of 'Math' to set
print(cs_courses) # notice that 'Math' still only appears once as sets don't store duplicates
print('\n')

# Sets are good for determining what values they share or don't share w/ other sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# interesection() - determines values sets have in common → History & Math
print(cs_courses.intersection(art_courses))

# difference() - returns courses in first set that aren't in second set → Physics & CompSci
print(cs_courses.difference(art_courses))

# union() - combines both sets to show all courses offered
print(cs_courses.union(art_courses))
print('-----------------------------------------------------------------\n')

#---------------------------------------------------------------------------------------------------------#

# note the small gotcha for creating empty sets

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

