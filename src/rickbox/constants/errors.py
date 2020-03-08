import json
from flask import Response

ERROR_400 = Response(json.dumps({'message': 'Bad request'}), 400)
ERROR_401 = Response(json.dumps({'message': 'Authentication Required: Login required to perform action'}), 401)
ERROR_403 = Response(json.dumps({'message': 'Permission Denied. Unable to perform action'}), 403)
ERROR_404 = Response(json.dumps({'message': 'Resource not found'}), 404)
