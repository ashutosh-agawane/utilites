import fnmatch
from struct import pack_into
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
from tkinter import *
from pandas.core.indexes.datetimes import date_range
import threading
import os
from escpos.connections import getFilePrinter, getNetworkPrinter
import PyPDF2
import json
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
# import
from pdfrw import PdfReader
from tkinter import Tk
from tkinter import filedialog
import sys
root = Tk()
# root.attributes("-fullscreen", False)
root.geometry("410x310")
root.tk.call('encoding', 'system', 'utf-8')
root.configure(bg='lightsteelblue2', relief='raised')


def select_pdf_directory():
    global names

    import_directory_path = filedialog.askdirectory()
    # pdf_files = glob.glob(import_directory_path + "/*.pdf")
    names = [os.path.basename(x)
             for x in glob.glob(import_directory_path+"/*.pdf")]

    print(names)


def execute1():
    # pass
    pdfs = []
    page_count_list = []
    height = []
    width = []
    for pdf_file in names:
        # print(pdf_file)

        object = PyPDF2.PdfFileReader(pdf_file)
        pdfr = PdfReader(pdf_file)

        # print(object)
        # object.decrypt('')
        # if object.isEncrypted:
        #     object.decrypt('')
        #     print
        NumPages = object.getNumPages()

        pdfs.append(pdf_file)
        page_count_list.append(NumPages)
        # page_size
        # page_size = object.getPage(0).mediaBox
        # print(page_size.get)

        s = pdfr.pages[0].MediaBox
        # for i in

        # for i in s:
        # print(i[2][3])
        # page_size.append(s)
        # print(s[2], s[3])
        height.append(s[2])
        width.append(s[3])
    # print(height, width)
    # heght = s[]
    # li = [pdf_file]
    # print(page_size)
    dis = {"PDF": pdfs, "page_count": page_count_list,
           "height": height, "width": width}
    # df = pd.DataFrame(data=dis)
    # print(dis)
    json_object = json.dumps(dis, indent=4)
    # pd.read_json(json_object).to_excel("output.xlsx")
    export_file_path = filedialog.asksaveasfilename(
        defaultextension='.xlsx')
    pd.read_json(json_object).to_excel(export_file_path)
    print(json_object)

    messagebox.showinfo("Success", "Done")


pdf_directory_btn = Button(root, command=select_pdf_directory,
                           text="select pdf folder").place(x=160, y=100)

execute1 = Button(root, command=execute1,
                  text="Execute").place(x=160, y=180)

btn1 = Button(root, text='Quit !',
              command=root.destroy).place(x=160, y=240)

root.mainloop()

sys.exit()

names = [os.path.basename(x) for x in glob.glob("*.pdf")]
pdfs = []
page_count_list = []
height = []
width = []
for pdf_file in names:
    # print(pdf_file)

    object = PyPDF2.PdfFileReader(pdf_file)
    pdfr = PdfReader(pdf_file)

    # print(object)
    # object.decrypt('')
    # if object.isEncrypted:
    #     object.decrypt('')
    #     print
    NumPages = object.getNumPages()

    pdfs.append(pdf_file)
    page_count_list.append(NumPages)
    # page_size
    # page_size = object.getPage(0).mediaBox
    # print(page_size.get)

    s = pdfr.pages[0].MediaBox
    # for i in

    # for i in s:
    # print(i[2][3])
    # page_size.append(s)
    # print(s[2], s[3])
    height.append(s[2])
    width.append(s[3])
print(height, width)
# heght = s[]
# li = [pdf_file]
# print(page_size)
dis = {"PDF": pdfs, "page_count": page_count_list,
       "height": height, "width": width}
# df = pd.DataFrame(data=dis)
# print(dis)
json_object = json.dumps(dis, indent=4)
pd.read_json(json_object).to_excel("output.xlsx")

print(json_object)

# df = pd.DataFrame({"pdf": pdf_file, "page_count": NumPages}, index=[0])
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# writer.save()

# dist1 = {"pdf": pdf_file,
#  "page_count": NumPages
#  }
