from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = {'1234':{'name':'Hung', 'age':'21'}}

# test resource
class Hello_World(Resource):
    # test get function that return a dictionary with "Hello World":"Hello"
    def get(self, id):
        return students[id]
    
    def post(self):
        return {'data':'Posted'}

api.add_resource(Hello_World, "/helloworld/<string:id>")

if __name__ == "__main__":
    app.run(debug=True)