# DAA Lab 2 - Task 3: Sparse Matrix Representation and Operations
# Name: Vinisha Wagh
# Description: Program to convert full 2D matrix to sparse triple representation,
# reconstruct full matrix, add sparse matrices directly, and compare space usage.

def display_matrix(matrix, label="Full Matrix"):
    """Prints a 2D matrix row by row."""
    print(f"\n{label}:")
    if not matrix or len(matrix) == 0:
        print(" [Empty Matrix]")
        return
    for row in matrix:
        print(" ", row)


def display_sparse(sparse_data, label="Sparse Triple Representation"):
    """Prints sparse matrix in standard (row, col, value) triples format."""
    rows, cols, triples = sparse_data
    print(f"\n{label}:")
    print(f"Dimensions: {rows} x {cols}, Non-zero entries: {len(triples)}")
    print("Row\tCol\tValue")
    print("-" * 25)
    if not triples:
        print("(all entries are 0)")
    for r, c, val in triples:
        print(f"{r}\t{c}\t{val}")


def to_sparse(matrix):
    """
    Converts a 2D list into sparse triple representation: (rows, cols, triples).
    triples contains (row, col, value) in row-major order.
    """
    if not matrix or len(matrix) == 0:
        return (0, 0, [])
    rows = len(matrix)
    cols = len(matrix[0])
    triples = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return (rows, cols, triples)


def to_full_matrix(sparse_data):
    """Reconstructs the full 2D matrix from sparse triple representation."""
    rows, cols, triples = sparse_data
    if rows == 0 or cols == 0:
        return []
    # Initialize full matrix of zeros
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for r, c, val in triples:
        matrix[r][c] = val
    return matrix


def add_sparse(sparse_a, sparse_b):
    """
    Adds two sparse matrices directly in sparse form without converting to full 2D.
    Uses two pointers i and j to merge sorted triples.
    """
    r1, c1, t1 = sparse_a
    r2, c2, t2 = sparse_b
    
    # Check dimension compatibility
    if r1 != r2 or c1 != c2:
        print(f"Error: Dimension mismatch! Cannot add {r1}x{c1} and {r2}x{c2}.")
        return None
        
    i = 0
    j = 0
    result_triples = []
    
    while i < len(t1) and j < len(t2):
        row1, col1, v1 = t1[i]
        row2, col2, v2 = t2[j]
        
        pos1 = (row1, col1)
        pos2 = (row2, col2)
        
        if pos1 < pos2:
            result_triples.append((row1, col1, v1))
            i += 1
        elif pos2 < pos1:
            result_triples.append((row2, col2, v2))
            j += 1
        else:
            # Same position, add values
            total = v1 + v2
            if total != 0:
                result_triples.append((row1, col1, total))
            i += 1
            j += 1
            
    # Add remaining elements from first matrix
    while i < len(t1):
        result_triples.append(t1[i])
        i += 1
        
    # Add remaining elements from second matrix
    while j < len(t2):
        result_triples.append(t2[j])
        j += 1
        
    return (r1, c1, result_triples)


def compare_forms(sparse_data):
    """Displays sparse form and reconstructed full form together."""
    display_sparse(sparse_data)
    full = to_full_matrix(sparse_data)
    display_matrix(full, "Reconstructed Full Matrix")


def run_space_analysis():
    """Tests space efficiency for Section D with two 6x6 matrices."""
    print("\n--- Section D: Space Optimization Analysis ---")
    
    # Matrix 1: 6x6 with roughly 80% zeros (7 non-zeros out of 36 = 80.6% zeros)
    m1 = [
        [0, 0, 5, 0, 0, 0],
        [0, 8, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 2, 0]
    ]
    
    # Matrix 2: 6x6 with fewer than 20% zeros (30 non-zeros out of 36 = 16.7% zeros)
    m2 = [
        [1,  2,  3,  4,  0,  6],
        [7,  8,  9,  0, 11, 12],
        [13, 14,  0, 16, 17, 18],
        [19,  0, 21, 22, 23, 24],
        [25, 26, 27, 28,  0, 30],
        [31, 32, 33, 34, 35,  0]
    ]
    
    tests = [("Matrix 1 (~80% zeros)", m1), ("Matrix 2 (<20% zeros)", m2)]
    
    for label, mat in tests:
        rows = len(mat)
        cols = len(mat[0])
        total = rows * cols
        sparse_rep = to_sparse(mat)
        k = len(sparse_rep[2])
        full_space = total
        sparse_space = 3 * k
        
        print(f"\n{label}:")
        print(f"  Dimensions: {rows} x {cols} (Total elements: {total})")
        print(f"  Non-zero elements (k): {k}, Zero elements: {total - k}")
        print(f"  Values stored in full 2D: {full_space}")
        print(f"  Values stored in sparse (3k): {sparse_space}")
        if sparse_space < full_space:
            print(f"  -> Sparse saves space! ({full_space - sparse_space} fewer values stored)")
        else:
            print(f"  -> Sparse uses MORE space! ({sparse_space - full_space} extra values stored)")
            
    print("\nBreak-even analysis:")
    print("  Full space = m * n")
    print("  Sparse space = 3 * k")
    print("  Break-even when 3k = mn  =>  k / (mn) = 1/3 = ~33.33%")
    print("  Sparse representation is beneficial only when non-zero elements < 33.3%.")


def input_matrix_from_user(name=""):
    """Reads a matrix from the user."""
    try:
        tag = f" for {name}" if name else ""
        r = int(input(f"Enter number of rows{tag}: "))
        c = int(input(f"Enter number of columns{tag}: "))
        if r <= 0 or c <= 0:
            print("Dimensions must be positive!")
            return None
        mat = []
        print(f"Enter each row ({c} space-separated integers):")
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
        print("Invalid input!")
        return None


def main():
    print("----- Sparse Matrix Operations -----")
    # Sample matrix D from worksheet
    sample_d = [
        [0, 0, 5],
        [0, 8, 0],
        [3, 0, 0],
        [0, 0, 0]
    ]
    current_sparse = to_sparse(sample_d)
    print("Loaded sample matrix D from assignment:")
    compare_forms(current_sparse)

    while True:
        print("\n--- Menu ---")
        print("1. Enter new 2D matrix and convert to sparse")
        print("2. Reconstruct full matrix from current sparse")
        print("3. Add two matrices in sparse form")
        print("4. Compare sparse and full reconstructed forms")
        print("5. Run Section D space analysis test")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            new_mat = input_matrix_from_user()
            if new_mat is not None:
                current_sparse = to_sparse(new_mat)
                compare_forms(current_sparse)
                
        elif choice == '2':
            full = to_full_matrix(current_sparse)
            display_matrix(full, "Reconstructed Full Matrix")
            
        elif choice == '3':
            print("\nEnter Matrix 1:")
            m1 = input_matrix_from_user("Matrix 1")
            if m1 is None:
                continue
            print("\nEnter Matrix 2:")
            m2 = input_matrix_from_user("Matrix 2")
            if m2 is None:
                continue
                
            s1 = to_sparse(m1)
            s2 = to_sparse(m2)
            print("\nMatrix 1 sparse form:")
            display_sparse(s1, "Matrix 1 Sparse")
            print("\nMatrix 2 sparse form:")
            display_sparse(s2, "Matrix 2 Sparse")
            
            s_sum = add_sparse(s1, s2)
            if s_sum is not None:
                print("\nAddition result (computed directly in sparse form):")
                compare_forms(s_sum)
                
        elif choice == '4':
            compare_forms(current_sparse)
            
        elif choice == '5':
            run_space_analysis()
            
        elif choice == '6':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
