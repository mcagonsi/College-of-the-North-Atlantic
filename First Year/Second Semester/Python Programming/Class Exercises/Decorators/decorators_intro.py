# def f1():
#     print("Called F1")
#
# def f2(f):
#     f()
#
# f2(f1)

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Finished")

    return wrapper

@f1
def f(a):
    print(a)

@f1
def f3():
    print("Hi, I'm F3")

# print(f1(f))
# f1(f)()

# x = f1(f)
# x()

f("Let's dance")
