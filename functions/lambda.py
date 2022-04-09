# lambdas are anonymous functions
x = lambda a, b : (a + b) * 2
print(x(5, 5)) # printed result will be 20

# this is an example of a lambda function inside a regular function
def addfunction(x):
    return lambda a : a + x


plusone = addfunction(1)
print(plusone(2))  # printed result will be 3
