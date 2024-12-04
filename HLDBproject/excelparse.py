import pandas as pd
from tkinter import filedialog
import os

file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls;*.csv"), ("All Files", "*.*")])
sheet_name = "Combined HR" 
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
df = df.iloc[1:] 

unique_values = {}
for column in df.columns:
    unique_values[column] = list(df[column].dropna().unique())

def write_to_new_file(unique_values):
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unique_values2.txt')
    with open(output_path, 'w') as file:
        for column, values in unique_values.items():
            file.write(f"{column}:\n")
            file.write(f"{values}\n\n") 

write_to_new_file(unique_values)
