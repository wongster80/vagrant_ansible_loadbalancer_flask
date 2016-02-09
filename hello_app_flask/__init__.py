from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#@app.route('/imgs')
#def imgs():
#    return app.send_static_file('welcome.jpg')
