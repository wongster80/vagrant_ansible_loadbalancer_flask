from flask import Flask, render_template, request
from time import gmtime, strftime
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    ip = request.remote_addr
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return "Hello from FLASK. My Hostname is: %s \n Your IP address is: %s \n The request timestamp is: %s" % (socket.gethostname(), ip, timestamp)

@app.route('/imgs')
def imgs():
    return app.send_static_file('welcome.jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

