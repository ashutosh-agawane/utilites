import win32api
import win32print
import glob
import os
import time
import win32ui
# A List containing the system printers
all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
# Ask the user to select a printer
printer_num = int(input("Choose a printer:\n" +
                  "\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
# set the default printer
win32print.SetDefaultPrinter(all_printers[printer_num])
names = [os.path.basename(x) for x in glob.glob("./*.pdf")]
# print(names)
# pdf_dir = "124287_M03300004778_04052021_Signed.pdf"
for f in names:
    win32api.ShellExecute(0, "print", f, None,  ".",  0)
    # dlg = win32ui.CreateFileDialog(0)
    # dlg.SetOFNInitialDir("C:")
    # flag = dlg.DoModal()
    # print(flag)

    time.sleep(12)
    os.system("TASKKILL /F /IM AcroRd32.exe")