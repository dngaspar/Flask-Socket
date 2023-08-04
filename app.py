from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


def ack():
    print("complete")

@socketio.on("messageFromExtension")
def handle_extension(data):
    print("messageFromExtension", data)
    emit("messageToExtension", data, callback=ack)

if __name__ == '__main__':
    socketio.run(app)