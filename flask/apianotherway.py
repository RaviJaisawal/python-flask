from flask import Flask,request,jsonify
from flask_restful import  Resource, Api



app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self):
        user = self.getUserDataFormDB()
        return "Data"

    def getUserDataFormDB(self):
        pass

    def post(self):
        return "Data"

    def put(self):
        return "Data"

api.add_resource(Student,'/')

app.run(port=5000)



