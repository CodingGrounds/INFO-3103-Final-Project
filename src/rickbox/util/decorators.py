from flask import session

from util.responses import ERROR_401, json_response


# There is likely a better file structuring scheme to use here.
def conceal_error_message(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Logging stuff here?
            print(e)
            return json_response({"message": "error"}, 500)
    return wrapper


def require_session(func):
    def wrapper(*args, **kwargs):
        if 'username' not in session or 'user_id' not in session:
            return ERROR_401
        return func(*args, **kwargs)
    return wrapper
