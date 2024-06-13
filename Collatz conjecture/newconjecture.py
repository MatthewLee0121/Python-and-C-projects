import json
import sys
import matplotlib.pyplot as plt

values = None

plt.ion()

def main():
    global values
    while True:
        what_do = input("""
            What do you want to do?
            1) Run the main loop
            2) Write the data to file
            3) Write all values to file (run with care)
            4) Convert an external file of dictionaries into a graph
            5) Find the highest value of a given key
            0) Exit the program
            """)
        
        if what_do == "1":
            values = get_values()
        elif what_do == "2":
            write_to_new_file(values)
        elif what_do == "3":
            for x in range(0, sys.maxsize):
                values = get_values(x)
                write_to_new_file(values)
        elif what_do == "4":
            dictionaries = get_dictionaries()
            plot_multi_line_graph(dictionaries)
        elif what_do == "5":
            dictionaries = get_dictionaries6()
        elif what_do == "0":
            break

def get_values(num=None):
    step = 0
    if num is None: 
        start = input_value()
    else:
        start = num
    storage = {step: start}
    
    while start >= 2:
        if start % 2 == 0:
            step += 1
            start = even(start)
            storage[step] = start
        elif start % 2 == 1:
            step += 1
            start = odd(start)
            storage[step] = start
        if step >= 1001:
            return storage
    print(storage)
    return storage

def even(num):
    return num // 6 

def odd(num):
    return (9 * num) + 3

def input_value():
    return int(input("Enter a whole number: "))

def write_to_new_file(data):
    with open('stored_values.txt', 'a') as file:
        file.write(str(data) + '\n')

def get_dictionaries():
    dicts = []
    with open('stored_values.txt', 'r') as file:
        for line in file:
            try:
                d = eval(line.strip())
                dicts.append(d)
            except Exception as e:
                print(f"Error parsing line: {line.strip()}")
                print(f"Error message: {e}")
    return dicts

def get_dictionaries6():
    highest_values = {}
    with open('stored_values.txt', 'r') as file:
        for line in file:
            try:
                d = eval(line.strip())
                for key, value in d.items():
                    if key in highest_values:
                        if value > highest_values[key]:
                            highest_values[key] = value
                    else:
                        highest_values[key] = value
            except Exception as e:
                print(f"Error parsing line: {line.strip()}")
                print(f"Error message: {e}")
    print(highest_values)
    return highest_values

def plot_multi_line_graph(dicts):
    plt.figure(figsize=(12, 10))
    for d in dicts:
        x = list(d.keys())
        y = list(d.values())
        plt.plot(x, y, marker='x', label=None)
    
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.title('Collatz Sequence')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
