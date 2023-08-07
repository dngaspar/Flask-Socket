from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


def ack():
    print("complete")

@socketio.on("messageFromExtension")
def handle_extension(data):
    print("messageFromExtension", "data")
    emit("messageToExtension", {"abc" :"first load from flask"}, callback=ack)

@socketio.on("first")
def handle_exten(data):
    print("messageFromExtension", data)
    emit("create_anonaddy", {"name": "denis", "id": str(uuid.uuid4())})
    # emit("secondfd", {"abc" :"first load from flask"})

@socketio.on("send_anonaddy")
def recieve_anonaddy(data):
    print(data)

@socketio.on("backto")
def handle_backto(data):
    print("backto", data)

if __name__ == '__main__':
    socketio.run(app)