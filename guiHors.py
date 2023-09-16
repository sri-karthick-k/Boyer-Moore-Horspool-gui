import tkinter as tk
from tkinter import filedialog, messagebox
from functools import partial

# Your Boyer-Moore-Horspool code here
def boyer_moore_horspool(text, pattern):
    # ... (Your existing code)
    bad_char = {}
    pattern_length = len(pattern)
    
    for i in range(pattern_length - 1):
        bad_char[pattern[i]] = pattern_length - 1 - i
    
    i = 0
    while i <= len(text) - pattern_length:
        j = pattern_length - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            # Pattern found
            yield i

            # Shift the pattern based on bad character heuristic
            i += pattern_length if i + pattern_length < len(text) else 1
        else:
            # Shift the pattern based on bad character heuristic
            i += max(1, bad_char.get(text[i + j], 1))

def search_pattern_in_file(file_path, pattern):
    # ... (Your existing code)
    with open(file_path, 'r') as file:
        text = file.read()
        for match in boyer_moore_horspool(text, pattern):
            print(f"Pattern found at index {match}")

# Create a function to handle the search button click
def search_button_clicked():
    pattern = entry_pattern.get()
    file_path = file_path_label.cget("text")

    if not file_path:
        messagebox.showerror("Error", "Please select a file")
        return

    if not pattern:
        messagebox.showerror("Error", "Please enter a pattern to search")
        return

    search_pattern_in_file(file_path, pattern)

# Create the main GUI window
root = tk.Tk()
root.title("Pattern Search")

# Create and configure widgets
file_path_label = tk.Label(root, text="Select a file")
entry_pattern = tk.Entry(root, width=30)
search_button = tk.Button(root, text="Search", command=search_button_clicked)
select_file_button = tk.Button(root, text="Select File",
                               command=lambda: file_path_label.config(text=filedialog.askopenfilename()))

# Arrange widgets in the window
file_path_label.pack()
select_file_button.pack()
entry_pattern.pack()
search_button.pack()

# Start the GUI event loop
root.mainloop()
