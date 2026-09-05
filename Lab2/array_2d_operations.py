# DAA Lab 2 - Task 2: 2D Array Operations
# Name: Vinisha Wagh
# Description: Program to insert a row, delete a row, search a value, and rotate a 2D array 90 degrees clockwise.

def display_matrix(matrix):
    """Prints the 2D array in proper row-by-row format."""
    if not matrix or len(matrix) == 0:
        print("Matrix is empty.")
        return
    print(f"Matrix ({len(matrix)} x {len(matrix[0])}):")
    for row in matrix:
        print(" ", row)


def insert_row(matrix, position, new_row):
    """Inserts a new row at the given position with dimension checking."""
    if position < 0 or position > len(matrix):
        print(f"Error: Position {position} is out of bounds! Valid range is 0 to {len(matrix)}.")
        return False
        
    if len(matrix) > 0:
        expected_cols = len(matrix[0])
        if len(new_row) != expected_cols:
            print(f"Error: Dimension mismatch! Expected {expected_cols} columns, but got {len(new_row)}.")
            return False
            
    matrix.insert(position, new_row)
    print(f"Successfully inserted row at position {position}:")
    display_matrix(matrix)
    return True


def delete_row(matrix, position):
    """Deletes a row at the given position."""
    if not matrix or len(matrix) == 0:
        print("Error: Matrix is empty, cannot delete row!")
        return None
        
    if position < 0 or position >= len(matrix):
        print(f"Error: Position {position} is out of bounds! Valid range is 0 to {len(matrix) - 1}.")
        return None
        
    removed = matrix.pop(position)
    print(f"Successfully deleted row {position} ({removed}):")
    display_matrix(matrix)
    return removed


def search_element(matrix, target):
    """Searches for a value across the 2D array and prints row, column."""
    if not matrix or len(matrix) == 0:
        print("Matrix is empty.")
        return None
        
    print(f"Searching for {target}...")
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                print(f"Found {target} at row {r}, column {c}.")
                return (r, c)
                
    print(f"{target} was not found in the matrix.")
    return None


def rotate_clockwise_90(matrix):
    """Rotates the 2D array 90 degrees clockwise."""
    if not matrix or len(matrix) == 0:
        print("Matrix is empty, cannot rotate.")
        return matrix
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    rotated = []
    for c in range(cols):
        new_row = []
        for r in range(rows - 1, -1, -1):
            new_row.append(matrix[r][c])
        rotated.append(new_row)
        
    matrix[:] = rotated
    print("Matrix rotated 90 degrees clockwise:")
    display_matrix(matrix)
    return matrix


def input_new_matrix():
    """Helper function to read a matrix from user."""
    try:
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        if r <= 0 or c <= 0:
            print("Invalid dimensions!")
            return []
        mat = []
        print(f"Enter elements for each row ({c} space-separated numbers per row):")
        for i in range(r):
            while True:
                line = input(f"Row {i}: ").strip().split()
                if len(line) != c:
                    print(f"Expected {c} numbers, got {len(line)}. Try again.")
                    continue
                mat.append([int(x) for x in line])
                break
        return mat
    except ValueError:
        print("Invalid input, expected numbers.")
        return []


def main():
    print("----- 2D Array Operations -----")
    # Provide a simple default matrix to make running and testing easy
    choice_init = input("Use default sample 3x3 matrix? (y/n): ").strip().lower()
    if choice_init == 'n':
        matrix = input_new_matrix()
    else:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
    display_matrix(matrix)

    while True:
        print("\n--- Menu ---")
        print("1. Insert a row")
        print("2. Delete a row")
        print("3. Search for a value")
        print("4. Rotate 90 degrees clockwise")
        print("5. Display current matrix")
        print("6. Enter a new matrix")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == '1':
            try:
                pos = int(input(f"Enter position to insert (0 to {len(matrix)}): "))
                cols_needed = len(matrix[0]) if len(matrix) > 0 else None
                if cols_needed:
                    prompt = f"Enter {cols_needed} numbers for row: "
                else:
                    prompt = "Enter numbers for row: "
                row = [int(x) for x in input(prompt).strip().split()]
                insert_row(matrix, pos, row)
            except ValueError:
                print("Invalid input!")
                
        elif choice == '2':
            if not matrix:
                print("Matrix is empty!")
                continue
            try:
                pos = int(input(f"Enter row index to delete (0 to {len(matrix) - 1}): "))
                delete_row(matrix, pos)
            except ValueError:
                print("Invalid input!")
                
        elif choice == '3':
            try:
                val = int(input("Enter value to search: "))
                search_element(matrix, val)
            except ValueError:
                print("Invalid input!")
                
        elif choice == '4':
            rotate_clockwise_90(matrix)
            
        elif choice == '5':
            display_matrix(matrix)
            
        elif choice == '6':
            matrix = input_new_matrix()
            display_matrix(matrix)
            
        elif choice == '7':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice, please select between 1 and 7.")


if __name__ == "__main__":
    main()
