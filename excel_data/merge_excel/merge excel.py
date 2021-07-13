from os import lseek
import re
from sys import executable, path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import N
import pandas as pd
import glob
from pandas.core.indexes.datetimes import date_range
import datetime
import openpyxl
import threading
import time
# import xlwt
root = tk.Tk()
root.title("Excel Merge")
canvas1 = tk.Canvas(root, width=500, height=600,
                    bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='      Excel Merge     ', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 60, window=label1)


def get_excel():
    global filename, count
    import_directory_path = filedialog.askdirectory()
    filename = glob.glob(import_directory_path + "\*.xlsx")


browseButton_Excel = tk.Button(text="       Select Directory       ",
                               command=get_excel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 120, window=browseButton_Excel)


def get_excel_xls():
    global filename, count
    import_directory_path = filedialog.askdirectory()
    filename = glob.glob(import_directory_path + "\*.xls")


browseButton_Excel = tk.Button(text="       Select xlx Directory       ",
                               command=get_excel_xls, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 180, window=browseButton_Excel)


# def select_xls_directory():
#     global filename, count

#     import_directory_path = filedialog.askdirectory()
#     filename = glob.glob(import_directory_path + "\*.xlsx")


# browseButton_Excel = tk.Button(text="       Select Directory       ",
#                                command=select_xls_directory, bg='green', fg='white', font=('helvetica', 12, 'bold'))
# canvas1.create_window(250, 120, window=browseButton_Excel)


def date_wise():
    global filename, count

    li = []
    for file in filename:
        date = re.findall('[0-9]+', str(file))
        for d in date:
            date_obj = datetime.datetime.strptime(
                str(d), "%d%m%Y").date()
            read_file = pd.read_excel(file)
            read_file["Date"] = date_obj
            li.append(read_file)
            final = pd.concat(li, ignore_index=True)
    # count = final.shape[0]

    export_file_path = filedialog.asksaveasfilename(
        defaultextension='.xlsx')
    final.to_excel(export_file_path, index=False)
    messagebox.showinfo("Successfully Merged", "Done")


merge_file = tk.Button(text='      Get Date & Merge        ', command=date_wise,
                       bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 240, window=merge_file)


def merge():
    global filename, count

    all_data = pd.DataFrame()
    li = []
    for file in filename:
        read_file = pd.read_excel(file)
        # print(read_file)
        li.append(read_file)
        # print(li)
        final = pd.concat(li, ignore_index=True)
    # count = final.shape[0]
    # print(final)
    export_file_path = filedialog.asksaveasfilename(
        defaultextension='.xlsx')
    final.to_excel(export_file_path, index=False)
    messagebox.showinfo("Successfully Merged", "Done")


def main():
    thread = threading.Thread(target=merge)
    thread.start()
    # print("done")


merge_file = tk.Button(text='       Excel Merge        ', command=main,
                       bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 300, window=merge_file)


# def count():
#     global count

#     messagebox.showinfo("Count", "Rows : " + str(count))


# count = tk.Button(text='count', command=count,
#                   bg='green', fg='white', font=('helvetica', 12, 'bold'))
# canvas1.create_window(250, 360, window=count)


def exitApplication():
    MsgBox = tk.messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit     ',
                       command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 400, window=exitButton)
root.mainloop()

# def Testing():
#     filename = glob.glob("*.xlsx")
#     all_data = pd.DataFrame()
#     read_data = pd.DataFrame()
#     li = []
#     for file in filename:
#         # print(data)
#         x = re.findall('[0-9]+', str(file))
#         for i in x:
#             # print(i)
#             date_obj = datetime.datetime.strptime(str(i), "%d%m%Y").date()
#             # print(date_obj)

#             read_file = pd.read_excel(file)
#             print(read_file)
#             read_file["Date"] = date_obj
#             read_file["filename"] = file
#             li.append(read_file)
#             final = pd.concat(li, ignore_index=True)
#             final.to_excel("results1.xlsx", index=False)
#             print(final)


# Testing()

# final.to_excel("results1.xlsx", index=False)
# print(final)
# df = pd.concat(pd.read_excel(file, sheet_name=None),
#                ignore_index=True, sort=False)

# all_data = all_data.append(df, ignore_index=True)

# print(all_data)

# export_file_path = filedialog.asksaveasfilename(
# defaultextension='.xlsx')
# all_data.to_excel("results1.xlsx", index=False)

# all_data.to_excel(export_file_path, index=False)
