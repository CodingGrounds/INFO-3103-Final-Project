import os


def get_users_procs():
    with open(os.path.join(os.path.dirname(__file__), 'users.sql'), 'rb') as f:
        return f.read()


def get_files_procs():
    with open(os.path.join(os.path.dirname(__file__), 'files.sql'), 'rb') as f:
        return f.read()


def get_folders_procs():
    with open(os.path.join(os.path.dirname(__file__), 'folders.sql'), 'rb') as f:
        return f.read()


def get_meta_procs():
    with open(os.path.join(os.path.dirname(__file__), 'meta.sql'), 'rb') as f:
        return f.read()


def get_all_procs():
    return {'users': get_users_procs(), 'files': get_files_procs(), 'folders': get_folders_procs(), 'meta': get_meta_procs()}
