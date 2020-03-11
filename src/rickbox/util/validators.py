def validate_id(id_value):
    if id_value is None:
        raise ValueError('`id_value` cannot be None.')

    # Lazy assertion that the id is actually an integer
    id_value = int(id_value)

    if id_value < 0:
        raise ValueError('`id_value` must be non-negative.')

    return id_value
