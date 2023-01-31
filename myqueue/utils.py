def convertToList(function):
    def wrapper(*args, **kwargs):
        notlist = not isinstance(args[1], list)
        if notlist:
            l = list(args)
            l[1] = [l[1]]
            args = tuple(l)
        response = function(*args, **kwargs)
        if response is not None:
            if notlist:
                return response[0]
            return response
    return wrapper