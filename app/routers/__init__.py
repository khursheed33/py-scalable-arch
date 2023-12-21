# app/__init__.py
import sys
from flask import Flask
from app.routers import hello_route
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("You said port is : {} ".format(port))

# Register the HelloWorld resource
api.add_resource(hello_route.HelloWorld, '/fo')
