class User:
    def __init__(self, username, root_folder_id, login_name, display_name=None):

    @staticmethod
    def get_by_id(user_id):
        if user_id is None:
            raise ValueError('`user_id` is a required parameter.')
        user =
