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

# Bash message with the event created from the client
@socketio.on('event')
def handleEvent(json):
  print( '\nRecived event: ' + str(json) + '\n')
  socketio.emit( 'response', json, callback=messageRecived )

# Message when the client disconects from the server
@socketio.on('disconnect')
def handleDisconnet():
    print('\n A user disconnected')

if __name__ == '__main__':
  socketio.run(app, debug = True)
