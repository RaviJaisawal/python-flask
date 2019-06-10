
from flask import  Flask





app = Flask(__name__)


@app.route('/')
def home():
    return "Hi Im Flask"

@app.route('/getName/<string:name>')
def get_name(name):
    return name



app.run(port=5000,debug=True)
