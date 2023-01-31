def convertToList(function):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], list):
            l = list(args)
            l[1] = [l[1]]
            args = tuple(l)
        response = function(*args, **kwargs)
        if response is not None:
            if not isinstance(args[1], list):
                return response[0]
            return response
    return wrapper