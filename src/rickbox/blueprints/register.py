from blueprints.users import users_bp


def register_all_blueprints(app_instance):
    app_instance.register_blueprint(users_bp)


