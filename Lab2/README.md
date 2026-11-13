# Lab 2: Arrays and Matrices

---

## Section A: Concept Check

1. In Python, a 1D array is commonly implemented using a **list**.
2. Inserting an element at the beginning of a list requires shifting **all** elements, making it an **O(n)** operation.
3. Deleting an element from the middle of a list requires shifting all elements **after** it, to fill the gap.
4. A left rotation by k positions moves the first k elements to the **end** of the array.
5. Linear search checks elements **sequentially (one by one)**, while binary search requires the array to be **sorted** first.
6. A sparse matrix stores only **non-zero** elements, along with their **row** and **column** indices.
7. The standard triple format for a sparse matrix entry is **(row, column, value)**.

---

## Section B: Trace the Logic

### 1. Array Operations Trace
Array: `[10, 20, 30, 40, 50]`
- Insert 25 at index 2: `[10, 20, 25, 30, 40, 50]`
- Delete element at index 0: `[20, 25, 30, 40, 50]`
- Rotate left by 2 positions: `[30, 40, 50, 20, 25]`

### 2. Linear Search Trace
Array: `[5, 12, 8, 19, 3, 27]`, Target = `19`
- Check index 0: 5 != 19
- Check index 1: 12 != 19
- Check index 2: 8 != 19
- Check index 3: 19 == 19 -> Found at index 3

### 3. Binary Search Trace
Array: `[2, 4, 7, 10, 15, 20, 22]`, Target = `15`
- Step 1: low = 0, high = 6 -> mid = (0 + 6) // 2 = 3. arr[3] is 10. Since 15 > 10, low = mid + 1 = 4.
- Step 2: low = 4, high = 6 -> mid = (4 + 6) // 2 = 5. arr[5] is 20. Since 15 < 20, high = mid - 1 = 4.
- Step 3: low = 4, high = 4 -> mid = (4 + 4) // 2 = 4. arr[4] is 15. Target found at index 4.

### 4. Sparse Matrix Representation
Matrix D:
```
[[0, 0, 5],
 [0, 8, 0],
 [3, 0, 0],
 [0, 0, 0]]
```
Non-zero triples (row, col, value):
- (0, 2, 5)
- (1, 1, 8)
- (2, 0, 3)

### 5. Storage Comparison for Matrix D
- Full 2D matrix: 4 rows * 3 cols = 12 values
- Sparse triple form: 3 non-zero elements * 3 = 9 values

---

## Section C: Programs Documentation

### Program 1: 1D Array Operations (`array_1d_operations.py`)

- **Aim:** To implement insert, delete, linear search, and left/right rotations on a 1D Python list.
- **Logic:** For insert and delete we check if the index is inside the valid range before modifying the list. For rotations, we use modulo `k % len(arr)` to handle large k, and then slice the list to shift the elements. Linear search loops from index 0 to end comparing each item.

- **Sample Input / Output:**
```
Enter initial array elements: 10 20 30 40 50
Current array: [10, 20, 30, 40, 50]

1. Insert
2. Delete
3. Linear Search
4. Rotate Left
5. Rotate Right
6. Exit
Enter choice: 1
Enter index to insert at: 2
Enter value: 25
Array after insert: [10, 20, 25, 30, 40, 50]

Enter choice: 2
Enter index to delete: 0
Deleted 10. Array: [20, 25, 30, 40, 50]

Enter choice: 4
Enter k: 2
Array after left rotation: [30, 40, 50, 20, 25]

Enter choice: 3
Enter value to search: 40
Found 40 at index 1
```

- **Boundary Cases Tested:**
  - Out of range index for insert:
    ```
    Enter choice: 1
    Enter index to insert at: 10
    Enter value: 99
    Invalid index!
    ```
  - Element not in array:
    ```
    Enter choice: 3
    Enter value to search: 99
    99 not found in array
    ```

---

### Program 2: 2D Array Operations (`array_2d_operations.py`)

- **Aim:** To implement row insertion, row deletion, searching, and 90-degree clockwise rotation on a 2D array.
- **Logic:** We check row index bounds and make sure the new row has the same number of columns as the matrix. For 90 degree clockwise rotation, column `j` becomes the new row, and elements are read from bottom row to top row (`range(rows - 1, -1, -1)`).

- **Sample Input / Output:**
```
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
1 2
3 4
Matrix:
[1, 2]
[3, 4]

1. Insert row
2. Delete row
3. Search value
4. Rotate 90 degrees clockwise
5. Exit
Enter choice: 1
Enter position to insert: 1
Enter row elements: 5 6
Matrix:
[1, 2]
[5, 6]
[3, 4]

Enter choice: 4
Matrix:
[3, 5, 1]
[4, 6, 2]

Enter choice: 3
Enter value to search: 5
Found 5 at row 0, col 1
```

