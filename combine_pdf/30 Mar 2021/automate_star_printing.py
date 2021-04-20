import fnmatch
from openpyxl import load_workbook
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import re
from sys import executable, path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import N
import pandas as pd
import glob
from pandas.core.indexes.base import Index

from pandas.core.indexes.datetimes import date_range
import datetime
import time
import os
from escpos.connections import getFilePrinter, getNetworkPrinter
# from win32printing import Printer
import win32print
import win32api
import tempfile
import socket
import win32con
# import win32ui
# from win32printing import Printer
from win32printing import PrinterBase, Printer
# from PDFNetPython3 import *
import openpyxl
import time
import itertools
import PyPDF2
import re
# all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
# Ask the user to select a printer
# printer_num = int(input("Choose a printer:\n" +
# "\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
# set the default printer
# win32print.SetDefaultPrinter(all_printers[printer_num])
pdf_dir = "E:/python/data/combine_pdf/NTO_INC_LETTERS-30.03.2021"
pdf_files = glob.glob(pdf_dir + "/*.pdf")
# names = [os.path.basename(x) for x in glob.glob(
#     pdf_dir + "/*.pdf")]

print(pdf_files)
# filename = "122940_SEP'2020_Signed.pdf"
files = "DISPATCH LIST_INC_LETTER_30-MAR-2021.xlsx"
# files = "List of Inc. Letters for Dispatch Mar 10, 2021.xlsx"
# for i in doc_name:

#     for pdf_file in file:
#         # print(pdf_file)
#         if i in pdf_file:
#             os.startfile(pdf_file)
#             print("opening pdf  " + str(pdf_file))

#             time.sleep(10)

#             os.system("TASKKILL /F /IM AcroRd32.exe")

# files = "List of Inc. Letters for Dispatch Mar 10, 2021.xlsx"
filename = pd.read_excel(files)
# doc_name = filename["Document No"].tolist()
# print (doc_name)
cust_id = filename["Customer ID"].tolist()
mon = filename["Month"].tolist()
# print(mon)
list_string = map(str, cust_id)
final_cust_id = list(list_string)
print(final_cust_id)
# final = str(final_cust_id) + "_"+str(mon)
# for i, j in zip(final_cust_id, mon):
# for c in final_cust_id:
# print(c)
# for pdf_file in pdf_files:
# if c in pdf_file:
# print("printing file : " + pdf_file)
# os.startfile(pdf_file, "print")
# messagebox.showerror("PDF's", pdf)

# win32api.ShellExecute(0, "print", pdf, None,  ".",  0)
# time.sleep(10)
# os.system("TASKKILL /F /IM AcroRd32.exe")
#     cat = i
#     cat_1 = i+"_"+j

#     cat_2 = i+"_V2_"+j

#     cat_3 = i+"_V3_"+j

#     # print(cat_4)

#     for pdf_file in names:
#         # print("Yes  " + str(pdf_file)) if cat_1 in pdf_file else cat_2 in pdf_file
#         if cat_1 in pdf_file or cat_2 in pdf_file or cat_3 in pdf_file:
#             print("Yes  " + str(pdf_file))

# elif cat_2 in pdf_file:
#     print("Yes  " + str(pdf_file))
# elif cat_3 in pdf_file:
#     print("Yes  " + str(pdf_file))

# print(final)
# for i in final:
# print(i)
# k = i + "_"

# for pdf in names:
# print(pdf)
# if i in pdf:
# print("Yes : " + pdf)

# print(final_cust_id)
# if
# for i in names:
#     print(i)
#     object = PyPDF2.PdfFileReader(i)

#     NumPages = object.getNumPages()

#     String = final_cust_id
#     for ids in String:
#         for i in range(0, NumPages):
#             PageObj = object.getPage(i)
#             print("this is page " + str(i))
#             Text = PageObj.extractText()
#             # print(Text)
#             ResSearch = re.search(ids, Text)
#             print(ResSearch)
# time.sleep(10)

# for pdf_file in file:
# print(pdf_file)
# if i in pdf_file:
# print("opening pdf  " + str(pdf_file))
# time.sleep(30)

# os.startfile(pdf_file,"print")

# win32api.ShellExecute(0, "print", pdf_file, None,  ".",  0)

# time.sleep(10)

# os._exit(os.EX_OK)
# os.system("TASKKILL /F /IM AcroRd32.exe")

# print(lenth // 50)
# matrix = []

# for i in range(2):
#     # print(i)
#     matrix.append([])
#     for j in range(50):
#         matrix[i].append(j)
# print(matrix)

# i = "122940"
# for i, j in zip(final_cust_id, mon):

#     k = i+"_"+j

#     for pdf_file in file:
#         # print(pdf_file)
#         if k in pdf_file:
#             print("Yes  " + str(pdf_file))
# time.sleep(5)
# win32api.ShellExecute(0, "print", pdf_file, None,  ".",  0)
# import os
# import time

# creating a forever loop
# os.system("TASKKILL /F /IM AcroRd32.exe")
# time.sleep(10)
# import os
# os.startfile("ChkBnce_122038_Inst.No._1296 & 1297_24032021_Signed.pdf", "print")
