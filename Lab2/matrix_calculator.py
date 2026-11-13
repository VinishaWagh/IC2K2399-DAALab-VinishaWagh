# Matrix Calculator: addition, multiplication, transpose, and determinant

def input_matrix(name=""):
    if name:
        print(f"Enter {name}:")
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    mat = []
    print("Enter elements row by row:")
    for i in range(r):
        row = [int(x) for x in input().split()]
        mat.append(row)
    return mat

def print_matrix(mat):
    print("Result:")
    for row in mat:
        print(row)

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Cannot add: matrices must have same dimensions!")
        return None
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        res.append(row)
    return res

def multiply_matrices(a, b):
    # columns of a must equal rows of b
    if len(a[0]) != len(b):
        print("Cannot multiply: columns of first matrix must equal rows of second matrix!")
        return None
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            val = 0
            for k in range(len(b)):
                val += a[i][k] * b[k][j]
            row.append(val)
        res.append(row)
    return res

def transpose(mat):
    res = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        res.append(row)
    return res

def determinant(mat):
    r = len(mat)
    c = len(mat[0])
    if r != c:
        print("Error: Determinant is only defined for square matrices!")
        return None
    if r == 1:
        return mat[0][0]
    elif r == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    elif r == 3:
        det = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
             - mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
             + mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))
        return det
    else:
        print("Determinant only implemented for 1x1, 2x2, and 3x3 matrices.")
        return None

def main():
    while True:
        print("\n--- Matrix Calculator ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find determinant")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            res = add_matrices(a, b)
            if res:
                print_matrix(res)
        elif choice == '2':
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            res = multiply_matrices(a, b)
            if res:
                print_matrix(res)
        elif choice == '3':
            a = input_matrix("Matrix")
            res = transpose(a)
            print_matrix(res)
        elif choice == '4':
            a = input_matrix("Matrix")
            det = determinant(a)
            if det is not None:
                print(f"Determinant = {det}")
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
