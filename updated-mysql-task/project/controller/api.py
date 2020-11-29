from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import json
import controller.controller as controller

user_config = open("config/user_config.json")
config = json.load(user_config)

ADDUSER_ENDPOINT = config.get("adduser_endpoint")
SHOWUSER_ENDPOINT = config.get("showuser_endpoint")
DELETEUSER_ENDPOINT = config.get("deleteuser_endpoint")


app = Flask(__name__)
api = Api(app)

class AddUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'id',
            type=int,
            required=True,
            help='ID required',
            location='args')
        self.parser.add_argument(
            'name',
            type=str,
            required=True,
            default=0,
            location='args')
        self.parser.add_argument(
            'age',
            type=int,
            required=True,
            default=0,
            location='args')
        self.parser.add_argument(
            'department',
            type=str,
            required=True,
            default=0,
            location='args')
        self.parser.add_argument(
            'subject',
            type=str,
            required=True,
            default=0,
            location='args')

    def post(self):
        """ POST request."""
        args = self.parser.parse_args()
        id = args.get('id')
        name = args.get('name')
        age = args.get('age')
        department = args.get('department')
        subject = args.get('subject')

        message = controller.adduser(id, name, age, department, subject)
        response = jsonify(message)
        return response

class ShowUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()


    def get(self):
        """ GET request."""
        message = controller.showuser()
        response = jsonify(message)
        return response

class DeleteUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'id',
            type=int,
            required=True,
            help='ID required',
            location='args')

    def delete(self):
        args = self.parser.parse_args()
        id = args.get('id')

        message = controller.deleteuser(id)
        response = jsonify(message)
        return response


api.add_resource(AddUser, ADDUSER_ENDPOINT)
api.add_resource(ShowUser, SHOWUSER_ENDPOINT)
api.add_resource(DeleteUser, DELETEUSER_ENDPOINT)


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    main()
