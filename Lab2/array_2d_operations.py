# 2D Array operations: insert row, delete row, search, and 90 degree clockwise rotation

def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(row)

def insert_row(matrix, pos, new_row):
    if pos < 0 or pos > len(matrix):
        print("Invalid row index!")
        return
    if matrix and len(new_row) != len(matrix[0]):
        print(f"Dimension mismatch! Expected {len(matrix[0])} elements.")
        return
    matrix.insert(pos, new_row)
    display_matrix(matrix)

def delete_row(matrix, pos):
    if not matrix:
        print("Matrix is empty!")
        return
    if pos < 0 or pos >= len(matrix):
        print("Invalid row index!")
        return
    deleted = matrix.pop(pos)
    print(f"Deleted row: {deleted}")
    display_matrix(matrix)

def search_element(matrix, val):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == val:
                print(f"Found {val} at row {i}, col {j}")
                return
    print(f"{val} not found in matrix")

def rotate_clockwise_90(matrix):
    if not matrix:
        print("Matrix is empty")
        return
    rows = len(matrix)
    cols = len(matrix[0])
    rotated = []
    for c in range(cols):
        new_row = []
        for r in range(rows - 1, -1, -1):
            new_row.append(matrix[r][c])
        rotated.append(new_row)
    matrix[:] = rotated
    display_matrix(matrix)

def main():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    matrix = []
    print("Enter elements row by row:")
    for i in range(r):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    display_matrix(matrix)

    while True:
        print("\n1. Insert row")
        print("2. Delete row")
        print("3. Search value")
        print("4. Rotate 90 degrees clockwise")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            pos = int(input("Enter position to insert: "))
            new_row = [int(x) for x in input("Enter row elements: ").split()]
            insert_row(matrix, pos, new_row)
        elif choice == '2':
            pos = int(input("Enter row index to delete: "))
            delete_row(matrix, pos)
        elif choice == '3':
            val = int(input("Enter value to search: "))
            search_element(matrix, val)
        elif choice == '4':
            rotate_clockwise_90(matrix)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
