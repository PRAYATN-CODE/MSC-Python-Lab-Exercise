while True:
    print("\n----- TUPLE PROGRAM MENU -----")
    print("1. Create and display tuple")
    print("2. Count elements in tuple")
    print("3. Sum of tuple elements")
    print("4. Search element in tuple")
    print("5. Count even and odd numbers")
    print("6. Find maximum and minimum")
    print("7. Convert tuple to list")
    print("8. Reverse tuple")
    print("9. Count occurrences of elements")
    print("10. Extract positive numbers")
    print("11. Demonstrate immutability")
    print("12. Check palindrome")
    print("13. Extract even index elements")
    print("14. Compare two tuples element-wise")
    print("15. Find common elements between two tuples")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        size = int(input("Enter size: "))
        temp = []
        for i in range(size):
            temp.append(int(input("Enter element: ")))
        t = tuple(temp)
        for item in t:
            print(item)

    elif choice == 2:
        t = tuple(map(int, input("Enter elements: ").split()))
        count = 0
        for item in t:
            count += 1
        print("Length:", count)

    elif choice == 3:
        t = tuple(map(int, input("Enter elements: ").split()))
        total = 0
        for item in t:
            total += item
        print("Sum:", total)

    elif choice == 4:
        t = tuple(map(int, input("Enter elements: ").split()))
        search = int(input("Enter element to search: "))
        found = False
        for item in t:
            if item == search:
                found = True
                break
        if found:
            print("Element found")
        else:
            print("Element not found")

    elif choice == 5:
        t = tuple(map(int, input("Enter elements: ").split()))
        even = 0
        odd = 0
        for item in t:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1
        print("Even:", even)
        print("Odd:", odd)

    elif choice == 6:
        t = tuple(map(int, input("Enter elements: ").split()))
        maxValue = t[0]
        minValue = t[0]
        for item in t:
            if item > maxValue:
                maxValue = item
            if item < minValue:
                minValue = item
        print("Maximum:", maxValue)
        print("Minimum:", minValue)

    elif choice == 7:
        t = tuple(map(int, input("Enter elements: ").split()))
        lst = list(t)
        print("List:", lst)

    elif choice == 8:
        t = tuple(map(int, input("Enter elements: ").split()))
        rev = ()
        for item in t:
            rev = (item,) + rev
        print("Reversed tuple:", rev)

    elif choice == 9:
        t = tuple(map(int, input("Enter elements: ").split()))
        freq = {}
        for item in t:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        for key in freq:
            print(key, ":", freq[key])

    elif choice == 10:
        t = tuple(map(int, input("Enter elements: ").split()))
        positive = []
        for item in t:
            if item > 0:
                positive.append(item)
        print("Positive tuple:", tuple(positive))

    elif choice == 11:
        t = tuple(map(int, input("Enter elements: ").split()))
        print("Before modification:", t)
        try:
            t[0] = 100
        except TypeError as e:
            print("Error:", e)
        print("After attempt:", t)

    elif choice == 12:
        t = tuple(map(int, input("Enter elements: ").split()))
        if t == t[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice == 13:
        t = tuple(map(int, input("Enter elements: ").split()))
        evenIndex = []
        for i in range(len(t)):
            if i % 2 == 0:
                evenIndex.append(t[i])
        print("Even index elements:", tuple(evenIndex))

    elif choice == 14:
        t1 = tuple(map(int, input("Enter first tuple: ").split()))
        t2 = tuple(map(int, input("Enter second tuple: ").split()))
        for i in range(min(len(t1), len(t2))):
            if t1[i] == t2[i]:
                print("Index", i, ": Equal")
            elif t1[i] > t2[i]:
                print("Index", i, ": First is greater")
            else:
                print("Index", i, ": Second is greater")

    elif choice == 15:
        t1 = tuple(map(int, input("Enter first tuple: ").split()))
        t2 = tuple(map(int, input("Enter second tuple: ").split()))
        common = []
        for item in t1:
            if item in t2 and item not in common:
                common.append(item)
        print("Common elements:", tuple(common))

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
