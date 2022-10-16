from flask import Flask
from flask_restful import reqparse, Api
from app_resources import PaprikaEndpoint, ShinkaiEndpoint

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(ShinkaiEndpoint, ShinkaiEndpoint.ENDPOINT)
api.add_resource(PaprikaEndpoint, PaprikaEndpoint.ENDPOINT)


if __name__ == '__main__':
    app.run(debug=True)
