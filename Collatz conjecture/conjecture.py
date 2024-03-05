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


def even(num):
    return num / 2

def odd(num):
    return (3 * num) + 1

def inputValue(start):
    pass

print(odd(3))
print(even(2))