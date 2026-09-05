# DAA Lab 2 - Task 4: Matrix Calculator
# Name: Vinisha Wagh
# Description: Menu-driven program to add, multiply, transpose, and find determinant of matrices.

def print_matrix(matrix, label="Matrix"):
    """Prints matrix row by row."""
    print(f"\n{label}:")
    if not matrix or len(matrix) == 0:
        print(" [Empty]")
        return
    for row in matrix:
        print(" ", row)


def input_matrix(name="Matrix"):
    """Takes input for a matrix from the user."""
    try:
        r = int(input(f"Enter number of rows for {name}: "))
        c = int(input(f"Enter number of columns for {name}: "))
        if r <= 0 or c <= 0:
            print("Invalid dimensions!")
            return None
        mat = []
        print(f"Enter each row with {c} space-separated numbers:")
        for i in range(r):
            while True:
                line = input(f"Row {i}: ").strip().split()
                if len(line) != c:
                    print(f"Expected {c} numbers, got {len(line)}. Try again.")
                    continue
                row_nums = []
                for x in line:
                    if '.' in x:
                        row_nums.append(float(x))
                    else:
                        row_nums.append(int(x))
                mat.append(row_nums)
                break
        return mat
    except ValueError:
        print("Invalid input!")
        return None


def add_matrices(a, b):
    """Adds two matrices of same dimensions."""
    r1, c1 = len(a), len(a[0])
    r2, c2 = len(b), len(b[0])
    if r1 != r2 or c1 != c2:
        print(f"Error: Incompatible dimensions for addition! Cannot add {r1}x{c1} and {r2}x{c2}.")
        return None
    result = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def multiply_matrices(a, b):
    """Multiplies two matrices: cols of A must equal rows of B."""
    r1, c1 = len(a), len(a[0])
    r2, c2 = len(b), len(b[0])
    if c1 != r2:
        print(f"Error: Cannot multiply! Columns of first matrix ({c1}) != Rows of second matrix ({r2}).")
        return None
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


def transpose(matrix):
    """Transposes an m x n matrix to n x m."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        row = []
        for r in range(rows):
            row.append(matrix[r][c])
        transposed.append(row)
    return transposed


def determinant(matrix):
    """Computes determinant of a square matrix using cofactor expansion."""
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        print(f"Error: Matrix is not square ({rows}x{cols}), determinant cannot be calculated!")
        return None
        
    if rows == 1:
        return matrix[0][0]
    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
    det = 0
    for c in range(cols):
        # Create submatrix removing row 0 and column c
        submatrix = []
        for r in range(1, rows):
            submatrix.append(matrix[r][:c] + matrix[r][c + 1:])
        sign = (-1) ** c
        det += sign * matrix[0][c] * determinant(submatrix)
    return det


def main():
    print("===== Matrix Calculator =====")
    while True:
        print("\n--- Menu ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find determinant of a matrix")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            print("\nEnter Matrix A:")
            a = input_matrix("Matrix A")
            if a is None:
                continue
            print("\nEnter Matrix B:")
            b = input_matrix("Matrix B")
            if b is None:
                continue
            res = add_matrices(a, b)
            if res is not None:
                print_matrix(res, "Result of A + B")
                
        elif choice == '2':
            print("\nEnter Matrix A:")
            a = input_matrix("Matrix A")
            if a is None:
                continue
            print("\nEnter Matrix B:")
            b = input_matrix("Matrix B")
            if b is None:
                continue
            res = multiply_matrices(a, b)
            if res is not None:
                print_matrix(res, "Result of A * B")
                
        elif choice == '3':
            mat = input_matrix("Matrix")
            if mat is None:
                continue
            res = transpose(mat)
            print_matrix(res, "Transposed Matrix")
            
        elif choice == '4':
            mat = input_matrix("Matrix")
            if mat is None:
                continue
            det_val = determinant(mat)
            if det_val is not None:
                print(f"Determinant = {det_val}")
                
        elif choice == '5':
            print("Exiting calculator.")
            break
            
        else:
            print("Invalid choice, please select between 1 and 5.")


if __name__ == "__main__":
    main()
