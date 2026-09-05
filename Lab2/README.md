# DAA Lab 2: Arrays, 2D Arrays, and Sparse Matrices

**Name:** Vinisha Wagh  
**Subject:** Design and Analysis of Algorithms Lab (Semester 7)  
**Lab Assignment:** Lab 2  

---

## Section A: Concept Check

1. In Python, a 1D array is commonly implemented using a **list**.
2. Inserting an element at the beginning of a list requires shifting **all n existing** elements, making it an **O(n)** operation.
3. Deleting an element from the middle of a list requires shifting all elements **after** it, to fill the gap.
4. A left rotation by k positions moves the first k elements to the **end** of the array.
5. Linear search checks elements **sequentially (one by one)**, while binary search requires the array to be **sorted** first.
6. A sparse matrix stores only **non-zero** elements, along with their **row indices** and **column indices**.
7. The standard triple format for a sparse matrix entry is **(row, column, value)**.

---

## Section B: Trace the Logic (Worksheet Solutions)

### 1. Array Operations Trace
Given array: `[10, 20, 30, 40, 50]`
- **Insert 25 at index 2:**  
  Elements at index 2, 3, and 4 shift right.  
  Array becomes: `[10, 20, 25, 30, 40, 50]`
- **Delete element at index 0:**  
  Element 10 is removed, elements shift left.  
  Array becomes: `[20, 25, 30, 40, 50]`
- **Rotate resulting array left by 2 positions:**  
  First 2 elements (`20, 25`) go to the end.  
  Final Array: `[30, 40, 50, 20, 25]`

### 2. Linear Search Trace
Given array: `[5, 12, 8, 19, 3, 27]`, Target = `19`
- Step 1: Check index 0 -> `5 != 19`
- Step 2: Check index 1 -> `12 != 19`
- Step 3: Check index 2 -> `8 != 19`
- Step 4: Check index 3 -> `19 == 19` (Match found)  
Result: Target 19 found at **index 3** after 4 checks.

### 3. Binary Search Trace
Given sorted array: `[2, 4, 7, 10, 15, 20, 22]`, Target = `15`
- **Step 1:** `low = 0`, `high = 6`  
  `mid = (0 + 6) // 2 = 3`  
  `arr[3] = 10`. Since `15 > 10`, search right side: `low = mid + 1 = 4`.
- **Step 2:** `low = 4`, `high = 6`  
  `mid = (4 + 6) // 2 = 5`  
  `arr[5] = 20`. Since `15 < 20`, search left side: `high = mid - 1 = 4`.
- **Step 3:** `low = 4`, `high = 4`  
  `mid = (4 + 4) // 2 = 4`  
  `arr[4] = 15`. Since `arr[4] == 15`, target is found!  
Result: Target 15 found at **index 4** in 3 steps.

### 4. Sparse Matrix Representation
Matrix D:
```
[[0, 0, 5],
 [0, 8, 0],
 [3, 0, 0],
 [0, 0, 0]]
```
Dimensions: 4 rows x 3 columns.  
Non-zero entries in row-major order:
- Row 0, Col 2: 5 -> `(0, 2, 5)`
- Row 1, Col 1: 8 -> `(1, 1, 8)`
- Row 2, Col 0: 3 -> `(2, 0, 3)`
- Row 3 has all zeros.

**Sparse Triple Representation:**
```
[(0, 2, 5), (1, 1, 8), (2, 0, 3)]
```

### 5. Values Stored Comparison for Matrix D
- **Full 2D representation:** Stores every entry: $4 \times 3 =$ **12 values**.
- **Sparse triple representation:** Stores 3 numbers `(row, col, value)` for each non-zero entry: $3 \times 3 =$ **9 values** (or 12 if counting the 3 numbers for rows, cols, non-zero count header).

---

## Section C: Programs Documentation

### Program 1: 1D Array Operations (`array_1d_operations.py`)

- **Aim:**  
  To write a Python program that performs insertion, deletion, linear search, and left/right rotation on a 1D array with input validation.

