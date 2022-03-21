
def main():
    
    # data is a variable of type Dictionary 
    # According to w3schools.com "Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates."
    data = {
        'msg1': 'Hola Mundo!',
        'msg2': 'My name is John',
        'age': 20,
        'a':1,
        'b':2,
        'c':3,
        'x':4,
        'y':4,
        'z':4
    }

    # for loops act mainly like an iterator method, this one will print every key in our dictionary with two lines of code
    for x in data:
        print(x)

    # this for loop will print every value in our dictionary with two lines of code
    for x in data:
        print(data[x])
    # else statement is optional and specifies some code to run when our loop finishes
    else:
        print('All done!')


if __name__ == '__main__':
    main()
