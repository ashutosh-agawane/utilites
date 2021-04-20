from tkinter import *
from tkinter import filedialog
from numpy import select
import pandas as pd
from tkinter import messagebox
import glob
import os
import win32api
import win32print

import time
root = Tk()

root.title("Star")
root.geometry("410x310")
root.tk.call('encoding', 'system', 'utf-8')


class GUI:
    def __init__(self, main):
        frame = Frame(main)
        frame.pack()

        self.browse = Button(main, text="browse", command=self.browse_excel)
        self.browse.pack(pady=10)

        self.select = Button(main, text="select PDF's",
                             command=self.select_pdf_directory)
        self.select.pack(pady=20)

        self.printing = Button(main, text="PRINT",
                               command=self.print_btn_func)
        self.printing.pack(pady=30)

        self.exit = Button(main, text="Quit !",
                           command=self.exit)
        self.exit.pack(pady=30)

    def browse_excel(self):
        global read_file, doc_name, final_cust_id, filename

        try:
            filename = filedialog.askopenfilename(
                title="Select a File", filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
            read_file = pd.read_excel(filename)
            cust_id = read_file["Customer ID"].tolist()
            list_string = map(str, cust_id)
            final_cust_id = list(list_string)
            print(final_cust_id)
        except AssertionError:
            messagebox.showerror("File", "Please select file")
            root.destroy()

    def select_pdf_directory(self):
        global read_file, doc_name, names

        import_directory_path = filedialog.askdirectory()
        print(import_directory_path)
        names = [os.path.basename(x) for x in glob.glob(
            import_directory_path + "\*.pdf")]
        print(names)

    def print_btn_func(self):
        try:
            for c in final_cust_id:
                for pdf in names:
                    if c in pdf:
                        # messagebox.showerror("PDF's", pdf)
                        print("printing file : " + pdf)
                        # os.startfile(pdf, "print")
                        win32api.ShellExecute(0, "print", pdf, None,  ".",  0)
                        # time.sleep(10)
                        # os.system("TASKKILL /F /IM AcroRd32.exe")
        except Exception as e:
            print(e)
        messagebox.showerror(
            "Error", "There was an error printing the file :(")

    def exit(self):
        root.destroy()


e = GUI(root)
root.mainloop()
