mylist = [1, 2, 3]
while mylist:
    foo = mylist.pop()
    if foo == 3:
        mylist.extend([69, 42])
    if foo == 42:
        print("bar")
