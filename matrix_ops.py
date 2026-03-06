def matrix_add(matrix_a, matrix_b):
    """Add two matrices element-wise using nested list comprehension."""
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    
    return [[a + b for a, b in zip(row_a, row_b)] 
            for row_a, row_b in zip(matrix_a, matrix_b)]


def matrix_transpose(matrix):
    """Transpose a matrix using zip and list comprehension."""
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A, B):
    """Multiply two matrices using dot product logic with list comprehension."""
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError(f"Cannot multiply: A has {len(A[0])} columns, B has {len(B)} rows")
    
    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*B)]
            for row_a in A]

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
print(matrix_add(a,b))
print(matrix_transpose(a))
print(matrix_multiply(a,b))