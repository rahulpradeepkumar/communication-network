from flask import Flask, request, jsonify
import db
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/users/all', methods=['GET'])
def getAllUsers():

    users = db.get_users()

    return jsonify({'success': True, 'users': db.parse_json(users)})


@app.route('/message/all', methods=['POST'])
def getMsg():
    payload = request.get_json()
    sender = payload['sender']
    receiver = payload['receiver']
    if not sender or not receiver:
        return jsonify({'success': True, 'msgs': []})

    msgs = db.get_msgs(sender, receiver)

    return jsonify({'success': True, 'msgs': db.parse_json(msgs)})


@app.route('/message', methods=['POST'])
def sendMsg():
    payload = request.get_json()
    sender = payload['sender']
    receiver = payload['receiver']
    value = payload['value']

    db.insert_msg(sender, receiver, value)

    return jsonify({'success': True})


@app.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    username = payload['username']
    password = payload['password']

    print(db.get_users())

    user = db.get_user(username, password)

    if user:
        return jsonify({'success': False, 'msg': 'user exists'})

    user = db.create_user(username, password)
    return jsonify({'success': True, 'user': db.parse_json(user)})


@app.route('/login', methods=['POST'])
def login():

    payload = request.get_json()
    username = payload['username']
    password = payload['password']

    user = db.get_user(username, password)

    if not user:
        return jsonify({'success': False, 'msg': 'user does not exist'})

    return jsonify({'success': True, 'user': db.parse_json(user)})


if __name__ == '__main__':
    app.run(debug=True)
