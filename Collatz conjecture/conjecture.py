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

#Main function
def main():
    what_do = input("""
          What do you want to do?
          1) run the main loop
          2) store the values to the database
          0) Exit the programme""")
    
    if what_do[0] == "1":
        values = get_values()
        what_do = " "
        return what_do
    if what_do[0] == "2":
        send_to_database(values)
        what_do = " "
        return what_do
    if what_do[0] == "0":
        raise SystemExit

def get_values():
    """
        Brief overview \n
         Script will ask for a input value then iterate through collatz conjecture and print the resulting value and the step value  \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
         \n
        -----------------------------------------------------------------------------\n
        Variables: \n
         start -- First number \n
        -----------------------------------------------------------------------------\n
        Overview: \n
         First  declares step then gets the original input value as a string then coverts it to a int and stores this as start, \n
         Next enters a while loop to interate through the conjecture and print the value and the step of each step
    """
    step = 0 
    start = inputValue()
    storage = {}
    storage[step] = start
    
    while start >= 2:
        if start % 2 == 0 and power_of_two(start) == False:
            step += 1 # add one to step
            start = even(start)
            storage[step] = start
            
        elif start % 2 == 1 and power_of_two(start) == False: #if odd number
            step += 1 #add 1 to step
            start = odd(start)
            storage[step] = start
            
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

def send_to_database(data):
    connection = sqlite3.connect('collatz.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS single_column_table (
                   id INTEGER PRIMARY KEY,
                   dictionary TEXT NOT NULL)''')
    cursor.execute("INSERT INTO single_column_table (dictionary) VALUES (?)", (str(data),))  # Convert data to string before insertion

    connection.commit()
    connection.close()


while True:
    main()