from flask import session

from database.models.file import File
from util.responses import ERROR_401, json_response, ERROR_400, ERROR_403, ERROR_404


# There is likely a better file structuring scheme to use here.
def conceal_error_message(func):
    """
    Wraps around endpoint logic to catch and log any errors,
    while returning a nondescript error to the end user.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Logging stuff here?
            print(e)
            return json_response({"message": "error"}, 500)

    return wrapper


def require_session(func):
    """
    Wraps around anything that requires an active user session,
    returning a 401 to the end user if they are not logged in.
    """

    def wrapper(*args, **kwargs):
        if 'username' not in session or 'user_id' not in session:
            return ERROR_401
        return func(*args, **kwargs)

    return wrapper


def verify_file_access_authorization(func):
    """
    Wraps around file interaction endpoints and provides them a
    File object iff the user has authorization to perform operations
    on the specified file.

    Retrieves identifiers from the wrapped function's **kwargs.
    """

    def wrapper(*args, **kwargs):
        kwdict = dict(**kwargs)

        user_identifier = kwdict['user_identifier']
        file_id = kwdict['file_id']

        if user_identifier in [None, '']:
            return ERROR_400

        if file_id in [None, '']:
            return ERROR_400

        if user_identifier not in [session.get('user_id'), session.get('username')]:
            return ERROR_403

        try:
            file = File.get_by_id(file_id)
        except LookupError:
            return ERROR_404

        if file is None:
            return ERROR_404

        if file.owner_id != session.get('user_id'):
            return ERROR_403

        return func(*args, authorized_file=file, **kwargs)

    return wrapper
