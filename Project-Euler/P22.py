# open .txt file w/ the names and read it into a list
names_file = open("P22_names.txt", "r")
names = names_file.read()
names_list = names.split(",")
names_file.close()

# sort list into alphabetical order
names_list.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# initialize total score which will be used to add up all names scores in the list
tot_score = 0

# Remove extra "" around name text
for i, name in enumerate(names_list):
    firstname = name.replace('"', '')
    names_list[i] = firstname
    score = 0
    # print(firstname)
    # if i==3: break

    # find the value of each char in the name and add together
    for char in firstname:
        letter_value = alphabet.index(char) + 1 # index starts at 0 but need it to start at 1 for scoring

        # letter_value can also be found using the ord() function which returns the unicode value of an argument
        # letter_value = (ord(char) - ord('A') + 1)

        score += letter_value

    # multiplier is is the index of the name's position in the list+1
    multiplier = i+1
    name_score = score*multiplier

    # add name_score to the running total score
    tot_score += name_score

print(tot_score)
    




