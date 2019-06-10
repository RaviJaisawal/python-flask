
from flask import  Flask , render_template, request ,jsonify


app = Flask(__name__)

employee = [{
    "id":1,
    "name":"ravi",
    "age": 26
}]

@app.route('/Employee',methods=['GET'])
def getEmployee():
    return jsonify(employee)




app.run(port=5000,debug=True)
