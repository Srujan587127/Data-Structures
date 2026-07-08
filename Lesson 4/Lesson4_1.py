# Binary Search

numbers = [10, 20 , 30, 40, 50, 60]

target = int(input("Enter target number: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers [mid] == target:
        print("Element FOund at Index ", mid)
        found = True
        break

    elif target < numbers[mid]:
        high = mid - 1

    else: 
        low = mid + 1

if not found:
    print("Element not found! ")