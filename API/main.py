from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

students = {1234:{'name':'Hung', 'age':'21'}}
student_put_args = reqparse.RequestParser()
student_put_args.add_argument('name', type=str, help='Name not specified', required=True)
student_put_args.add_argument('age', type=str, help='Age not specified', required=True)

def abort_if_non_existing_student(studentID):
    if studentID not in students:
        abort(404, message="Student ID not found")

def abort_if_existing_student(studentID):
    if studentID in students:
        abort(404, message="Student ID already exist")

# test resource
class Student(Resource):
    # test get function that return a dictionary with "Hello World":"Hello"
    def get(self, studentID):
        abort_if_non_existing_student(studentID)
        return students[studentID]
    
    def put(self, studentID):
        abort_if_existing_student(studentID)
        args = student_put_args.parse_args()
        students[studentID] = args
        return args, 201
    
    def delete(self, studentID):
        abort_if_non_existing_student(studentID)
        del students[studentID]
    
    def post(self):
        return {'data':'Posted'}
 
api.add_resource(Student, "/student/<int:studentID>")

if __name__ == "__main__":
    app.run(debug=True)