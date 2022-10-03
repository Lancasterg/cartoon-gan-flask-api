from importlib.resources import Resource
import parser
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('task')


class Hayago(Resource):

    ENDPOINT = "/v1/hayago/<image>"

    def get(self, todo_id):
        return "Nothing here yet"

    def delete(self, todo_id):
        return "Nothing here yet"

    def put(self, todo_id):
        return "Nothing here yet"
