# functions can be defined with multiple arguments also called args
def random_function(name, age):
    print('Hi my name is ' + name + ' and I am ' + str(age))

random_function('John Doe', 20)

# functions can be also be defined with arbitrary arguments meaning you don't
# know the amount of arguments expected
def other_function(*names):
    print('I have three brothers: ' + names[0])

other_function('Ben', 'Harry', 'Joe')

# functions can be defined with a default argument meaning if no argument is
# in the function call a default value will be assigned
def another_function(favFood = 'steak'):
    print('my favorite food is' + favFood)

another_function('Chicken')
another_function()
