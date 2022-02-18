from flask import Flask,request
from flask.json import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if(functionName=='add' or functionName=='subtract' or functionName=='multiply'):
        if('x' not in postedData or 'y' not in postedData):
            return 301 # missing parameter Error
        else:
            return 200 #all Good

    elif (functionName=='division'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif int(postedData['y']==0):
            return 302
        else:
            return 200
    
class Add(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,'add')

        if (status_code!=200):
            retJson= {
                'message':'An Error Happened',
                'status_code':status_code
            }
            return jsonify(retJson)
        else:
            x=postedData['x']
            y=postedData['y']
            x=int(x)
            y=int(y)
            ret=x+y

            retMap = {
                'message':ret,
                'status_code':status_code
            }

            return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,'subtract')

        if(status_code!=200):
            retJson= {
                'message':'An Error Happened',
                'status_code':status_code
            }
            return jsonify(retJson)
        
        else:
            x=postedData['x']
            y=postedData['y']
            x=int(x)
            y=int(y)
            ret=x-y

            retMap={
                'message':ret,
                'status_code':status_code
            }
            return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,'multiply')

        if(status_code!=200):
            retJson={
                'message':'An Error Happened',
                'status_code':status_code
            }
            return jsonify(retJson)
        else:
            x=postedData['x']
            y=postedData['y']
            x=int(x)
            y=int(y)
            ret=x*y

            retMap={
                'message':ret,
                'status_code':status_code
            }

            return jsonify(retMap)


class Division(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,'division')

        if(status_code!=200):
            retJson={
                'message':'An error Happened',
                'status_code':status_code
            }
            return jsonify(retJson)

        else:
            x=postedData['x']
            y=postedData['y']
            x=int(x)
            y=int(y)

            ret=x/y

            retMap={
                'message':ret,
                'status_code':status_code
            }
            return jsonify(retMap)


# Add Resources 
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Division, '/division')


@app.route('/')
def Hello():
    return 'hello'


if __name__=='__main__':
    app.run(debug=True)


