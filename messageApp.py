from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET KEY'] = 'testasd123'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('./index.html')

def messageRecived():
  print('message delivered')

@socketio.on('event')
def handleEvent(json):
  print( 'Recived event: ' + str(json) + '\n')
  socketio.emit( 'response', json, callback=messageRecived )

@socketio.on('disconnect')
def handleDisconnet():
    print('Client disconnected\n')

if __name__ == '__main__':
  socketio.run(app, debug = True)
