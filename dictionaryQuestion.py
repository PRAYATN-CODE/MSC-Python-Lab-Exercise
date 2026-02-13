while True:
    print("\n----- DICTIONARY PROGRAM MENU -----")
    print("1. Create student dictionary and count marks >= 40")
    print("2. Display all keys and values")
    print("3. Check whether a key exists")
    print("4. Count total key-value pairs")
    print("5. Delete a key after checking")
    print("6. Separate keys and values into lists")
    print("7. Create dictionary of numbers and their squares")
    print("8. Find key with maximum value")
    print("9. Merge two dictionaries")
    print("10. Sort dictionary based on values")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        d = {}
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            d[name] = marks
        count = 0
        for value in d.values():
            if value >= 40:
                count += 1
        print("Students with marks >= 40:", count)

    elif choice == 2:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value
        for key, value in d.items():
            print("Key:", key, "Value:", value)

    elif choice == 3:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value
        search = input("Enter key to search: ")
        if search in d:
            print("Key exists")
        else:
            print("Key does not exist")

    elif choice == 4:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value
        count = 0
        for key in d:
            count += 1
        print("Total key-value pairs:", count)

    elif choice == 5:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value
        deleteKey = input("Enter key to delete: ")
        if deleteKey in d:
            del d[deleteKey]
            print("Key deleted")
        else:
            print("Key not found")
        print(d)

    elif choice == 6:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value
        keys = list(d.keys())
        values = list(d.values())
        print("Keys:", keys)
        print("Values:", values)

    elif choice == 7:
        squareDictionary = {}
        n = int(input("Enter number of elements: "))
        for i in range(n):
            num = int(input("Enter number: "))
            squareDictionary[num] = num ** 2
        print(squareDictionary)

    elif choice == 8:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            d[key] = value
        max_key = None
        max_value = float('-inf')
        for key, value in d.items():
            if value > max_value:
                max_value = value
                max_key = key
        print("Key with maximum value:", max_key)

    elif choice == 9:
        d1 = {}
        d2 = {}
        n1 = int(input("Enter number of entries for first dictionary: "))
        for i in range(n1):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d1[key] = value
        n2 = int(input("Enter number of entries for second dictionary: "))
        for i in range(n2):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d2[key] = value
        d3 = {}
        for key in d1:
            d3[key] = d1[key]
        for key in d2:
            d3[key] = d2[key]
        print("Merged dictionary:", d3)

    elif choice == 10:
        d = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            d[key] = value
        items = list(d.items())
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i][1] > items[j][1]:
                    items[i], items[j] = items[j], items[i]
        for key, value in items:
            print(key, value)

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
