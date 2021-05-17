# from logging import debug
# from re import I
# from typing import final
# from flask import Flask
# from flask import json
# from flask.json import jsonify

# from pymongo import MongoClient

# app = Flask(__name__)
# app.config["DEBUG"] = True

# client = MongoClient()
# db = client["vikrant"]


# @app.route('/', methods=['GET'])
# def hello_world():
#     return "hello"


# @app.route('/api', methods=['GET'])
# def get_api():
#     input_data = db.data.find()

#     output = []
#     for i in input_data:
#         # print(i["Post_Barcode"])
#         output.append({'awbno': i["awbno"], 'date': i['date'],
#                        'time': i['time'], 'office': i['office'], 'status': i['status']})
#         # print(output)
#     return jsonify({"results": output})


# @app.route('/api/', methods=['GET', 'POST'])
# def get_one_star(awbno):
#     i = db.data.find_one({'awbno': awbno})
#     # print(input_data)
#     if i:
#         output = {'awbno': i["awbno"], 'date': i['date'],
#                   'time': i['time'], 'office': i['office'], 'status': i['status']}
#     else:
#         output = "no data found"
#     return jsonify({'result': output})


# if __name__ == '__main__':
#     app.run()

{"awbno": "AN233455",
 "weight": "0.98",
 "deliverystatus": "No Service",
 "deliverydate": "02-May-2021",
 "returnreason": "",
 "receivername": "",
 "relation": "",
 "receivernumber": "",
 "referenceno": "",
 "noservice": "",
 "physicalcopystatus": "",
 "barcode": "19022020686201",
 "deliveryproof": ""
 }

img_url = ob.full_Screenshot(
    driver, save_path=r'.', image_name='sceenshot.png')
image1 = Image.open(r'sceenshot.png')
im1 = image1.convert('RGB')
im1.save(
    r'E:\python\data\india_post_website_track\screenshots{}.pdf'.format(awbno))
