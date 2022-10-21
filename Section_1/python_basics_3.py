#Functions

def square_it(x):
    return x * x


def do_something(f, x):
    return f(x)


print(square_it(5))
print(do_something(square_it, 3))

print(do_something(lambda x: x * x * x, 7))

