#Currently in progress of developing Tkinter UI
#Changes to inputs needs done
#if__name__=='__main__' main script file

counter = 0
import sys
import time
import tkinter as tk
#imports sys and time mainly for typing function
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
0) Exit
.....""")) 
    #main function string to select the script you want the programme to run
    #1) Find and replace script to find and replace all occurances of a word in a file
    #2) how many occurances of the word exist in the file
    #3) Copies any lines in the file to a new file
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
    else: #if a invalid input id declared
      typing("Choose again")

    return what_do, file_path, find, keep_lines #returns the inputs

def find_and_replace(file_path, find, replace): #starts the find and replace scripting
  global counter #imports global counter
  with open(file_path, 'r') as file: #opens file in read mode
    lines = file.readlines() #saves each line to a list of strings 

  for i in range(len(lines)):# Process each line and perform replacement iterating over each index
      if find in lines[i]: #if the word is found in the line
          counter += 1 #add one to the counter
          # Replace the word in the line
          lines[i] = lines[i].replace(find, replace) #replaces find with replace within the list

  with open(file_path, 'w') as file:# Write the updated content back to the file with the file open in write mode
      file.writelines(lines) #write the lines as the list
  if counter == 0: #if counter is 0 then we didnt replace anything
     typing(f"'{find}' not found") #informs the user
  else:
    typing(f"{counter} Occurrences of '{find}' replaced with '{replace}' in the file.") #informs the users how many occurances of find was replaced
    counter = 0 #resets the counter


def how_many(file_path, find): #starts the how many occurances scripting
    global counter #imports the global counter
    with open(file_path, 'r') as file: #opens file in read mode
        content = file.read() #returns the file content as a string
        counter = content.count(find) #counters how many times find occurs in the string
        
    typing(f"Total occurrences of '{find}' in the file: {counter}") #accounces output of script

def copy_lines_to_new(file_path, find_word, keep_lines): #starts copying lines to new function
    new_file_path = rf"C:\Users\matty\Coding_with_beans\python projects\find and replace folder\{find_word}"# Define new file path to be in the find and replace folder consinder input? or way to change this within the scripting and save it
    
    with open(file_path, 'r') as file: #opens file in read
        lines = file.readlines() #saves each line to a list

    if keep_lines[0] == "n": #if keep lines first character is n then we dont want the original lines
        lines_with_word = [line for line in lines if find_word in line] #creates a list lines_with_word that saves every line with the word to the new list and passes over none
    else: #if we want to keep the lines
        lines_without_word = [line if find_word in line else "No match \n" for line in lines] #same as above but new list this one will replace each line in the list with no match instead

    # Opens the new file and writes the lines to it
    with open(new_file_path, 'w') as new_file:# Opens the new file and writes the lines to it
        if keep_lines[0] == "n":#if statement to decided which list to save the new file as
            new_file.writelines(lines_with_word) #writes list to new file
        else:
            new_file.writelines(lines_without_word)

    return new_file_path #outputs the new file path

what_do, file_path, find, keep_lines = inputs() #starts the script

while (what_do != "0") == True: #loops the inputs while 0 is not selected
   what_do, file_path, find, keep_lines = inputs()


#------------------------------------------UI----------------------------------------------------------------------
window = tk.Tk()# make a window in tkinter
window.title("Find And Replace Codingwithbeans") #names the programme
#window parameters
window.geometry("1000x1600") #starting small
window.configure(bg="#f0f0f0") #setting background

set_file_path_button = tk.Button(
    window,
    text = "Set a file path"
    
)

find_and_replace_button = tk.Button(
    window,
    text = "Find and Replace"
)

occurances_button = tk.Button(
    window,
    text = "How many occurances"
)

copy_file_to_new_button = tk.Button(
    window,
    text = "Copy the lines to a new file"
)

exit_button = tk.Button(
    window,
    text = "Exit"
)
window.mainloop() #UI loop