- **Boundary Cases Tested:**
  - Inserting row with wrong number of elements:
    ```
    Enter choice: 1
    Enter position to insert: 1
    Enter row elements: 7 8 9
    Dimension mismatch! Expected 2 elements.
    ```
  - Deleting row at invalid index:
    ```
    Enter choice: 2
    Enter row index to delete: 5
    Invalid row index!
    ```

---

### Program 3: Sparse Matrix Operations (`sparse_matrix_operations.py`)

- **Aim:** To convert a 2D matrix into sparse triple form, reconstruct it back, and add two sparse matrices directly without converting back to full matrices.
- **Logic:** We loop through the matrix and save only elements not equal to 0 as `[row, col, value]`. For adding two sparse matrices, we use two pointers `i` and `j` to walk through both triple lists in sorted row-major order, adding values at matching positions and appending remaining triples.

- **Sample Input / Output:**
```
1. Convert matrix to sparse and reconstruct
2. Add two matrices in sparse form
3. Exit
Enter choice: 1
Enter number of rows: 4
Enter number of columns: 3
Enter elements row by row:
0 0 5
0 8 0
3 0 0
0 0 0

Sparse format:
Sparse representation (4x3):
Row	Col	Val
0	2	5
1	1	8
2	0	3

Reconstructed matrix:
Full matrix:
[0, 0, 5]
[0, 8, 0]
[3, 0, 0]
[0, 0, 0]
```

- **Direct Sparse Addition Sample:**
```
Enter choice: 2
Enter Matrix 1:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
1 0
0 4
Enter Matrix 2:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
0 3
0 -4

Sum in sparse format:
Sparse representation (2x2):
Row	Col	Val
0	0	1
0	1	3

Sum reconstructed full matrix:
Full matrix:
[1, 3]
[0, 0]
```
*(Notice at position (1,1), 4 + (-4) = 0, so it gets removed from the sparse list properly).*

- **Boundary Cases Tested:**
  - Adding matrices with different sizes:
    ```
    Cannot add: matrices have different dimensions!
    ```

---

### Section D Analysis (for Program 3)

1. **Space formulas for m x n matrix with k non-zero elements:**
   - Full 2D matrix space: `m * n`
   - Sparse triple form space: `3 * k`

2. **Testing two 6x6 matrices (36 total elements):**
   - **Matrix 1 (~80% zeros):**
     - Non-zero elements (k) = 7 (so 29 zeros = ~80.5% zeros)
     - Full matrix storage: 36 values
     - Sparse storage: 3 * 7 = 21 values
     - Sparse saves 15 values.
   - **Matrix 2 (<20% zeros):**
     - Non-zero elements (k) = 30 (so 6 zeros = ~16.7% zeros)
     - Full matrix storage: 36 values
     - Sparse storage: 3 * 30 = 90 values
     - Sparse uses 54 MORE values than normal 2D array.

3. **Break-even percentage:**
   Sparse saves space only when:
   `3 * k < m * n`  
   `k / (m * n) < 1/3` (around 33.3%)  
   So if more than ~33% of elements are non-zero, sparse representation stops saving space and takes more memory because each non-zero needs 3 values (row, col, value).

4. **Real-world example:**
   - In social networks (like Instagram or Facebook), people are represented in a huge friendship matrix. Since each user is only friends with a few hundred people out of millions of users, almost all entries in the matrix are 0. Storing it as a sparse matrix saves massive amounts of memory.

---

### Program 4: Matrix Calculator (`matrix_calculator.py`)

- **Aim:** A menu-driven program to perform matrix addition, multiplication, transpose, and determinant.
- **Logic:** Addition requires both matrices to have the exact same dimensions. Multiplication checks that columns of the first matrix match rows of the second matrix, then calculates the dot products. Transpose swaps rows and columns `mat[i][j] -> res[j][i]`. Determinant checks that the matrix is square and computes the value using standard formulas for 1x1, 2x2, and 3x3.

- **Sample Input / Output:**
```
--- Matrix Calculator ---
1. Add two matrices
2. Multiply two matrices
3. Transpose a matrix
4. Find determinant
5. Exit
Enter choice: 1
Enter Matrix A:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
1 2
3 4
Enter Matrix B:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
5 6
7 8
Result:
[6, 8]
[10, 12]

Enter choice: 3
Enter Matrix:
Enter number of rows: 2
Enter number of columns: 3
Enter elements row by row:
1 2 3
4 5 6
Result:
[1, 4]
[2, 5]
[3, 6]

Enter choice: 4
Enter Matrix:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row:
1 2
3 4
Determinant = -2
```

- **Boundary Cases Tested:**
  - Incompatible multiplication (cols of A != rows of B):
    ```
    Cannot multiply: columns of first matrix must equal rows of second matrix!
    ```
  - Finding determinant of non-square matrix:
    ```
    Error: Determinant is only defined for square matrices!
    ```
