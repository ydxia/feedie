def set_routes(config):

    config.add_route(
        name='home',
        pattern='/',
        request_method='GET',
    )
    config.add_route(
        name='profile',
        pattern='/profile/{user_handle}',
        request_method='GET',
    )