# Sparse matrix operations: convert to sparse triple, reconstruct, and add in sparse form

def to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    triples = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                triples.append([r, c, matrix[r][c]])
    return rows, cols, triples

def to_full_matrix(rows, cols, triples):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for r, c, val in triples:
        matrix[r][c] = val
    return matrix

def display_sparse(rows, cols, triples):
    print(f"Sparse representation ({rows}x{cols}):")
    print("Row\tCol\tVal")
    for r, c, val in triples:
        print(f"{r}\t{c}\t{val}")

def display_matrix(matrix):
    print("Full matrix:")
    for row in matrix:
        print(row)

def add_sparse(s1, s2):
    r1, c1, t1 = s1
    r2, c2, t2 = s2
    
    if r1 != r2 or c1 != c2:
        print("Cannot add: matrices have different dimensions!")
        return None
        
    i = 0
    j = 0
    result_triples = []
    
    while i < len(t1) and j < len(t2):
        pos1 = (t1[i][0], t1[i][1])
        pos2 = (t2[j][0], t2[j][1])
        
        if pos1 < pos2:
            result_triples.append(t1[i])
            i += 1
        elif pos2 < pos1:
            result_triples.append(t2[j])
            j += 1
        else:
            total = t1[i][2] + t2[j][2]
            if total != 0:
                result_triples.append([t1[i][0], t1[i][1], total])
            i += 1
            j += 1
            
    while i < len(t1):
        result_triples.append(t1[i])
        i += 1
    while j < len(t2):
        result_triples.append(t2[j])
        j += 1
        
    return r1, c1, result_triples

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

def main():
    while True:
        print("\n--- Sparse Matrix Operations ---")
        print("1. Convert matrix to sparse and reconstruct")
        print("2. Add two matrices in sparse form")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            mat = input_matrix()
            r, c, triples = to_sparse(mat)
            print("\nSparse format:")
            display_sparse(r, c, triples)
            print("\nReconstructed matrix:")
            reconstructed = to_full_matrix(r, c, triples)
            display_matrix(reconstructed)
            
        elif choice == '2':
            mat1 = input_matrix("Matrix 1")
            mat2 = input_matrix("Matrix 2")
            s1 = to_sparse(mat1)
            s2 = to_sparse(mat2)
            
            print("\nMatrix 1 sparse:")
            display_sparse(s1[0], s1[1], s1[2])
            print("\nMatrix 2 sparse:")
            display_sparse(s2[0], s2[1], s2[2])
            
            res = add_sparse(s1, s2)
            if res:
                print("\nSum in sparse format:")
                display_sparse(res[0], res[1], res[2])
                print("\nSum reconstructed full matrix:")
                full_res = to_full_matrix(res[0], res[1], res[2])
                display_matrix(full_res)
                
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
