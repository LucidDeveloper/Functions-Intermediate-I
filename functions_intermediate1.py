'''
# @ author: 
# Gianni M. Javier

# Assignment: Functions Intermediate I

# Objectives:

# Practice writing functions and looping over dictionaries
# Achieve a better understanding of how to traverse through a list of dictionaries or through a dictionary of lists
# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.

'''

#Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print() #Prints a new line

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# print(x) #Prints the list of lists contained in the variable x
# print() #Prints a new line
x[1][0] = 15 #Changes the value of the integer 10 in the first position of the second list, to the integer 15, which is contained in the variable x which contains a list of lists
print(x) #Prints the list of lists contained in the variable x with the modification of the changed value 
print() #Prints a new line

#Change the last_name of the first student from 'Jordan' to 'Bryant'

# print(students) #Prints the list of dictionaries contained in the variable students
# print() #Prints a new line
students[0]['last_name'] = 'Bryant' #Changes the value of the keyvalue 'Jordan', which is associated with the keyname 'last_name', from 'Jordan' to 'Bryant, which is contained in the first dictionary of the list of dictionaries, which is contained in the variable named students
print(students) #Prints the list of dictionaries contained in the variable students with the modification of the changed value
print() #Prints a new line

#In the sports_directory, change 'Messi' to 'Andres'

# print(sports_directory) #Prints the dictionary contained in the variable sports_directory, which contains a list of keyvalues associated with each keyname
# print() #Prints new line
sports_directory['soccer'][0] = 'Andres' #Changes the value of the string 'Messi' in the first position of the list of values associated with the keyname 'soccer', the second dictionary within the list of dictionaries contained in the variable sports_directory, from the String 'Messi' to the String 'Andres'
print(sports_directory) #Prints the dictionary contained in the variable sports_directory with the modification of the changed value
print() #Prints new line

#Change the value 20 in z to 30

# print(z) #Prints the list of dictionaries contained in the variable z
# print() #Prints new line
z[0]['y'] = 30 #Changes the value of the integer 20, which is the key value associated with the keyname 'y', which is contained in the first dictionary in the first position of the list contained in the variable z, from the integer 20 to the integer 30
print(z) #Prints the list of dictionaries contained in the variable z with the modification of the changed value
print() #Prints new line

# Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list): #Function, which when given a list of dictionaries, loops through each dictionary in the list and prints out each key paired with its associated value
    for index in range(len(some_list)): #Runs the loop from 0 to the length of the list minus one and stores each value into the variable name index
        # print(index) #Prints the value of the variable named index for each iteration
        # print(some_list[index]) #Prints the dictionary in the list at given index for each iteration
        keyList = [] #Initiates empty list to store keys for each iteration of loop
        valList = [] #Initiates empty list to store values for each iteration of loop
        pairList = [] #Initiates empty list to store key value pairs for each iteration of loop
        for key in some_list[index]: #Runs loop through each position of list, for given index, and stores the value in the variable named key
            # print(key) #Prints the Value of the variable named key
            keyList.append(key) #Appends the value of the variable named key into the list named keyList
            val = some_list[index][key] #Stores the value of the associated key in the variable named val
            # print(val) #Prints the value in the variable val
            valList.append(val) #Appends the value of the variable val to the list named valList
            pair = key + ' - ' + val #Stores the variable key and the variable val as a key value pair in the variable pair
            # print(pair) #Prints the value of the variable pair
            pairList.append(pair) #Appends the value of the variable pair to the list named pairList
        print(*pairList, sep = ', ') #For each iteration of the loop Prints all items in the list named pairList, using * operator, as seperates values, without the use of a loop, seperated by the chosen character, sep = ', ', which would be seperated by space, ' ', by default

iterateDictionary(students) #Calls the function iterateDictionary with the argument of students as the list of dictionaries
print() #Prints a new line

# Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

# For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name,some_list): #Function, which when give a list of dictionaries and a key name, prints out the value associated with the key name for each dictionary within the list 
    for index in range(len(some_list)):
        print(some_list[index][key_name])

iterateDictionary2('first_name',students) #Calls function iterateDictionary2 with argument 'first_name' for the key name and argument students for the list of dictionaries
print() #Prints new line

iterateDictionary2('last_name',students) #Calls function iterateDictionary2 with argument 'last_name' for the key name and argument students for the list of dictionaries
print() #Prints new line

# Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
 
# For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo(some_dict): #Function, which given a dictionary whose values are all lists, will print the name of each key along with the size of its list, and then prints the associated values of the key which are stored in each key's list
    for key in some_dict: #Runs a loop through the dictionary of lists named some_dict and stores the key name in the variable key for each iteration
        list = [] #Creates an empty list named list
        for index in range(len(some_dict[key])): #Runs a loop, from 0 to the length minus one, of the list associated with the key name stored in the variable key, from the dictionary of lists, and stores it in the variable index for every iteration
            val = some_dict[key][index] #Stores the value at the given index of the list associated with the given key, from the dictionary of lists, into the variable val
            list.append(val) #Appends the value of the variable val to the list named list
        print(len(list), key) #Prints the length of the list as well as the value store in the variable key, which in this case if the dictionary key of the respective list associated with the key
        print(*list, sep = '\n') #Prints he associated list within the dictionary as individual items, using * operator, rather than using a loop to print each item in the list, seperated by the chosen character, in this case a new line, sep ='\n', by default it would be seperated by a space, sep=' '
        print() #Prints new line

printInfo(dojo)