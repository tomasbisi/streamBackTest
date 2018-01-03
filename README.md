This Project is a network messaging application using Flask and SocketIO.

## How to install

### Dependencies
```
Python: 2.7.10
Flask: 0.12.2
Flask-socketio
Virtualenv
Jquery: 3.2.1
```

On a new Terminal window clone the repository:  
```
git clone https://github.com/tomasbisi/streamBackTest.git
cd streamBackTest
```

This application is running inside a virtual environment using python's virtualvenv. This will allow you to install packages inside the environment without affecting the computer's secutiry integrity. If you don't have it installed run :
```
sudo pip install virtualenv
```

Then:
```
virtualenv venv
virtualenv --no-site-packages venv
```

Once the virtualenv is installed, setted up and the packages have been added, run this command to start running it:
```
source venv/bin/activate
```

Install all the dependencies that the project requires to import in order to work:

```
pip install -r requirements.txt
```

Finally you are ready to run the project:
```
python messageApp.py
```

It's running on port 5000. Copy this url on the browser:
```
http://127.0.0.1:5000

```


To have a multi-client chat open a new tab and copy the same url. 

