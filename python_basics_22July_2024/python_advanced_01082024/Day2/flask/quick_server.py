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

if __name__ == '__main__':
    #http://localhost:5000
    app.run()
    #host, port, security - deployment topics 