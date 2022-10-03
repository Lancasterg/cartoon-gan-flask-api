from flask import Flask
from flask_restful import reqparse, Api
from app_resources import Hayago

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(Hayago, Hayago.ENDPOINT)

if __name__ == '__main__':
    app.run(debug=True)
