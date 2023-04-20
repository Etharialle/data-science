# -*- coding: utf-8 -*-
import pandas as pd
import tkinter as tk
import tkinter.messagebox
import os

def onClick():
    tk.messagebox.showinfo("Split Complete", "Split Complete")

def split_file():
    # Get the source file name from the user
    source_file_name = entry_source_file.get()

    # Get the column header from the user
    column_header = entry_column_header.get()

    # Read the file into a Pandas DataFrame
    df = pd.read_csv(source_file_name)

    # Group the DataFrame by the column header
    groups = df.groupby(column_header)

    # Create a new directory for the output files
    if not os.path.exists("output"):
        os.mkdir("output")

    #set name to string
    # Iterate over the groups and write each group to a separate CSV file
    for name, group in groups:
        name = str(name)
        output_file_name = os.path.join("output", name + ".csv")
        group.to_csv(output_file_name, index=False)
        
    onClick()



# Create a Tkinter window
window = tk.Tk()

# Create a label for the source file
label_source_file = tk.Label(text="Source file:")

# Create an entry for the source file
entry_source_file = tk.Entry(width=20)

# Create a label for the column header
label_column_header = tk.Label(text="Column header:")

# Create an entry for the column header
entry_column_header = tk.Entry(width=20)

# Create a button to split the file
button_split = tk.Button(text="Split", command=split_file)

# Layout the widgets
label_source_file.grid(row=0, column=0)
entry_source_file.grid(row=0, column=1)
label_column_header.grid(row=1, column=0)
entry_column_header.grid(row=1, column=1)
button_split.grid(row=2, column=0)

# Start the event loop
window.mainloop()

