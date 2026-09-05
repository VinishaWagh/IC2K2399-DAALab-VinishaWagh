# DAA Lab 2 - Task 1: 1D Array Operations
# Name: Vinisha Wagh
# Description: Program to perform insert, delete, linear search, and left/right rotations on a 1D array.

def display_array(arr):
    """Prints the current state and length of the array."""
    print("Array:", arr, f"(Size: {len(arr)})")


def insert_element(arr, index, value):
    """Inserts an element at the specified index after checking bounds."""
    if index < 0 or index > len(arr):
        print(f"Error: Index {index} is out of range! Valid range is 0 to {len(arr)}.")
        return False
    arr.insert(index, value)
    print(f"Successfully inserted {value} at index {index}.")
    display_array(arr)
    return True


def delete_element(arr, index):
    """Deletes an element from the given index after checking bounds."""
    if len(arr) == 0:
        print("Error: Array is empty, cannot delete!")
        return None
    if index < 0 or index >= len(arr):
        print(f"Error: Index {index} is out of range! Valid range is 0 to {len(arr) - 1}.")
        return None
    removed = arr.pop(index)
    print(f"Successfully deleted {removed} from index {index}.")
    display_array(arr)
    return removed


def linear_search(arr, target):
    """Searches sequentially for a value in the array."""
    print(f"Searching for {target}...")
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Found {target} at index {i}.")
            return i
    print(f"{target} was not found in the array.")
    return -1


def rotate_left(arr, k):
    """Rotates the array left by k positions."""
    if len(arr) == 0:
        print("Array is empty, nothing to rotate.")
        display_array(arr)
        return arr
    
    # In case k is larger than array length
    k = k % len(arr)
    arr[:] = arr[k:] + arr[:k]
    print(f"Array rotated left by {k} position(s):")
    display_array(arr)
    return arr


def rotate_right(arr, k):
    """Rotates the array right by k positions."""
    if len(arr) == 0:
        print("Array is empty, nothing to rotate.")
        display_array(arr)
        return arr
        
    k = k % len(arr)
    if k != 0:
        arr[:] = arr[-k:] + arr[:-k]
    print(f"Array rotated right by {k} position(s):")
    display_array(arr)
    return arr


def main():
    print("----- 1D Array Operations -----")
    user_input = input("Enter array elements separated by spaces (or press enter for empty): ").strip()
    if user_input:
        try:
            arr = [int(x) for x in user_input.split()]
        except ValueError:
            arr = user_input.split()
    else:
        arr = []
    
    print("Initial array:")
    display_array(arr)

    while True:
        print("\n--- Menu ---")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Linear search")
        print("4. Rotate left by k")
        print("5. Rotate right by k")
        print("6. Display array")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == '1':
            try:
                idx = int(input(f"Enter index to insert at (0 to {len(arr)}): "))
                val = int(input("Enter integer value to insert: "))
                insert_element(arr, idx, val)
            except ValueError:
                print("Invalid input! Please enter integers.")
                
        elif choice == '2':
            if len(arr) == 0:
                print("Error: Array is already empty!")
                continue
            try:
                idx = int(input(f"Enter index to delete (0 to {len(arr) - 1}): "))
                delete_element(arr, idx)
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '3':
            try:
                val = int(input("Enter value to search: "))
                linear_search(arr, val)
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '4':
            try:
                k = int(input("Enter positions k to rotate left: "))
                rotate_left(arr, k)
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '5':
            try:
                k = int(input("Enter positions k to rotate right: "))
                rotate_right(arr, k)
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '6':
            display_array(arr)
            
        elif choice == '7':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice, please select between 1 and 7.")


if __name__ == "__main__":
    main()
