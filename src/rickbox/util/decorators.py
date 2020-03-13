from flask import Response, session
from util.errors import ERROR_401


# There is likely a better file structuring scheme to use here.
def conceal_error_message(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Logging stuff here?
            print(e)
            return Response('{"message": "error"}', status=500, mimetype='application/json')
    return wrapper


def require_session(func):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return ERROR_401
        return func(*args, **kwargs)
    return wrapper
