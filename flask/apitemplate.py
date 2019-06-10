
from flask import  Flask , render_template, request , jsonify



employee =[]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    # if request.method == 'GET' :
    #     return render_template('index.html')

    # if request.method == 'POST' :
    #     print(request.form)
    #     data = {
    #         "name" : request.form['name'],
    #         "age" : request.form['age'],
    #         "salary" : request.form['salary'],
    #         "designation" : request.form['designation']
    #     }
    #     employee.append(data)
    #     return jsonify(employee),200

    return jsonify(employee)

@app.route('/', methods=['POST'])
def insert_employee():
    data = request.get_json()
    print(data)
    if data is not None:
        employee.append(data)
        return jsonify(employee)
    return "No data"

@app.route('/', methods=['PUT'])
def update_employee():
    data = request.get_json()
    print(data)
    if data is not None:
        for emp in employee:
            if emp["id"] == data["id"]:
                emp["age"] = data["age"]
                emp["designation"] = data["designation"]
                emp["name"] = data["name"]
                emp["salary"] = data["salary"]
            return jsonify(employee)
    return "No data"


@app.route('/', methods=['DELETE'])
def delete_employee():
    data = request.get_json()
    print(data)
    if data is not None:
        for emp in employee :
            if emp["id"]  ==  data["id"]:
                employee.remove(emp)
            return jsonify(employee)
    return "No data"

@app.route('/getName/<string:name>')
def get_name(name):
    return render_template('index.html',name=name)



app.run(port=5000,debug=True)
