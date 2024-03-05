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

start = inputValue() #sets a value = to the return of inputValue as uses it as a start point
if start % 2 == 0: #if statement for now will probably have to make it into a while statement eventually
    start = even(start) #if even number then / 2
elif start % 2 == 1: #if odd number
    start = odd(start) # then perform 3n + 1
else: #if not a even or odd number
    return("Error") #prints an error