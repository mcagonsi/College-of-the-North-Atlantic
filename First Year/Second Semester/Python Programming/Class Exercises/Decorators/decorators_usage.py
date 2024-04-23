import time

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        func()
        print("Function took: ", time.time() - before, "seconds")

    return wrapper

@timer
def run():
    time.sleep(2)

run()

@timer
def say_hello():
    print("hello")

say_hello()