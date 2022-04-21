def main():
    mylist = ['b', 'c', 'a']
    numberlist = [2, 3, 1]
    
    mylist.sort()  # ['a', 'b', 'c']
    mylist.sort(reverse = True)  # ['c', 'b', 'a']
    numberlist.sort()  # [1, 2, 3]
    numberlist.sort(reverse=True)  # [3, 2, 1]



if __name__ == '__main__':
    main()
