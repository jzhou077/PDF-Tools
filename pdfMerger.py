import tkinter as tk
from tkinter import filedialog

from pypdf import PdfMerger

import os

root = tk.Tk()
root.withdraw()

filenames = filedialog.askopenfilenames()

for file in os.listdir("outputFiles"):
    os.remove(file)

merger = PdfMerger()

for file in filenames:
    merger.append(file)

dest = input("Enter desired destination: ")
if dest == "downloads":
    dest = "C:/Users/jackz/Downloads/"

outputFilename = input("Output filename: ")

merger.write(dest + outputFilename + ".pdf")
merger.close()