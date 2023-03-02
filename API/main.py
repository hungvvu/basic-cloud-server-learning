from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# create the schema for the student
class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"
    
# db.create_all()

# argument parser for put
student_put_args = reqparse.RequestParser()
student_put_args.add_argument('name', type=str, help='Name not specified', required=True)
student_put_args.add_argument('age', type=str, help='Age not specified', required=True)

# argument parser for update
student_update_args = reqparse.RequestParser()
student_update_args.add_argument('name', type=str, help='Name not specified', required=False)
student_update_args.add_argument('age', type=str, help='Age not specified', required=False)


# def abort_if_non_existing_student(studentID):
#     if studentID not in students:
#         abort(404, message="Student ID not found")

# def abort_if_existing_student(studentID):
#     if studentID in students:
#         abort(404, message="Student ID already exist")

# fields for serialization
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age':fields.Integer
}

# test resource
class Student(Resource):
    # test get function that return a dictionary with "Hello World":"Hello"
    @marshal_with(resource_fields)
    def get(self, studentID):
        # query and return the data
        result = StudentModel.query.filter_by(id=studentID).first()
        if not result:
            abort(404, message="Student ID not found")
        return result
    
    @marshal_with(resource_fields)
    def put(self, studentID):
        args = student_put_args.parse_args()
        
        # check whether the student ID is taken or not
        result = StudentModel.query.filter_by(id=studentID).first()
        if result:
            abort(409, message='Student ID already exist.')

        # create a student object and add it to the session
        student = StudentModel(id=studentID, name=args['name'], age=args['age'])
        db.session.add(student)
        db.session.commit()
        return student, 201
    
    def patch(self, studentID):
        args = student_update_args.parse_args()

        # check whether the student ID exist or not
        result = StudentModel.query.filter_by(id=studentID).first()
        if not result:
            abort(404, message='Student ID not found')
        
        if args['name']:
            result.name = args['name']
        if args['age']:
            result.age = args['age']

        db.session.commit()
    
    # def delete(self, studentID):
    #     abort_if_non_existing_student(studentID)
    #     del students[studentID]
    
    # def post(self):
    #     return {'data':'Posted'}
 
api.add_resource(Student, "/student/<int:studentID>")

if __name__ == "__main__":
    app.run(debug=True)