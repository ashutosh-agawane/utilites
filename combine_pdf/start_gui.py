from tkinter import *
from tkinter import filedialog
import glob
from numpy import PINF, rot90
import pandas as pd
import os
import win32api
import win32print
import traceback
from tkinter import font  # * doesn't import font or messagebox
from pprint import pprint
import time
import sys
import threading
from tkinter import messagebox
import logging
from datetime import date, datetime as dt

logging.basicConfig(filename="logfilename.log", level=logging.DEBUG,
                    style='{', datefmt='%Y-%m-%d %H:%M:%S', format='{asctime} {levelname} {filename}:{lineno}: {message}')

root = Tk()
# root.attributes("-fullscreen", False)
root.geometry("410x310")
root.tk.call('encoding', 'system', 'utf-8')
root.configure(bg='lightsteelblue2', relief='raised')

# name = Label(root, text="Name").place(x=10, y=50)

# _printer = StringVar(root)
select_catagory = IntVar(root)
# var1 = IntVar()
# var2 = IntVar()

# def font_size(fs):
#     return font.Font(family='Helvetica', size=fs, weight='bold')


# def sel_printer(*args):
#     print(_printer.get())


# _printer.trace('w', sel_printer)

# choices = [printer[2] for printer in win32print.EnumPrinters(2)]
# _printer.set(win32print.GetDefaultPrinter())  # set the default option

# popupMenu = OptionMenu(root, _printer, *choices)
# popupMenu['font'] = font_size(10)
# Label(root, text="SELECT PRINTER").grid(row=1, column=1)
# popupMenu.grid(row=2, column=1)


def read_excel():
    global read_file, doc_name, final_cust_id, filename
    try:

        filename = filedialog.askopenfilename(
            title="Select a File", filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
        read_file = pd.read_excel(filename)
        # doc_name = read_file["Document No"].tolist()
        cust_id = read_file["Document No"].tolist()
        list_string = map(str, cust_id)
        final_cust_id = list(list_string)
        print(final_cust_id)

    except AssertionError as msg:
        print(msg)
        logging.error("error : " + str(msg))
        messagebox.showerror("File", "Please select file")

    # print(len(doc_name))
    # print(read_file)
    # for doc in doc_name:
    # print(doc_name)


def credit_note_and_debit_note():
    global read_file, doc_name, cn_dn_final
    try:
        cust_id = read_file["Document No"].tolist()
        # mon = read_file["Month"].tolist()
        list_string = map(str, cust_id)
        cn_dn_final = list(list_string)
        print(len(cn_dn_final))
    except Exception as e:
        print(e)
        logging.error("error : " + str(e))
        messagebox.showerror("File", "Please select Excel file")


def Incentive_letter():
    global read_file, incentive_final, mon, final
    try:

        cust_id = read_file["Customer ID"].tolist()
        mon = read_file["Month"].tolist()
        list_string = map(str, cust_id)
        incentive_final = list(list_string)
        # final = str(final_cust_id) + "_"+str(mon)
        print(len(incentive_final))

    except Exception as e:
        print(e)
        logging.error("error : " + str(e))

        messagebox.showerror("File", "Please select Excel file")


def select_pdf_directory_and_print():
    global read_file, doc_name, pdf_files
    try:

        import_directory_path = filedialog.askdirectory()
        print(import_directory_path)
        pdf_files = glob.glob(import_directory_path + "/*.pdf")

        # names = [os.path.basename(x) for x in glob.glob(
        # import_directory_path + "\*.pdf")]
        print(pdf_files)
    except Exception as e:
        print(e)
        logging.error("error : " + str(e))

        # messagebox.showerror("File", "Please select Excel file")


def print_btn_func():
    # global names,final_cust_id
    # win32print.SetDefaultPrinter(_printer.get())
    logging.info("================================")

    try:
        if select_catagory.get() == 1:
            for i, j in zip(incentive_final, mon):
                cat_1 = i+"_"+j

                cat_2 = i+"_V2_"+j

                cat_3 = i+"_V3_"+j

                for pdf_file in pdf_files:
                    # print("Yes  " + str(pdf_file)) if cat_1 in pdf_file else cat_2 in pdf_file
                    if cat_1 in pdf_file or cat_2 in pdf_file or cat_3 in pdf_file:
                        print("printing file : " + pdf_file)
                        logging.info("Completed : {}".format(pdf_file))
                        os.startfile(pdf_file, "print")

                        # win32api.ShellExecute(0, "print", pdf, None,  ".",  0)
                        time.sleep(10)
                        os.system("TASKKILL /F /IM AcroRd32.exe")
        else:
            for c in cn_dn_final:
                # print(c)
                for pdf_file in pdf_files:
                    if c in pdf_file:
                        print("printing file : " + pdf_file)
                        logging.info("Completed : {}".format(pdf_file))
                        os.startfile(pdf_file)

                        # win32api.ShellExecute(0, "print", pdf, None,  ".",  0)
                        time.sleep(10)
                        os.system("TASKKILL /F /IM AcroRd32.exe")
    except Exception as e:
        print(e)
        logging.error("error : " + str(e))
        messagebox.showerror(
            "Error", "Error")


def main():
    thread = threading.Thread(target=print_btn_func)
    thread.start()
    # print("done")


Browse = Button(root, command=read_excel,
                text="Excel Browse").place(x=160, y=60)

pdf_directory_btn = Button(root, command=select_pdf_directory_and_print,
                           text="select pdf folder").place(x=160, y=100)

R1 = Radiobutton(root, text="Incentive_letter", variable=select_catagory, value=1,
                 command=Incentive_letter).place(x=100, y=140)
R2 = Radiobutton(root, text="Credit Note & Debit Note", variable=select_catagory, value=2,
                 command=credit_note_and_debit_note).place(x=220, y=140)


print_btn = Button(root, command=main,
                   text="PRINT").place(x=160, y=180)

btn1 = Button(root, text='Quit !',
              command=root.destroy).place(x=160, y=240)

root.mainloop()
