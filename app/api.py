from flask_restful import Resource
from flask import Response, jsonify

from app.data import CV_DATA

class Personal(Resource):
    def get(self) -> Response:
        return jsonify(CV_DATA["personal"])

class Experience(Resource):
    def get(self) -> Response:
        return jsonify(CV_DATA["experience"])

class Education(Resource):
    def get(self) -> Response:
        return jsonify(CV_DATA["education"])
