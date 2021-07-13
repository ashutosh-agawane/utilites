from os import lseek
import re
from sys import executable, path
import tkinter as tk
from tkinter import IntVar, filedialog
from tkinter import messagebox
from tkinter.constants import N
import pandas as pd
from glob import glob
from pandas.core.indexes.datetimes import date_range
import datetime
import openpyxl
import threading
import time
from os.path import join
import os
 
# import xlwt
# root = tk.Tk()
# root.title("Excel Merge")

# root.geometry("500x600")
# root.tk.call('encoding', 'system', 'utf-8')
# root.configure(bg='lightsteelblue2', relief='raised')

# var1 = IntVar(root)


# def get_excel():
#     global files, count
#     files = []
#     import_directory_path = filedialog.askdirectory()
#     # filename = glob.glob(import_directory_path + "\*.xlsx")
#     for ext in ('*.xlsx', '*.xls'):
#         files.extend(os.path.basename(x)
#                      for x in glob(join(import_directory_path, ext)))
#     print(files)

# # def get_excel():
# #     global files, count
# #     files = filedialog.askopenfilename(
# #         title="Select a File", filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
# #     # filename = glob.glob(import_directory_path + "\*.xls")


# # def select_xls_directory():
# #     global filename, count

# #     import_directory_path = filedialog.askdirectory()
# #     filename = glob.glob(import_directory_path + "\*.xlsx")


# # browseButton_Excel = tk.Button(text="       Select Directory       ",
# #                                command=select_xls_directory, bg='green', fg='white', font=('helvetica', 12, 'bold'))
# # canvas1.create_window(250, 120, window=browseButton_Excel)


# def date_wise():
#     global files, count

#     li = []
#     for file in files:
#         date = re.findall('[0-9]+', str(file))
#         for d in date:
#             date_obj = datetime.datetime.strptime(
#                 str(d), "%d%m%Y").date()
#             read_file = pd.read_excel(file)
#             read_file["Date"] = date_obj
#             li.append(read_file)
#             final = pd.concat(li, ignore_index=True)
#     # count = final.shape[0]

#     export_file_path = filedialog.asksaveasfilename(
#         defaultextension='.xlsx')
#     final.to_excel(export_file_path, index=False)
#     messagebox.showinfo("Successfully Merged", "Done")


# def merge():
#     global files, count

#     # print(files)

#     all_data = pd.DataFrame()
#     li = []
#     for file in files:
#         read_file = pd.read_excel(file)
#         print(read_file)
#         li.append(read_file)
#         # print(li)
#         # final = pd.concat(li, ignore_index=True)
#     # count = final.shape[0]
#     # print(final)
#     # export_file_path = filedialog.asksaveasfilename(
#     # defaultextension='.xlsx')
#     # final.to_excel(export_file_path, index=False)
#     # messagebox.showinfo("Successfully Merged", "Done")


# # def main():
# #     thread = threading.Thread(target=merge)
# #     thread.start()
#     # print("done")


# browseButton_Excel = tk.Button(text="Select Directory",
#                                command=get_excel, bg='blue', fg='white', font=('helvetica', 12, 'bold')).place(x=160, y=150)

# date_merge_file = tk.Button(text='by date', command=date_wise,
#                             bg='green', fg='white', font=('helvetica', 12, 'bold')).place(x=160, y=200)

# merge_file = tk.Button(text='Merge', command=merge,
#                        bg='green', fg='white', font=('helvetica', 12, 'bold')).place(x=160, y=250)

# # browseButton_Excel = tk.Button(text="       Select Directory       ",
# #                                command=get_excel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
# # canvas1.create_window(250, 120, window=browseButton_Excel)


# # def count():
# #     global count

# #     messagebox.showinfo("Count", "Rows : " + str(count))


# # count = tk.Button(text='count', command=count,
# #                   bg='green', fg='white', font=('helvetica', 12, 'bold'))
# # canvas1.create_window(250, 360, window=count)


# def exitApplication():
#     MsgBox = tk.messagebox.askquestion(
#         'Exit Application', 'Are you sure you want to exit the application', icon='warning')
#     if MsgBox == 'yes':
#         root.destroy()


# # exitButton = tk.Button(root, text='       Exit     ',
#         #    command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
# # canvas1.create_window(250, 400, window=exitButton)
# root.mainloop()

def Testing():
    new_xlsx_path = r"C:\Users\Vikrant\Documents\merge-file"
    path = r"C:\Users\Vikrant\Documents\post_data\post\vashi"
    filename = []
    for ext in ('*.xlsx', '*.xls'):

        filename.extend(os.path.basename(x)
                        for x in glob(join(new_xlsx_path, ext)))
    # filename = glob.glob("*.xlsx")
    # print(filename)
    all_data = pd.DataFrame()
    read_data = pd.DataFrame()
    li = []
    for file in filename:
        # print(file)
        read_file = pd.read_excel(file)
        print(read_file)

        # x = re.findall('[0-9]+', str(file))
        # for i in x:
        # print(i)
        # date_obj = datetime.datetime.strptime(str(i), "%d%m%Y").date()
        # print(date_obj)

        # read_file = pd.read_excel(file)
        # print(read_file)
        # read_file["Date"] = date_obj
        # read_file["filename"] = file
        # li.append(read_file)
        # final = pd.concat(li, ignore_index=True)
        # final.to_excel("results1.xlsx", index=False)
        # print(final)


Testing()

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
