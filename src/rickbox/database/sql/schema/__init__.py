import os


def get_users_schema():
    with open(os.path.join(os.path.dirname(__file__), 'create_users.sql'), 'r') as f:
        return f.read()


def get_files_schema():
    with open(os.path.join(os.path.dirname(__file__), 'create_files.sql'), 'r') as f:
        return f.read()


def get_folders_schema():
    with open(os.path.join(os.path.dirname(__file__), 'create_folders.sql'), 'r') as f:
        return f.read()


def get_fks_schema():
    with open(os.path.join(os.path.dirname(__file__), 'create_fks.sql'), 'r') as f:
        return f.read()


def get_all_schemas():
    return {'users': get_users_schema(), 'files': get_files_schema(), 'folders': get_folders_schema()}