- **Logic:**  
  Before inserting or deleting, the program checks if the index is within the valid bounds to prevent errors. For rotations, modulo arithmetic (`k % len`) calculates the actual shift needed, and list slicing rearranges the elements. Linear search iterates through the array from start to end comparing each element with the target.

- **Sample Input / Output:**

```
----- 1D Array Operations -----
Enter array elements separated by spaces (or press enter for empty): 10 20 30 40 50
Initial array:
Array: [10, 20, 30, 40, 50] (Size: 5)

--- Menu ---
1. Insert an element
2. Delete an element
3. Linear search
4. Rotate left by k
5. Rotate right by k
6. Display array
7. Exit
Enter choice (1-7): 1
Enter index to insert at (0 to 5): 2
Enter integer value to insert: 25
Successfully inserted 25 at index 2.
Array: [10, 20, 25, 30, 40, 50] (Size: 6)

Enter choice (1-7): 2
Enter index to delete (0 to 5): 0
Successfully deleted 10 from index 0.
Array: [20, 25, 30, 40, 50] (Size: 5)

Enter choice (1-7): 4
Enter positions k to rotate left: 2
Array rotated left by 2 position(s):
Array: [30, 40, 50, 20, 25] (Size: 5)

Enter choice (1-7): 3
Enter value to search: 40
Searching for 40...
Found 40 at index 1.

Enter choice (1-7): 5
Enter positions k to rotate right: 1
Array rotated right by 1 position(s):
Array: [25, 30, 40, 50, 20] (Size: 5)
```

- **Boundary Cases Tested:**
  - **Out of bounds insertion index:**  
    Input: Insert at index `10` in a 5-element array  
    Output: `Error: Index 10 is out of range! Valid range is 0 to 5.`
  - **Out of bounds deletion index:**  
    Input: Delete index `7` in a 5-element array  
    Output: `Error: Index 7 is out of range! Valid range is 0 to 4.`
  - **Search element not found:**  
    Input: Search for `99`  
    Output: `99 was not found in the array.`
  - **Empty array:**  
    Input: Delete on `[]`  
    Output: `Error: Array is empty, cannot delete!`

---

### Program 2: 2D Array Operations (`array_2d_operations.py`)

- **Aim:**  
  To write a Python program that performs row insertion, row deletion, 2D search, and 90-degree clockwise rotation on a 2D array.

- **Logic:**  
  When inserting a row, we verify that the row index is within bounds and the number of columns matches existing rows. For rotation, the element at row $r$ and column $c$ moves to column $c$ and new row position from the bottom, effectively turning rows into columns. The search scans row by row and prints the matching row and column indices.

- **Sample Input / Output:**

```
----- 2D Array Operations -----
Use default sample 3x3 matrix? (y/n): y
Matrix (3 x 3):
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]

--- Menu ---
1. Insert a row
2. Delete a row
3. Search for a value
4. Rotate 90 degrees clockwise
5. Display current matrix
6. Enter a new matrix
7. Exit
Enter choice (1-7): 1
Enter position to insert (0 to 3): 1
Enter 3 numbers for row: 10 20 30
Successfully inserted row at position 1:
Matrix (4 x 3):
  [1, 2, 3]
  [10, 20, 30]
  [4, 5, 6]
  [7, 8, 9]

Enter choice (1-7): 2
Enter row index to delete (0 to 3): 2
Successfully deleted row 2 ([4, 5, 6]):
Matrix (3 x 3):
  [1, 2, 3]
  [10, 20, 30]
  [7, 8, 9]

Enter choice (1-7): 3
Enter value to search: 20
Searching for 20...
Found 20 at row 1, column 1.

Enter choice (1-7): 4
Matrix rotated 90 degrees clockwise:
Matrix (3 x 3):
  [7, 10, 1]
  [8, 20, 2]
  [9, 30, 3]
```

