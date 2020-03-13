import json

from flask import Response


def json_response(body, code):
    return Response(json.dumps(body), code, mimetype='application/json')


def resource_created(id):
    return json_response({'resourceId': id}, 201)


def resource_list(resources):
    return json_response({'items': resources}, 200)


OK_200 = json_response({'message': 'OK'}, 200)
OK_204 = json_response({}, 204)
ERROR_400 = json_response({'message': 'Bad request'}, 400)
ERROR_401 = json_response({'message': 'Authentication Required: Login required to perform action'}, 401)
ERROR_403 = json_response({'message': 'Permission Denied. Unable to perform action'}, 403)
ERROR_404 = json_response({'message': 'Resource not found'}, 404)
