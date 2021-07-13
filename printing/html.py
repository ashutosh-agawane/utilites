import glob
import codecs
import io
import pdfkit
import os
import time
from pyhtml2pdf import converter
files = glob.glob('./*.txt')

# print(files)
for i in files:
    # print(i)
    with open(i, 'r') as f:
        text = f.read()

        f.close()

        # print(text)
        strTable = '''
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
        # print(strTable)
        res = bytes(strTable, 'utf-8')

        hs = open("{}.html".format(i), 'wb')
        hs.write(res)
        time.sleep(5)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            for file in files:

                if file.endswith('.html'):
                    # print(file)
                    converter.convert(file, '{}.pdf'.format(i))

            # print(root+'/'+str(file))

        # html_files = glob.glob(
        #     'E:/python/data/printing/Shree_Ganesh_Offset/12052021/CDSL 0000 TO 2587/CDSL 0000 TO 2587/files./*.html')
        # # print(html_files)
        # for j in html_files:
        #     print(j)
        #     converter.convert(j, '{}.pdf'.format(i))
