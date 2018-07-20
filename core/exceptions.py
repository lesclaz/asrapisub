class ApiError(Exception):
    pass


class AutenticationError(ApiError):
    pass


class ConnectionParametersError(ApiError):
    pass


class Error(object):
    pass
