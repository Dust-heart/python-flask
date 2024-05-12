from flask_restful import Resource


class ResourceAdd(Resource):
    @staticmethod
    def get():
        return "resource_add"
