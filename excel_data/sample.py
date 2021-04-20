# from docx import Document
# import re
import pandas as pd
import tkinter

import numpy as np
import glob

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from xls2xlsx import XLS2XLSX

root = tk.Tk()
root.title("xls to xlsx converter")
canvas1 = tk.Canvas(root, width=300, height=300,
                    bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='XLX To XLSX', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getExcel():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = XLS2XLSX(import_file_path)


browseButton_Excel = tk.Button(text="      Import Excel File     ",
                               command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_Excel)


def convert():
    global read_file

    # x2x = XLS2XLSX("blue_dart1.xls")

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    # read_file.to_csv(export_file_path, index=None, header=True)
    read_file.to_xlsx(export_file_path)


saveAsButton_CSV = tk.Button(text='Convert XLS to XLSX', command=convert,
                             bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)

root.mainloop()

# filename = "sample.docx"

# from xls2xlsx import XLS2XLSX
# x2x = XLS2XLSX("blue_dart1.xls")
# x2x.to_xlsx("blue_dart1.xlsx")


# document = Document(filename)

# for p in document.paragraphs:
#     # txt = p.text
#     print(p)
#     # x = re.search("^antiopam*ipsum$", txt)

#     # TITLE = r"(?:[A-Z][a-z]*\.\s*)?"

#     # r = re.findall(TITLE, txt)
#     # print(r)
#     # print(x)
# f1 = pd.read_excel("excel_1.xlsx")
# f2 = pd.read_excel("excel_2.xlsx")
# f3 = pd.read_excel("excel_3.xlsx")
# f4 = pd.read_excel("excel_4.xlsx")
# f5 = pd.read_excel("excel_5.xlsx")

# path = r'C:\Users\Vikrant\Documents\data\excel_data'

# filename = glob.glob(path + "\*.xlsx")
# # print(filename)
# all_data = pd.DataFrame()

# for f in filename:
#     df = pd.concat(pd.read_excel(f, sheet_name=None),
#                    ignore_index=True, sort=False)

#     final = all_data.append(df, ignore_index=True)

# # print(final)
# final.to_excel("results1.xlsx", index=False)


# all_data = all_data.append(df, ignore_index=True)

# print(all_data)

# f1 = pd.read_excel("blue_dart.xlsx")
# f2 = pd.read_excel("blue_dart1.xlsx")

# df = pd.concat(pd.read_excel(
# 'excel_1.xlsx', sheet_name=None), ignore_index=True)
# print(f1)

# f3 = f1.merge(f2)
# f3 = pd.concat([f1, f2])


# f3.to_excel("results.xlsx", index=False)
# print(f2)
