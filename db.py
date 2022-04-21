import json
import hashlib
import encrypter
from pymongo import MongoClient
from bson import json_util

client = MongoClient('mongodb://localhost:27017/')
db = client.fernet_chat


def insert_msg(sender, receiver, value):
    value = encrypter.encrypt(value)
    db.messages.insert_one(
        {'sender': sender, 'receiver': receiver, 'value': value})


def get_msgs(sender, receiver):
    arr = [sender, receiver]
    messages = []
    res = db.messages.find(
        {'sender': {'$in': arr}, 'receiver': {'$in': arr}},  {'_id': 0})
    for message in res:
        message['value'] = encrypter.decrypt(message['value'])
        messages.append(message)

    return messages


def get_user(username, password):
    password = hashlib.md5(password.encode()).hexdigest()
    user = db.users.find_one(
        {'username': username, 'password': password}, {'password': 0})
    return user


def get_user_by_id(id):
    user = db.users.find_one({'_id': id},  {'password': 0})
    return user


def create_user(username, password):
    password = hashlib.md5(password.encode()).hexdigest()
    user = db.users.insert_one({'username': username, 'password': password})
    return get_user_by_id(user.inserted_id)


def get_users():
    users = [user for user in db.users.find({}, {'_id': 0, 'password': 0})]
    return users


def parse_json(data):
    return json.loads(json_util.dumps(data))