- **Boundary Cases Tested:**
  - **Incompatible row length on insertion:**  
    Input: Insert row `[99, 99]` into a 3-column matrix  
    Output: `Error: Dimension mismatch! Expected 3 columns, but got 2.`
  - **Out of bounds row deletion:**  
    Input: Delete row index `5` in a 3-row matrix  
    Output: `Error: Position 5 is out of bounds! Valid range is 0 to 2.`
  - **Search element not present:**  
    Input: Search for `100`  
    Output: `100 was not found in the matrix.`

---

### Program 3: Sparse Matrix Representation & Operations (`sparse_matrix_operations.py`)

- **Aim:**  
  To convert a 2D matrix into its sparse triple form, reconstruct the matrix back, add two matrices directly while in sparse form, and compare their storage requirements.

- **Logic:**  
  The conversion iterates over the full matrix and saves only non-zero elements with their row and column coordinates. Addition uses two pointers to compare the current triples of both matrices in sorted row-major order, adding matching cells and inserting non-zero results directly without creating full 2D arrays. Reconstruction initializes a zero matrix and places each non-zero value at its given coordinate.

- **Sample Input / Output:**

```
----- Sparse Matrix Operations -----
Loaded sample matrix D from assignment:

Sparse Triple Representation:
Dimensions: 4 x 3, Non-zero entries: 3
Row	Col	Value
-------------------------
0	2	5
1	1	8
2	0	3

Reconstructed Full Matrix:
  [0, 0, 5]
  [0, 8, 0]
  [3, 0, 0]
  [0, 0, 0]

--- Adding Two Sparse Matrices Directly ---
Matrix 1 (2x2):
  [1, 0]
  [0, 4]  -> Triples: [(0, 0, 1), (1, 1, 4)]

Matrix 2 (2x2):
  [0, 3]
  [0, -4] -> Triples: [(0, 1, 3), (1, 1, -4)]

Addition result (computed directly in sparse form):
Sparse Triple Representation:
Dimensions: 2 x 2, Non-zero entries: 2
Row	Col	Value
-------------------------
0	0	1
0	1	3

Reconstructed Full Matrix:
  [1, 3]
  [0, 0]
```
*(Note: At position (1, 1), `4 + (-4) = 0`, which was correctly omitted from the sparse result).*

- **Boundary Cases Tested:**
  - **Incompatible dimensions for addition:**  
    Input: Matrix 1 is `2x3`, Matrix 2 is `3x2`  
    Output: `Error: Dimension mismatch! Cannot add 2x3 and 3x2.`
  - **Values cancelling out to zero:** Summing `4` and `-4` at `(1, 1)` yields `0`, which is ignored so sparsity is preserved.

---

### Section D: Space Optimization Analysis

#### 1. Space Used Formulas
For an $m \times n$ matrix having $k$ non-zero elements:
- **Full 2D representation:** Stores all entries = **$m \times n$ values**.
- **Sparse triple representation:** Stores 3 numbers `(row, col, value)` for each non-zero element = **$3k$ values** (or $3k + 3$ if including the 3 header numbers for rows, columns, and total non-zero elements).

#### 2. Experimental Test on two 6x6 Matrices (36 total cells)

- **Matrix 1 (~80% zeros, i.e. ~20% non-zeros):**
  - Dimensions: $6 \times 6 = 36$ elements
  - Non-zero count ($k$): **7** ($19.4\%$ non-zero, $80.6\%$ zeros)
  - Full 2D storage: **36 values**
  - Sparse storage ($3k$): $3 \times 7 =$ **21 values**
  - **Result:** Sparse saves **15 values** ($41.7\%$ space reduction).

- **Matrix 2 (<20% zeros, i.e. >80% non-zeros):**
  - Dimensions: $6 \times 6 = 36$ elements
  - Non-zero count ($k$): **30** ($83.3\%$ non-zero, $16.7\%$ zeros)
  - Full 2D storage: **36 values**
  - Sparse storage ($3k$): $3 \times 30 =$ **90 values**
  - **Result:** Sparse uses **54 extra values** ($150\%$ overhead compared to full matrix).

#### 3. Break-Even Percentage
- Sparse saves space when:
  $$3k < m \times n \implies \frac{k}{m \times n} < \frac{1}{3} \approx 33.33\%$$
