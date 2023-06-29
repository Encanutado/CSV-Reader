import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def get_csv_paths():
    csv_paths = filedialog.askopenfilenames(filetypes=[('CSV files', '*.csv')])
    
    num_files = len(csv_paths)
    num_files_label.config(text=f'{num_files} file(s) selected')
    
    update_table(csv_paths)

def update_table(csv_paths):
    csv_data = []

    for path in csv_paths:
        df = pd.read_csv(path)

        # Get the number of rows and columns in the CSV file
        num_rows = df.shape[0]
        num_cols = df.shape[1]

        # Add the data for this CSV file to the list
        csv_data.append({'File': os.path.basename(path), 'Rows': num_rows, 'Columns': num_cols})

    df = pd.DataFrame(csv_data)

    table.delete(*table.get_children())
    for index, row in df.iterrows():
        table.insert('', 'end', values=(row['File'], row['Rows'], row['Columns']))

root = tk.Tk()
root.title('CSV Info')
root.geometry('600x400')

file_label = tk.Label(root, text='Select CSV files:', font=('Arial', 14))
file_label.pack(pady=10)

file_button = tk.Button(root, text='Select Files', font=('Arial', 14), command=get_csv_paths)
file_button.pack()

num_files_label = tk.Label(root, text='', font=('Arial', 14))
num_files_label.pack(pady=10)

table_columns = ('File', 'Rows', 'Columns')
table = tk.ttk.Treeview(root, columns=table_columns, show='headings')
for col in table_columns:
    table.heading(col, text=col)
table.pack(pady=10)

root.mainloop()