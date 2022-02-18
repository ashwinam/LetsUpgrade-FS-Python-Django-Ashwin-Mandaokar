from flask import Flask
from flask_restful import Resource, Api


app = Flask (__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'World from ashwin'}


class Greetme(Resource):
    def get(self):
        return {'hello':'World'}


api.add_resource(HelloWorld,'/')
api.add_resource(Greetme,'/greet')

if __name__=='__main__':
    app.run(debug=True)


