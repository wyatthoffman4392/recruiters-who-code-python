def main():
    cars = ['Honda', 'Toyota', 'Nissan']
    
    # for loops are used to iterate over sequences
    
    # this loop will run 3 times printing one of the strings from the cars list each time
    for x in cars:
        print(x)
    
    # this loop will run 5 times printing each letter of the word Honda each time
    for x in cars[0]:
        print(x)

    # this loop will run 13 times printing the number one, incrementing x by two then printing
    #  again until reaching 26 which will not be printed
    for x in range(1, 26, 2):
        print(x)
    else:
        print('That is all of the odd numbers 1 - 25')


if __name__ == '__main__':
    main()
