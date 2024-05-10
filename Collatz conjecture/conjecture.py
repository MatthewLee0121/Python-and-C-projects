# The conjecture states that we take a number F(N) F(N) has to be a real integer number between 0 and infinity 
#if F(N) % 2 == true then we perform n/2 if F(N) % 2 == 1 then we perform f(N)= 3N + 1 untill we either reach 1 the conjecture is to prove you will always hit 1

# Firstly i will use python to formulate a script thatll take a number i input and then do the conjecture and output each number in the list then at the end tell us how many steps we took to get there, function should also give us a maximum
# value, and the step this occured on

# This problem is hard, but we are not scared.

# I believe the question to be worded wrong, since if F(N) % 2 == 0 is true then we perform n/2, this means there is certain numbers we will hit that will immediately end the loop and plummet us to 1.
# these numbers are {1:1, 2:2, 3:4, 4:8, 5:16.......} in the form {steps to get to 1 : number that will plummet} you may notice the values in the key value pairs are 1, 2 ,4 ,8, 16, 32, 64, ......... or 2^x
# conjecture is not that we will always hit 1 but that we will always hit the line 2^x, as by default this will always take us to 1.
# This is what i aim to prove that as the number of attempts approaches infinity the chance that you will hit a 2^x number approaches 1 exactly.

######################################################## SCRIPT values ETC #################################################################################

import sqlite3
import json
import sys
import matplotlib.pyplot as plt

values = None

plt.ion()

#Main function
def main():
    global values
    what_do = input("""
          What do you want to do?
          1) run the main loop
          2) store the values to the database
          3) write the data to file
          4) This is 3 but for all values run with care
          5) convert a external file of dictionaries into a graph
          6)find the highest value of a given key(edit lines 138, 139)
          0) Exit the programme""")
    
    if what_do[0] == "1":
        values = get_values()
        what_do = " "
        return what_do
    if what_do[0] == "2":
        send_to_database(values)
        what_do = " "
        return what_do
    if what_do[0] == "3":
        write_to_new_file(values)
        what_do = " "
        return what_do
    if what_do[0] == "4":
        for x in range(0, sys.maxsize):
            values = get_values(x)
            write_to_new_file(values)
        what_do = " "
        return what_do
    if what_do[0] == "5":
        dictionarys = get_dictionarys()
        plot_multi_line_graph(dictionarys)
    if what_do[0] == "6":
        dictionarys = get_dictionarys6()
    if what_do[0] == "0":
        raise SystemExit

def get_values(num = None):
    step = 0

    if num == None: 
        start = inputValue()
    else:
        start = num
    storage = {}
    storage[step] = start
    
    while start >= 2:
        if start % 2 == 0 and power_of_two(start) == False:
            step += 1 # add one to step
            start = even(start)
            storage[step] = start
            if step >= 1001:
                return(storage)
            
        elif start % 2 == 1 and power_of_two(start) == False: #if odd number
            step += 1 #add 1 to step
            start = odd(start)
            storage[step] = start
            if step >= 1001:
                return(storage)
            
        elif power_of_two(start) == True: #if start is 1
            storage[step] = start
            print(storage)
            return(storage)

#Function for if num is even
def even(num):
    return int(num / 2) 

#Function for if num is odd
def odd(num):
    return (3 * num) + 1

#Function to get input value
def inputValue():
    num = int(input("Enter a whole number."))
    return num

#Fuction to check if power of two
def power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0 #checks if greater than 1 and only 1 set bit

def write_to_new_file(data):
    with open(r'C:\Users\mat_m\Coding_with_beans\Collatz conjecture\stored values', 'a') as file:
        file.write(str(data) + '\n')

def send_to_database(data):
    connection = sqlite3.connect('collatz.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS single_column_table (
                   id INTEGER PRIMARY KEY,
                   dictionary TEXT NOT NULL)''')
    cursor.execute("INSERT INTO single_column_table (dictionary) VALUES (?)",(json.dumps(data),))  # Convert data to string before insertion

    connection.commit()
    connection.close()

def get_dictionarys():
    dicts = []
    with open(r'C:\Users\mat_m\Coding_with_beans\Collatz conjecture\stored values', 'r') as file:
        for line_num, line in enumerate(file):
            if line_num in range(200000):
                try:
                    d = eval(line.strip())
                    dicts.append(d)
                except Exception as e:
                    print(f"Error parsing line {line_num + 1}: {line.strip()}")
                    print(f"Error message: {e}")
    return dicts

def get_dictionarys6():
    highest_values = {}  # Initialize dictionary to store the highest values for each key
    with open(r'C:\Users\mat_m\Coding_with_beans\Collatz conjecture\stored values', 'r') as file:
        for line_num, line in enumerate(file):
            if line_num in range(10000):
                try:
                    d = eval(line.strip())
                    for key, value in d.items():
                        if key in highest_values:
                            # Update the highest value for the key if the current value is higher
                            if value > highest_values[key]:
                                highest_values[key] = value
                        else:
                            highest_values[key] = value  # Add key-value pair if it doesn't exist yet
                except Exception as e:
                    print(f"Error parsing line {line_num + 1}: {line.strip()}")
                    print(f"Error message: {e}")
    print(highest_values)
    return highest_values

def plot_multi_line_graph(dicts):
    plt.figure(figsize=(12, 10))
    for d in dicts:
        y = list(d.values())
        x = list(d.keys())
        plt.plot(x, y, marker='x', label=None)

    
    
    plt.xlabel('Steps')
    plt.ylabel('value')
    plt.title('Collatz')
    plt.legend()
    plt.grid(True)
    plt.show



while True:
    main()