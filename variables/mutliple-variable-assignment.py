
def main():
    # This is a comment, comments are used to explain code  and also make code easier to understand

    # msg1, msg2, and age are all variables, variables can be used as a location to store data
    msg1 = 'Hola Mundo!'  # msg1 is of type str meaning string
    msg2 = 'My name is John'  # msg2 is of type str meaning string
    age = 20  # age is of type int meaning integer

    # multiple assignment can be used to reduce the amount of code when assigning variable data
    a, b, c = 1, 2, 3
    # multiple assignment can be used to assign one value to multiple variables
    x = y = z = 4

    # prints msg1 and msg2 variables as a single string of data to command line using comma separation of values
    print(msg1, msg2)
    # prints msg1 and msg2 variables as a single string of data to command line using + operator
    print(msg1 + msg2)
    # due to age data being of type int we can add an int of 10 to the print statement for a result of 30 in the command line
    print(age + 10)
    # Note data with different types can't be concatenated with the + operator and printed for example
    # print(age + msg1)
    # This print statement above would throw an error but you can use comma separation to concatenate values of different types
    print(age, msg1)

    print(a)  # prints a value of 1
    print(b)  # prints a value of 2
    print(c)  # prints a value of 3
    print(x)  # prints a value of 4
    print(y)  # prints a value of 4
    print(z)  # prints a value of 4


if __name__ == '__main__':
    main()
