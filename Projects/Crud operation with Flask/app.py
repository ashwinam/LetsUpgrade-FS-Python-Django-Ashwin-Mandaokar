# from types import MethodDescriptorType
from flask import Flask, request, render_template
import json
# from flask.wrappers import
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route('/greet')
def greet():
    return '<p>Hello,Everybody,Enjoy the Coding!</p>'

# CRUD= Creat,Read,Update,Delete.

# Get method for reading all data from DB/Json/Cloud/3rd party API


@app.route('/get', methods=['GET', 'POST'])
def get_data():
    print(f'Request Name:{request.method}')
    with open("total_log.json", 'r')as logs:
        logData = json.load(logs)
    # return {"name":logData["total_log"]}
    return render_template('index.html', data=logData["total_log"])
    # return '<h1>Hello, World!</h1>'

# Post Request for sending new entries


@app.route("/post", methods=['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        data = request.form['name']
        print(data)
        name, price = data.split()
        with open('total_log.json', 'r')as logs:
            logData = json.load(logs)
        logData['total_log'][name] = price
        with open('total_log.json', 'w')as logs:
            logs.write(json.dumps(logData))
        return (f'Successfully Saves: {name}')
    else:
        return render_template('post.html')

# Update Request make changes in existing items
@app.route("/update", methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        data = request.form['update']
        name, price = data.split()

        with open('total_log.json', 'r')as logs:
            logData = json.load(logs)

        findMethod = logData['total_log'].get(name, "NOT FOUND")
        if findMethod == "NOT FOUND":
            return ("Update Error : Product Not Found")
        else:
            logData['total_log'][name] = price
            with open("total_log.json", 'w')as logs:
                logs.write(json.dumps(logData))
            return ('Updated Successfully')
    else:
        return render_template('update.html')

# delete request delete an item from the list
# @app.route("/delete",methods=['GET','POST'])
# def delete_data():
#     if request.method=='POST':
#         data=request.form['delete']
#         name,price=data.split()

#         with open('total_log.json','r')as logs:
#             logData=json.load(logs)

#         findMethod=logData['total_log'].get(name,"NOT FOUND")
#         if findMethod=="NOT FOUND":
#             return ("Update Error : Product Not Found")
#         else:
#             logData['total_log'][name]=price
#             with open("total_log.json",'w')as logs:
#                 logs.write(json.remove(logData))
#             return ('Deleted  Successfully')
#     else:
#         return render_template('delete.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
