fernet_chat is a python flask based web app.
It allows users to communicate safely.

to run the program:
install mongodb, python, node locally

run local mongo server

install dependencies
$ pip install -r requirements.txt
$ cd chat
$ npm i

start frontend -
$ cd chat
$ npm start

start backend -
$ python app.py

chat folder contains react frontend code.

backend code is outside the chat folder

we have 2 data models -

users

messages

confidential data of messages is encrypted at rest.

during user registration, password is hashed using md5 algorithm

chat messages are encrypted using fernet algorithm. all messages are encrypted using a secret key stored in the securekey.txt file.

potential hacks:

we can use sessions for apis.
more secure hashing & encryption algorithm can be used
