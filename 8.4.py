def val_checker(is_valid):
    def wrapper(func):
        def valid_exe(*args):
            if is_valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'Wrong value: {args}')
        return valid_exe()
    return wrapper()


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(4)
