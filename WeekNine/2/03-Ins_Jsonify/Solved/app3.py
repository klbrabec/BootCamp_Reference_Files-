from flask import Flask, jsonify

app = Flask(__name__)

hello_list = ["Hello", "World!"]
hello_dict = {"Hello": "World!"}

@app.route("/")
def home():
    return "Hi"

@app.route("/normal")
def normal():
    return str(hello_list)

@app.route("/jsonified")
def jsonified_list():
    return jsonify(hello_list)

@app.route("/dict")
def dictionary():
    return hello_dict

if __name__ == "__main__":
    app.run(debug=True)

#you cannot have multiple routes with the same name
#all names must be unique. 
#both the name of the route and the associated functions
#have to have unique names 

#if you get errors, the browser window will show you what
#the error is, which you can use to determine what needs
#to be corrected.

#recommended to write one route at a time. 
