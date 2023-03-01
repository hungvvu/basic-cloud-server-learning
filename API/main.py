from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# test class
class Hello_World(Resource):
    # test get function that return a dictionary with "Hello World":"Hello"
    def get(self):
        return {"Hello World":"Hello"}

api.add_resource(Hello_World, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)