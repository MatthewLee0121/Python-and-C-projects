#Currently in progress of developing Tkinter UI
#Changes to inputs needs done
# 4) needs work.

counter = 0
import sys
import time
import pyautogui
import tkinter as tk
#imports sys and time mainly for typing function
#imports pyautogui for experimental option 4
#imports tkinters for GUI (experimental)

#function to immitate typing to give a nicer feel
def typing(message, delay = 0.01): #creates the function message is the input will often be the print statement delay is speed of typing
    for letter in message: #for every character in the print statement/string
        sys.stdout.write(letter) #writes to the system standard output
        sys.stdout.flush()#outputs the charater to the standard output "print()"
        time.sleep(delay) #delays for next letter
    return " "

#input boxes script function
def inputs():#creates a function for input boxes
    global counter #calls the global variable counter
    counter = 0 #sets it = to 0
    what_do = input(typing(""" 
1) Find and replace
2) How many occurances  
3) Copy the word lines to a new file
4) typing keyboard macro
0) Exit
.....""")) 
    #main function string to select the script you want the programme to run
    #1) Find and replace script to find and replace all occurances of a word in a file
    #2) how many occurances of the word exist in the file
    #3) Copies any lines in the file to a new file
    #4) experimental keyboard macro to help with youtube shorts (use at risk requires work)
    #0) Exit programme
    if what_do == "0": #if statement to exit programm
      typing("Exiting the programme, Thank you :)") 
      raise SystemExit 
    # asks some other inputs required by all functions
    file_path = input(typing("Please copy the file path. ")) #gets a file path to work on
    find = input(typing("What word do you want to find? ")) #gets a word to find from the file
    keep_lines = None #variable to tie in with option 3
    
    
    #can involve splicing here to eliminate false positives
    
    
    if what_do == '1': #initiating Find and replace script
      replace = input(typing("What word do you want to replace it with? ")) #gets a input value to replace the word with
      find_and_replace(file_path, find, replace) #calls the find and replace script function with the values of file_path find and replace as parameters
    elif what_do == '2':#initiating how many occurance script
      how_many(file_path, find) #no extra inputs needed here just runs the script with existing variables
    elif what_do == '3': #initiating copy lines scripting
      keep_lines = input(typing("Do you want to keep the original lines? ")) #input to see if the user wants to keep the original file lines
      new_file_created = copy_lines_to_new(file_path, find, keep_lines) #calls the main copy lines to new function and saves it to a variable for a print statement
      typing(f"New file: {new_file_created} if you wish to remove No match please select option 1 and replace No match with nothing") #print statement to inform user of new file
    elif what_do == '4': #initiates keyboard macro for youtube shorts
        content = typing_file(file_path) #creates a variable for the content of the macro after calling the file path through typing file function
        time.sleep(5) #delays for 5 seconds before typing for safety to avoid unwanted typing
        keyboard_macro(content) #passes content through keyboard macro
    else: #if a invalid input id declared need to find a new place for this higher up the code as it asks for extra inputs
      typing("Choose again")

    return what_do, file_path, find, keep_lines #returns the inputs

#define find and replace script
def find_and_replace(file_path, find, replace): #passes inputs as parameters
  global counter #inport global counter
# Read the file content    
  with open(file_path, 'r') as file: #opens the file to read it
    lines = file.readlines() #assign each line to a list of strings called lines

# Process each line and perform replacement
  for i in range(len(lines)): #iterate through each line of the file
      if find in lines[i]: #if find input is in the line
          counter += 1 #add one to the counter
          lines[i] = lines[i].replace(find, replace) # Replace the word in the line

# Write the updated content back to the file
  with open(file_path, 'w') as file: # opens file path in write mode now
      file.writelines(lines) 
  if counter == 0:
     typing(f"'{find}' not found")
  else:
    typing(f"{counter} Occurrences of '{find}' replaced with '{replace}' in the file.")


def how_many(file_path, find):
    global counter
    with open(file_path, 'r') as file:
        content = file.read()
        counter = content.count(find)
        
    typing(f"Total occurrences of '{find}' in the file: {counter}")

def copy_lines_to_new(file_path, find_word, keep_lines):
    # Define new file path to be in the find and replace folder
    new_file_path = rf"C:\Users\Coding_with_beans\python projects\find and replace folder\{find_word}"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if keep_lines[0] == "n":
        lines_with_word = [line for line in lines if find_word in line]
    else:
        lines_without_word = [line if find_word in line else "No match \n" for line in lines]

    # Opens the new file and writes the lines to it
    with open(new_file_path, 'w') as new_file:
        if keep_lines[0] == "n":
            new_file.writelines(lines_with_word)
        else:
            new_file.writelines(lines_without_word)

    return new_file_path

def keyboard_macro(message, delay=0.0001):
    for c in message:
        if c == '\n':
            # Handle newline (Enter) character
            pyautogui.press('enter')
        elif c == ' ':
            # Handle space character
            pyautogui.press('space')
        else:
            # Handle other characters
            pyautogui.typewrite(c)
        time.sleep(delay)
    time.sleep(1)  # Give time to switch to the desired window

def typing_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

what_do, file_path, find, keep_lines = inputs()

while (what_do != "0") == True:
   what_do, file_path, find, keep_lines = inputs()


#------------------------------------------UI----------------------------------------------------------------------
window = tk.Tk()# make a window in tkinter
window.title("Find And Replace Codingwithbeans")
#window parameters
window.geometry("500x800")
window.configure(bg="#f0f0f0")

window.mainloop()