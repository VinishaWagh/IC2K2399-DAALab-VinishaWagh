# 1D Array operations: insert, delete, linear search, and rotations

def insert_element(arr, index, val):
    if index < 0 or index > len(arr):
        print("Invalid index!")
        return
    arr.insert(index, val)
    print("Array after insert:", arr)

def delete_element(arr, index):
    if len(arr) == 0:
        print("Array is empty!")
        return
    if index < 0 or index >= len(arr):
        print("Invalid index!")
        return
    removed = arr.pop(index)
    print(f"Deleted {removed}. Array:", arr)

def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            print(f"Found {val} at index {i}")
            return i
    print(f"{val} not found in array")
    return -1

def rotate_left(arr, k):
    if not arr:
        print("Array is empty")
        return
    k = k % len(arr)
    arr[:] = arr[k:] + arr[:k]
    print("Array after left rotation:", arr)

def rotate_right(arr, k):
    if not arr:
        print("Array is empty")
        return
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    print("Array after right rotation:", arr)

def main():
    user_input = input("Enter initial array elements: ").strip()
    if user_input:
        arr = [int(x) for x in user_input.split()]
    else:
        arr = []
    print("Current array:", arr)

    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Linear Search")
        print("4. Rotate Left")
        print("5. Rotate Right")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            idx = int(input("Enter index to insert at: "))
            val = int(input("Enter value: "))
            insert_element(arr, idx, val)
        elif choice == '2':
            idx = int(input("Enter index to delete: "))
            delete_element(arr, idx)
        elif choice == '3':
            val = int(input("Enter value to search: "))
            linear_search(arr, val)
        elif choice == '4':
            k = int(input("Enter k: "))
            rotate_left(arr, k)
        elif choice == '5':
            k = int(input("Enter k: "))
            rotate_right(arr, k)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
