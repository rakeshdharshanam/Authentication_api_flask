from flask import Flask,request
from functools import wraps
 
app = Flask(__name__)
 
def reqauthenticate(orgfunc):
    @wraps(orgfunc)
    def authenticate(*args, **kwargs):
        print("authenticated")
        print(args)
        return orgfunc(*args, **kwargs)
    return authenticate

@app.route('/',methods = ["GET"])
@reqauthenticate
def hello_world():
    print(request.headers["name"])
    return "from hello_world" 

@app.route('/test',methods=["GET"])
@reqauthenticate
def test():
    return "from test"
 
# main driver function
if __name__ == '__main__':
    app.run(debug=True)
