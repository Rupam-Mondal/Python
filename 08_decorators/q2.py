def debug(func):
    def wrapper(*args , **kwargs):
        print(func.__name__)
        print(args)
        return func(*args , **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Rupam", greeting="Hello ")