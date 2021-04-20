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
from PyPDF2 import PdfFileReader, PdfFileWriter
# import

# # all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
# # Ask the user to select a printer
# # printer_num = int(input("Choose a printer:\n" +
# # "\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
# # set the default printer
# # win32print.SetDefaultPrinter(all_printers[printer_num])
# # pdf_dir = "E:/python/data/combine_pdf/31 Mar 2021/NTO_INC_LETTERS-30.03.2021"
# # pdf_files = glob.glob(pdf_dir)
# # names = [os.path.basename(x) for x in glob.glob(
# # pdf_dir + "/*.pdf")]

# # print(names)
# # pdf_read = "23365285_NTO_INC_LETTER_DATE_WISE_Signed.pdf"
# # files = "11_Dec-2020 Speed Post_Data.xlsx"
# files = "31_Mar-2021 Speed Post_Data.xlsx"
# # for i in doc_name:

# #     for pdf_file in file:
# #         # print(pdf_file)
# #         if i in pdf_file:
# #             os.startfile(pdf_file)
# #             print("opening pdf  " + str(pdf_file))

# #             time.sleep(10)

# #             os.system("TASKKILL /F /IM AcroRd32.exe")

# # files = "List of Inc. Letters for Dispatch Mar 10, 2021.xlsx"
# filename = pd.read_excel(files)
# # doc_name = filename["Document No"].tolist()
# # print (doc_name)
# cust_id = filename["Customer ID"].tolist()
# mon = filename["Month"].tolist()
# # print(mon)
# list_string = map(str, cust_id)
# final_cust_id = list(list_string)
# final = str(final_cust_id) + "_"+str(mon)
# # print(final)
# # for i, j in zip(final_cust_id, mon):

# #     cat = i
# #     cat_1 = i+"_"+j

# #     cat_2 = i+"_V2_"+j

# #     cat_3 = i+"_V3_"+j

# #     # print(cat_4)

# #     for pdf_file in names:
# #         # print("Yes  " + str(pdf_file)) if cat_1 in pdf_file else cat_2 in pdf_file
# #         if cat_1 in pdf_file or cat_2 in pdf_file or cat_3 in pdf_file:
# #             print("Yes  " + str(pdf_file))

# # elif cat_2 in pdf_file:
# #     print("Yes  " + str(pdf_file))
# # elif cat_3 in pdf_file:
# #     print("Yes  " + str(pdf_file))

# # print(final)
# # for i in final:
# # print(i)
# # k = i + "_"

# # for pdf in names:
# # print(pdf)
# # if i in pdf:
# # print("Yes : " + pdf)

# # print(final_cust_id)
# # if
# # pdf_files = glob.glob("/*.pdf")
# # print(pdf_files)
# names = [os.path.basename(x) for x in glob.glob("*.pdf")]
# # # for i, j in zip(final_cust_id, mon):

# # #     cat = i
# # #     cat_1 = i+"_"+j

# # #     cat_2 = i+"_V2_"+j

# # #     cat_3 = i+"_V3_"+j

# # #     # print(cat_4)

# for pdf_file in names:
#     # print("Yes  " + str(pdf_file)) if cat_1 in pdf_file else cat_2 in pdf_file
#     # if cat_1 in pdf_file or cat_2 in pdf_file or cat_3 in pdf_file:
#     # print("found " + str(pdf_file))
#     object = PyPDF2.PdfFileReader(pdf_file)
#     # print(object)
#     NumPages = object.getNumPages()
#     print(NumPages)
#     String = final_cust_id

#     # print(String)

#     for ids in String:
#         for i in range(0, NumPages):
#             # print(i)
#             PageObj = object.getPage(i)

#     # print(PageObj)
#             # print("this is page " + str(i))
#     # Text = PageObj.extractText()
#     # print(Text)
#     # ResSearch = re.search(ids, Text)
#     # print(ResSearch)
#     # if ResSearch != None:
#     # print("yes : "+str(ids))
#     # os.startfile(pdf_file, "print")
#     # os.system("TASKKILL /F /IM AcroRd32.exe")


# # time.sleep(10)

# # for pdf_file in file:
# # print(pdf_file)
# # if i in pdf_file:
# # print("opening pdf  " + str(pdf_file))
# # time.sleep(30)

# # os.startfile(pdf_file,"print")

# # win32api.ShellExecute(0, "print", pdf_file, None,  ".",  0)

# # time.sleep(10)

# # os._exit(os.EX_OK)
# # os.system("TASKKILL /F /IM AcroRd32.exe")

# # print(lenth // 50)
# # matrix = []

# # for i in range(2):
# #     # print(i)
# #     matrix.append([])
# #     for j in range(50):
# #         matrix[i].append(j)
# # print(matrix)

# # i = "122940"
# # for i, j in zip(final_cust_id, mon):

# #     k = i+"_"+j

# #     for pdf_file in file:
# #         # print(pdf_file)
# #         if k in pdf_file:
# #             print("Yes  " + str(pdf_file))
# # time.sleep(5)
# # win32api.ShellExecute(0, "print", pdf_file, None,  ".",  0)
# # import os
# # import time

# # creating a forever loop
# # os.system("TASKKILL /F /IM AcroRd32.exe")
# # time.sleep(10)
# pdf_splitter.py

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    # print(fname)
    files = "31_Mar-2021 Speed Post_Data.xlsx"

    filename = pd.read_excel(files)
    cust_id = filename["Customer ID"].tolist()
    list_string = map(str, cust_id)
    final_cust_id = list(list_string)
    pdf = PdfFileReader(path)
    count = 0
    for page in range(pdf.getNumPages()):
        # print(page)
        for i in final_cust_id:
            PageObj = pdf.getPage(page)
            # print(PageObj)
            # print("this is page " + str(i))
            Text = PageObj.extractText()
            # print(Text)
            ResSearch = re.search(i, Text)
            count = count + 1
            print(count)
            # print(ResSearch)
            # if ResSearch != None:
            # print("yes : "+str(i))

        #     # print(i)
        #     # print(page)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
        # print(pdf_writer)

            output_filename = 'E:/python/data/combine_pdf/test/{}_page_{}_{}.pdf'.format(
                fname, page+1, i)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            print('Created: {}'.format(output_filename))
        # break


if __name__ == '__main__':
    path = 'LetterNo.01_RIO49_Final.pdf'
    # names = [os.path.basename(x) for x in glob.glob("*.pdf")]
    pdf_splitter(path)
