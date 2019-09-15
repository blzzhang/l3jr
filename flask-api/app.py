import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

creds = credentials.Certificate('key.json')
default_app = initialize_app(creds)
fireDB = firestore.client()
places = fireDB.collection('places')


# @app.route('/add', methods=['POST'])
# def add():
#     try:
#         id = request.json['id']
#         todos.document(id).set(request.json)
#         return jsonify({"success" : True}), 200
#     except Exception as exception:
#         return "An Error Occured: {}".format(exception)

@app.route('/')
def hello():
    return "Landing Page"

@app.route('/get', methods=['GET'])
def get():
    try:
        id = request.args.get('id')
        coords = id.split("-")
        x = coords[0]
        y = coords[1]
        all_places = [doc.to_dict() for doc in places.stream()]
        return jsonify(all_places)
        # if id:
        #     todo = todos.document(todo_id).get()
        #     return jsonify(todo.to_dict()), 200
        # else:
        #     todos_list = [doc.to_dict() for doc in todos.stream()]
        #     return jsonify(todos_list), 200
    except Exception as exception:
        return "An Error Occured: {}".format(exception)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)