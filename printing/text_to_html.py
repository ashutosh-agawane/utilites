import glob
import os
import time
from pyhtml2pdf import converter


def text_to_html():
    names = [os.path.basename(x) for x in glob.glob("./*.txt")]
    for i in names:
        with open(i, 'r') as f:
            text = f.read()
            f.close()
            html_format = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <pre>'''+text+'''
                </pre>
            </body>
            </html>
                '''
            res = bytes(html_format, 'utf-8')
            replce = i.replace(".txt", "")
            hs = open("{}.html".format(replce), 'wb')
            hs.write(res)


def html_to_pdf():

    html_fi = [os.path.basename(x) for x in glob.glob("./*.html")]

    for j in html_fi:
        url = "file:///E:/python/data/printing/Shree_Ganesh_Offset/12052021/CDSL%202588%20TO%206000/CDSL%202588%20TO%206000/html_pdf/{}".format(
            j)
        print(url)
        k = j.replace(".txt.html", "")
        converter.convert(url, '{}.pdf'.format(k))
        print("done : "+k)


if __name__ == "__main__":
    begin = time.time()
    text_to_html()
    # html_to_pdf()
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")
