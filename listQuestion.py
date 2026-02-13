while True:
    print("\n----- LIST PROGRAM MENU -----")
    print("1. Input and display list")
    print("2. Count even and odd numbers")
    print("3. Find sum of elements")
    print("4. Find largest and smallest element")
    print("5. Count frequency of a given element")
    print("6. Reverse the list")
    print("7. Separate positive and negative numbers")
    print("8. Remove duplicate elements")
    print("9. Check if list is sorted")
    print("10. Find second largest element")
    print("11. Merge two lists")
    print("12. Find common elements between two lists")
    print("13. Rotate list by k positions")
    print("14. Find frequency of each element")
    print("15. Split into even-index and odd-index lists")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = []
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            value = input("Enter element: ")
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    pass
            element.append(value)
        print("The List is:", element)
        for ele in element:
            print(ele)

    elif choice == 2:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        even = 0
        odd = 0
        for ele in element:
            if ele % 2 == 0:
                even += 1
            else:
                odd += 1
        print("Even count:", even)
        print("Odd count:", odd)

    elif choice == 3:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        total = 0
        for ele in element:
            total += ele
        print("Sum:", total)

    elif choice == 4:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        maxValue = element[0]
        minValue = element[0]
        for ele in element:
            if ele > maxValue:
                maxValue = ele
            if ele < minValue:
                minValue = ele
        print("Maximum:", maxValue)
        print("Minimum:", minValue)

    elif choice == 5:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        search = int(input("Enter element to search: "))
        count = 0
        for ele in element:
            if ele == search:
                count += 1
        print("Frequency:", count)

    elif choice == 6:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        rev = []
        for ele in element:
            rev.insert(0, ele)
        print("Reversed list:", rev)

    elif choice == 7:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        positive = []
        negative = []
        for ele in element:
            if ele > 0:
                positive.append(ele)
            elif ele < 0:
                negative.append(ele)
        print("Positive:", positive)
        print("Negative:", negative)

    elif choice == 8:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        unique = []
        for ele in element:
            if ele not in unique:
                unique.append(ele)
        print("Unique elements:", unique)

    elif choice == 9:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        if element == sorted(element):
            print("List is sorted")
        else:
            print("List is not sorted")

    elif choice == 10:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        element = list(set(element))
        element.sort()
        if len(element) >= 2:
            print("Second largest:", element[-2])
        else:
            print("Second largest does not exist")

    elif choice == 11:
        list1 = []
        list2 = []
        size1 = int(input("Enter size of first list: "))
        for i in range(size1):
            list1.append(int(input("Enter number: ")))
        size2 = int(input("Enter size of second list: "))
        for i in range(size2):
            list2.append(int(input("Enter number: ")))
        merged = list1 + list2
        print("Merged list:", merged)

    elif choice == 12:
        list1 = []
        list2 = []
        size1 = int(input("Enter size of first list: "))
        for i in range(size1):
            list1.append(int(input("Enter number: ")))
        size2 = int(input("Enter size of second list: "))
        for i in range(size2):
            list2.append(int(input("Enter number: ")))
        common = []
        for ele in list1:
            if ele in list2 and ele not in common:
                common.append(ele)
        print("Common elements:", common)

    elif choice == 13:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        k = int(input("Enter k: "))
        k = k % len(element)
        rotated = element[-k:] + element[:-k]
        print("Rotated list:", rotated)

    elif choice == 14:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        freq = {}
        for ele in element:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1
        for key in freq:
            print(key, ":", freq[key])

    elif choice == 15:
        element = []
        size = int(input("Enter the size: "))
        for i in range(size):
            element.append(int(input("Enter number: ")))
        evenIndex = element[::2]
        oddIndex = element[1::2]
        print("Even index list:", evenIndex)
        print("Odd index list:", oddIndex)

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
