def main():

    # Lists can contain multiple data types
    multiDataList = ['name', 1, True]
    
    # This for loop will print each item in the list
    for x in multiDataList:
        print(x)

    # Each items in the list can be accessed by pointing to its index. The index of a List starts at 0
    print(multiDataList[0])
    print(multiDataList[1])

    # The len function can be used to determine how many items are in the list
    print(len(multiDataList))


if __name__ == '__main__':
    main()
