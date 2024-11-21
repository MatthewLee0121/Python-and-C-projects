def reverse_string(input):
    reversed_input = input[:: -1]
     
    print(reversed_input)

reverse_string("hello")

def is_palindrome(input):
    if input == input[::-1]:
        return True
    else:
        return False
    
is_palindrome("radar")

def count_vowels(input):
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in input:
        if char in vowels:
            counter += 1
        else:
            pass


count_vowels("a")

for i in range (10, 1, -1):
    print(i)
