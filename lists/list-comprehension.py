def main():
    list = ['pitbull', 'pug', 'great dane']
    mylist = [x for x in list if len(x) > 3]  # ['pitbull', 'great dane']
    myupperlist = [x.upper() for x in list]   # ['PITBULL', 'PUG', 'GREAT DANE']

if __name__ == '__main__':
    main()