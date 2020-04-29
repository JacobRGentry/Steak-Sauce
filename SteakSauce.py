from os import system
def cls():
    system('cls')

#put the text file into a dictionary to make editing easier
todo = {}
list = open('steaksauce.txt', 'r')
for x in list:
    line = x
    todo[line[1:2]] = line[4:]
list.close()
#Program loop
running = True
while running:
    cls()
    print("Welcome to Steak Sauce (v1.0), your daily to-do list organizer.")
    print("""
        [1] Make a new to-do list
        [2] Add to to-do list
        [3] Read to-do list
        [4] Mark completed to-do list item
        [5] Read about Steak Sauce
        [6] Exit
    """)
    selection = input("What would you like to do? ")
    #Make a new to-do list
    if selection == "1":
        ok = input("Warning! This will overwrite any current to-do list. Do you wish to continue? [y/n] ")
        if ok == "y":
            cls()
            list = open('steaksauce.txt', 'w')
            todo = {}
            a_group = []
            a2_group = {}
            b_group = []
            b2_group = {}
            c_group = []
            c2_group = {}
            a = 1
            adding = True
            print("Add all of your to-do list items and when you're finished hit enter.")
            #Adding stuff to the do-list loop (It's actually coded kinda backwards (on purpose) so what happens in the else statement is supposed to before the user types done
            while adding:
                addition = input("Enter a new to do list item: ")
                if addition == "":
                    cls()
                    print("Now we need to prioritize our to-do list. You need to go through and select which items get an A, B, or C and then which items get 1, 2, 3, etc.")
                    for x, y in todo.items():
                        print("[" + x + "] " + y)
                    #Getting a_group
                    while True:
                        placement = input("Which item(s) belong in the A group? ")
                        if placement == "":
                            print("", end='\r')
                            break
                        elif int(placement) <= len(todo):
                            a_group.append(todo[placement])
                        else:
                            print("Sorry, that's not a valid to-do list item")
                    #Getting b_group
                    while True:
                        placement = input("Which item(s) belong in the B group? ")
                        if placement == "":
                            print("", end='\r')
                            break
                        elif int(placement) <= len(todo):
                            b_group.append(todo[placement])
                        else:
                            print("Sorry, that's not a valid to-do list item")
                    #Getting c_group
                    while True:
                        placement = input("Which item(s) belong in the C group? ")
                        if placement == "":
                            print("", end='\r')
                            break
                        elif int(placement) <= len(todo):
                            c_group.append(todo[placement])
                        else:
                            print("Sorry, that's not a valid to-do list item")
                    todo.clear()
                    cls()
                    print("Now we need to go through and give our A's, B's, and C's numbers.")
                    #Getting a2_group
                    print("\nGroup A:")
                    a = 0
                    for x in a_group:
                        print(x)
                    print()
                    for x in a_group:
                        print(x)
                        placement = input("What number is this item? ")
                        if placement == "":
                            break
                        else:
                            a2_group["A" + placement] = a_group[a]
                        a += 1
                    #Getting b2_group
                    print("\nGroup B:")
                    a = 0
                    for x in b_group:
                        print(x)
                    print()
                    for x in b_group:
                        print(x)
                        placement = input("What number is this item? ")
                        if placement == "":
                            break
                        else:
                            b2_group["B" + placement] = b_group[a]
                        a += 1
                    #Getting c2_group
                    print("\nGroup C:")
                    a = 0
                    for x in c_group:
                        print(x)
                    print()
                    for x in c_group:
                        print(x)
                        placement = input("What number is this item? ")
                        if placement == "":
                            break
                        else:
                            c2_group["C" + placement] = c_group[a]
                        a += 1
                    #Putting it all together
                    for x, y in a2_group.items():
                        todo[x] = y
                    for x, y in b2_group.items():
                        todo[x] = y
                    for x, y in c2_group.items():
                        todo[x] = y
                    for i in sorted(todo):
                        todo[i] = todo[i]
                    for x, y in todo.items():
                        lines = x + ". " + y + "\n"
                        list.writelines(lines)
                    list.close()
                    break
                else:
                    addition == addition + "\n" 
                    todo[str(a)] = addition
                    a += 1
                    #print(todo) For testing purposes
        if ok == "n":
            continue
    #Add to to-do list
    elif selection == "2":
        cls()
        list = open('steaksauce.txt', 'w')
        for x, y in todo.items():
            print("[" + x + "] " + y + "\n")
        addvalue = input("What would you like to add? ")
        addkey = input("Where is this item in importance? [A1, B1, etc.] ")
        todo[addkey] = addvalue
        for x, y in todo.items():
            lines = x + ". " + y + "\n"
            list.writelines(lines)
        list.close()
    #Read to-do list
    elif selection == "3":
        cls()
        list = open('steaksauce.txt', 'r')
        print()
        print(list.read())
        input()
        list.close()
    #Mark completed to-do list item
    elif selection == "4":
        cls()
        list = open('steaksauce.txt', 'w')
        for x, y in todo.items():
            print("[" + x + "] " + y + "\n")
        toremove = input("What item have you completed? [Enter A1, B1, etc.] ")
        if toremove in todo:
             del todo[toremove]
        else:
            print("Sorry, but that's not on your to do list")
        for x, y in todo.items():
            lines = x + ". " + y + "\n"
            list.writelines(lines)
        list.close()        
        break
    #Read about Steak Sauce
    elif selection =="5":
        pass
    #Exit
    elif selection == "6":
        running = False
    elif selection == "316":    
        print(todo)
    else:
        print("Sorry. Please make sure you enter a valid number.")
