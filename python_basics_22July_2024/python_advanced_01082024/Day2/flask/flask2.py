#################quick_server.py
#Execute by
#python quick_server.py
from flask import Flask

#https://flask.palletsprojects.com/en/2.0.x/api/
app = Flask(__name__)


#URL end => function , by defualt, Flask uses 200 OK, text/html
#flask uses all methods - GET,....

@app.route("/", methods=['GET'])  # http://localhost:5000/
def home():
    return  """
    <html>
    <head><title>MyWebserevr</title>
    <style>
    .some {
        color: red;
    }
    </style></head>
    <body>
    <h1 id="some" class="some">Hello there!</h1>
    <h1 id="some2">hello again!!</h1>
    </body>
    </html>
    """

"""
GET Params 
    URL params 
        http://localhost:5000/helloj?name=das&format=json
        Use request.args 
    PATH params 
        http://localhost:5000/helloj/das/json 

POST params 
    body params, set Content-Type = application/json 
    sned json string in body 
        request.json() to parse 

"""
"""
helloj  takes and return age from db 
"""
from flask import request , jsonify

@app.route("/helloj", methods=["GET"]) #http://localhost:5000/helloj?name=das&format=json
@app.route("/helloj/<string:name>/<string:format>", methods=['GET'])#http://localhost:5000/helloj/das/json
@app.route("/helloj/<string:name>", methods=['GET']) #http://localhost:5000/helloj/das
def helloj(name="abc", format="json"): #PATH params , flask sends value of name and format here
    db = [dict(name="das",age=40), dict(name="abc", age=35)]
    #Parse URL params
    fname = request.args.get("name", name)  # requst.args is dict , get(key, default_value)
    fformat = request.args.get("format", format)
    age = None
    for e in db:
        if e['name'].lower() == fname.lower():
            age = e['age']
    #Response
    if age is not None:
        #success
        obj = dict(name=fname, age=age)
        status_code = 200
    else:
        #failure
        obj = dict(name=fname, details="Not found")
        status_code = 500
    resp = jsonify(obj)  # sets COntent-Type as json and converts to json string
    resp.status_code = status_code
    return resp

if __name__ == '__main__':
    #http://localhost:5000
    #run(host=None, port=None, debug=None, load_dotenv=True, **option
    app.run()
    #host, port, security - deployment topics