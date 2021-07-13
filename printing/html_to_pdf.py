import glob
import os
import time
from pyhtml2pdf import converter


def html_to_pdf():

    html_fi = [os.path.basename(x) for x in glob.glob("./*.html")]

    for j in html_fi:
        path = os.path.abspath(j)
        converter.convert(f'file:///{path}', '{}.pdf'.format(j))
        print("done : "+j)


begin = time.time()
html_to_pdf()
end = time.time()
print(f"Total runtime of the program is {end - begin}")
