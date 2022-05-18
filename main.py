#Flask
#You cannot run this in jupyter, instead you have to convert it into a script file and launch it from the terminal
from flask import Flask
import uuid

app = Flask(__name__)
# we need the id for trying out the AWS ELB
my_id = str(uuid.uuid4())


@app.route("/hi")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "Bye"

#We start the server from host='0.0.0.0' in order to make it reachable from the outside.
#You have to replace the ip in your browser by your own ip server.
# we run the app in debug mode

app.run(debug=True,port=5000,host=‘0.0.0.0’    
