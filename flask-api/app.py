import os
from flask import Flask, request, jsonify
from firebase_Admin import credentials, firestore, initalize_app

app = Flask(__name___)

creds = credentials.Certificate('key.json')
default_app = initalize_app(creds)
fireDB = firestore.client()
todos = db.collect('todos')


# @app.route('/add', methods=['POST'])
# def add():
#     try:
#         id = request.json['id']
#         todos.document(id).set(request.json)
#         return jsonify({"success" : True}), 200
#     except Exception as exception:
#         return "An Error Occured: {}".format(exception)

@app.route('/get', methods=['GET'])
def get():
    try:
        todo_id = request.args.get('id')
        if id:
            todo = todos.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            todos_list = [doc.to_dict() for doc in todos.stream()]
            return jsonify(todos_list), 200
    except Exception as exception:
        return "An Error Occured: {}".format(exception)
