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

#Main function
def main():
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
    step = 0 #set the step counter to 0
    start = int(inputValue()) #sets a value = to the return of inputValue as uses it as a start point
    while start >= 2: #while start is greater than 2 so we dont have to call it over and over
        if start % 2 == 0: #if statement for now will probably have to make it into a while statement eventually
            step += 1 # add one to step
            start = print(even(start), step) #if even number then / 2 and prints it and the step value
        elif start % 2 == 1: #if odd number
            step += 1 #add 1 to step
            start = print(odd(start), step) # then perform 3n + 1 and prints it and the step value
        elif start == 1: #if start is 1
            print("End", "1", step) #we are at the end and the step value
        else: #if not a even or odd number
            print("Error") #prints an error
    

#Function for if num is even
def even(num):
    """
        Brief overview \n
         Function takes our input number and will divide it by two fufilling the F(N) %  2 == 0: n /2 \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
         num -- input number for whereever we are in the sequence \n
        -----------------------------------------------------------------------------\n
        Variables: \n
         num -- see Keyword arguments \n
        -----------------------------------------------------------------------------\n
        Overview: \n
         Function takes our input number, then returns the value / 2 returns values as int\n
    """
    return num / 2 #returns a float will have to change

#Function for if num is odd
def odd(num):
    """
        Brief overview \n
         Function takes our input number and will divide it by two fufilling the F(N) %  2 == 1: 3n + 1 \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
         num -- input number for whereever we are in the sequence \n
        -----------------------------------------------------------------------------\n
        Variables: \n
         num -- see Keyword arguments \n
        -----------------------------------------------------------------------------\n
        Overview: \n
         Function takes our input number, then returns the value * 3 then + 1 returns value as a float \n
    """
    return (3 * num) + 1

#Function to get input value
def inputValue():
    """
        Brief overview \n
         Function takes our input number and will divide it by two fufilling the F(N) %  2 == 1: n /2 \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
         num -- input number for whereever we are in the sequence \n
        -----------------------------------------------------------------------------\n
        Variables: \n
         num -- see Keyword arguments \n
        -----------------------------------------------------------------------------\n
        Overview: \n
         Function takes our input number, then returns the value / 2 \n
    """
    num = input("Enter a whole number.")
    return num



main()