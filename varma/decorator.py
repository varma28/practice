def modifier(func):
    """
    This function signifies the usage of decorators
    """
    def wraper(x):
        print("Function is in wrapper and value of x is: ",x)
        result = func()
        return result
    return wraper

@modifier
def foo():
    print("Foo doesn't have any arguments but it is modified to take one")


foo(1)
print(modifier.__doc__)
