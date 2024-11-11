import csv #import csv

with open(r'C:\Users\mat_m\Downloads\GCSE Results Data.csv') as GCSE_result_unread: #open the file and save it information
    #print(GCSE_result) #this is a test print
    GCSE_result = csv.reader(GCSE_result_unread) #opens the variable with the file data and reads it then stores the read data as a new variable


    results68137 = []
    for row in GCSE_result: #for every row in the document
        if row[1] == '68137':
            results68137.append(row)

    print(results68137)

    first_line_file = open(r'C:\Users\mat_m\Downloads\GCSE Results Data.csv', 'r')
    first_line = first_line_file.readline()

    print(first_line)

