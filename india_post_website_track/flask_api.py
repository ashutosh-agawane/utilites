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

destination = str(input("Enter the Destination : "))
number_of_item = str(input("Number of Item : "))

# li = []

# li.append(destination)

print("your going on holiday to {},and need to pack {} items".format(
    destination, number_of_item))
x = list(map(str, input("Enter Items to be packed : ").split()))
# print("list of items : ", x)

# print("{} it is there in the list".format(i) for i in x)

if not x:
    print("it is not in the packing list")
    add = str(input("Add in the list: "))
    x.append(add)
for i in x:
    if i == i:
        print("{} it is there in the list".format(i))
    # elif not x:
    # else:
    #     print("no one is added")
