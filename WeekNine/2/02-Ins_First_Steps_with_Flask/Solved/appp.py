# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"
#routes are the URL that allows us to access the data

# 4. Define what to do when a user goes to the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "HI!! Welcome to my 'About' page!"

#this statement puts it into DEBUG MODE - that means if you make 
#updates it will catch the changes to execute. 
if __name__ == "__main__":
    app.run(debug=True)