- **Reasoning:** Since each non-zero element in the sparse format needs 3 numbers (row, column, and value), if more than **$\approx 33.3\%$** of the elements are non-zero (i.e. fewer than ~66.7% are zero), the sparse format ends up taking more memory than a standard 2D array.

#### 4. Real-World Applications of Sparse Matrices
- **Social Network Adjacency Matrices (e.g. Instagram/Facebook graph):**  
  In a network with millions of users, each user is only connected to a few hundred friends. A complete adjacency matrix would have trillions of cells, but almost all of them are zero because any two random people are rarely friends.
- **Search Engine Term-Document Matrix:**  
  Rows are dictionary words and columns are web pages. A web page only mentions a tiny fraction of all available words in a language, so over 99% of entries in each column are zero.

---

### Program 4: Matrix Calculator (`matrix_calculator.py`)

- **Aim:**  
  To implement a menu-driven calculator in Python supporting matrix addition, multiplication, transpose, and determinant.

- **Logic:**  
  Addition verifies that both matrices have identical dimensions before adding elements at corresponding indices. Multiplication verifies that columns of the first matrix equal rows of the second matrix before computing dot products. Transpose swaps rows with columns, and determinant verifies that the matrix is square before using cofactor expansion along the first row.

- **Sample Input / Output:**

```
===== Matrix Calculator =====

--- Menu ---
1. Add two matrices
2. Multiply two matrices
3. Transpose a matrix
4. Find determinant of a matrix
5. Exit
Enter choice (1-5): 1

Enter Matrix A:
Enter number of rows for Matrix A: 2
Enter number of columns for Matrix A: 2
Enter each row with 2 space-separated numbers:
Row 0: 1 2
Row 1: 3 4

Enter Matrix B:
Enter number of rows for Matrix B: 2
Enter number of columns for Matrix B: 2
Enter each row with 2 space-separated numbers:
Row 0: 5 6
Row 1: 7 8

Result of A + B:
  [6, 8]
  [10, 12]

Enter choice (1-5): 2

Enter Matrix A:
Enter number of rows for Matrix A: 2
Enter number of columns for Matrix A: 3
Enter each row with 3 space-separated numbers:
Row 0: 1 2 3
Row 1: 4 5 6

Enter Matrix B:
Enter number of rows for Matrix B: 3
Enter number of columns for Matrix B: 2
Enter each row with 2 space-separated numbers:
Row 0: 7 8
Row 1: 9 1
Row 2: 2 3

Result of A * B:
  [31, 19]
  [85, 55]

Enter choice (1-5): 3
Enter number of rows for Matrix: 2
Enter number of columns for Matrix: 3
Row 0: 1 2 3
Row 1: 4 5 6

Transposed Matrix:
  [1, 4]
  [2, 5]
  [3, 6]

Enter choice (1-5): 4
Enter number of rows for Matrix: 3
Enter number of columns for Matrix: 3
Row 0: 6 1 1
Row 1: 4 -2 5
Row 2: 2 8 7

Determinant = -306
```

- **Boundary Cases Tested:**
  - **Incompatible dimensions for addition:**  
    Input: Matrix A is 2x2, Matrix B is 1x2  
    Output: `Error: Incompatible dimensions for addition! Cannot add 2x2 and 1x2.`
  - **Incompatible dimensions for multiplication:**  
    Input: Matrix A is 2x2, Matrix B is 1x3 (columns of A = 2, rows of B = 1)  
    Output: `Error: Cannot multiply! Columns of first matrix (2) != Rows of second matrix (1).`
  - **Non-square matrix for determinant:**  
    Input: Matrix of size 2x3  
    Output: `Error: Matrix is not square (2x3), determinant cannot be calculated!`

---

## Instructions to Run

```bash
# Navigate to Lab2 directory
cd Lab2

# Run Program 1
python array_1d_operations.py

# Run Program 2
python array_2d_operations.py

# Run Program 3
python sparse_matrix_operations.py

# Run Program 4
python matrix_calculator.py
```
