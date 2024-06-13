import time
def timer(func):
    def wrapper(*args):
        start = time.time()
        result =func(*args)
        end = time.time()
        print(f"Time is = {end - start}")
        return result
    return wrapper

@timer
def function(n):
    time.sleep(n)

function(2)