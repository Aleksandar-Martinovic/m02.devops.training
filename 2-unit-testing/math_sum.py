def add(a, b):
    #raise NotImplementedError("Implement this function using TDD")
    return a+b


def subtract(a, b):
    #raise NotImplementedError("Implement this function using TDD")
    return a-b


def multiply(a, b):
    #raise NotImplementedError("Implement this function using TDD")
    return a*b

def divide(a, b):
    #raise NotImplementedError("Implement this function using TDD")
    if b != 0:
        return a/b
    else:
        raise ValueError("B can not be 0!")