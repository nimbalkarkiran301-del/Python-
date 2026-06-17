
club1 = {"Kiran", "Ravi", "Amit", "Neha"}
club2 = {"Amit", "Priya", "Ravi", "Sohan"}
club3 = {"Ravi", "Amit", "Pooja", "Neha"}

while True:
    print("\n----- Club Management -----")
    print("1. Display all members of each club")
    print("2. Display all unique members")
    print("3. Display members in all three clubs")
    print("4. Add a new member")
    print("5. Remove a member from all clubs")
    print("6. Check membership")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    # 1. Display all members
    if ch == 1:
        print("Club1 Members:", club1)
        print("Club2 Members:", club2)
        print("Club3 Members:", club3)

    # 2. Display all unique members
    elif ch == 2:
        all_members = club1 | club2 | club3
        print("Unique Members:", all_members)

    # 3. Display common members in all clubs
    elif ch == 3:
        common = club1 & club2 & club3
        print("Members in all three clubs:", common)

    # 4. Add new member
    elif ch == 4:
        club_no = int(input("Enter club number (1/2/3): "))
        name = input("Enter member name: ")

        if club_no == 1:
            if name in club1:
                print("Member already exists in Club1")
            else:
                club1.add(name)
                print("Member added successfully")

        elif club_no == 2:
            if name in club2:
                print("Member already exists in Club2")
            else:
                club2.add(name)
                print("Member added successfully")

        elif club_no == 3:
            if name in club3:
                print("Member already exists in Club3")
            else:
                club3.add(name)
                print("Member added successfully")

    # 5. Remove member from all clubs
    elif ch == 5:
        name = input("Enter member name to remove: ")

        if name not in club1 and name not in club2 and name not in club3:
            print("Warning: Member does not exist in any club")
        else:
            club1.discard(name)
            club2.discard(name)
            club3.discard(name)
            print("Member removed from all clubs")

    # 6. Check membership
    elif ch == 6:
        name = input("Enter member name: ")
        found = False

        if name in club1:
            print(name, "belongs to Club1")
            found = True
        if name in club2:
            print(name, "belongs to Club2")
            found = True
        if name in club3:
            print(name, "belongs to Club3")
            found = True

        if not found:
            print("Not a member of any club")

    # Exit
    elif ch == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")