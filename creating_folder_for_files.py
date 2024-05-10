import os
import tkinter as tk
from tkinter import filedialog
import shutil
from typing import List


def create_folders_and_move_files(folder_path: str, file_list: List[str]) -> None:
    if not file_list:
        print("No new files found in the selected folder.")
        return

    file_names = []
    file_extensions = []

    # Extract file names and extensions
    for file in file_list:
        file_names.append(file)
        _, ext = os.path.splitext(file)
        file_extensions.append(ext)

    # Create folders and move files
    for ext in set(file_extensions):
        folder_name = ext[1:].capitalize()  # Remove the dot and capitalize the first letter
        folder_path_ext = os.path.join(folder_path, folder_name)
        for file, file_ext in zip(file_names, file_extensions):
            if file_ext == ext:
                if not os.path.exists(folder_path_ext):
                    os.makedirs(folder_path_ext, exist_ok=True)
                dest_file = os.path.join(folder_path_ext, os.path.basename(file))
                try:
                    shutil.move(file, dest_file)
                except Exception as e:
                    print(f"Error moving file '{os.path.basename(file)}': {e}")


def open_folder() -> None:
    folder_path = filedialog.askdirectory()
    if folder_path:
        files = [os.path.join(root_dir, file) for root_dir, _, files in os.walk(folder_path) for file in files]
        create_folders_and_move_files(folder_path, files)


# Create the main application window
root_window = tk.Tk()
root_window.title("File Selector")

# Create a button to open the folder
open_button = tk.Button(root_window, text="Open Folder", command=open_folder)
open_button.pack(pady=10)

# Run the application
root_window.mainloop()
