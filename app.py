
import os
from flask import Flask, request
#from flask_ngrok import run_with_ngrok
app = Flask(__name__)
#app = Flask(__name__, static_url_path='')


print("test")


from routes import *

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
    app.run(debug=True)
    #app.run()
