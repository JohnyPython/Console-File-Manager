

def decorator_fun(func):
    def inner():
        print("* " * 11)
        result = func()
        return result
    return inner
