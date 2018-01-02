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
  print( 'recived event: ' + str( json ) )
  socketio.emit( 'response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run(app, debug = True)
