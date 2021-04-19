def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        result = func(*args)
        return result
    return wrapper


@type_logger
def multiplication(x, y):
    return x * y


print(multiplication(5, 2))
