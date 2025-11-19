def gauss_jordan(A, b):
    """
    Solve linear system Ax = b using Gauss-Jordan elimination.
    Args:
        A: square matrix as a list of lists
        b: vector as a list
    Returns:
        solution vector
    """
    n = len(A)

    # Make a copy to preserve originals
    A_copy = [row[:] for row in A]
    b_copy = b[:]

    for k in range(n):
        pivot = A_copy[k][k]

        # Normalize pivot row
        for j in range(k, n):
            A_copy[k][j] /= pivot
        b_copy[k] /= pivot

        # Eliminate other rows
        for i in range(n):
            if i != k:
                factor = A_copy[i][k]
                for j in range(k, n):
                    A_copy[i][j] -= factor * A_copy[k][j]
                b_copy[i] -= factor * b_copy[k]

    return b_copy

if __name__ == "__main__":
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    solution = gauss_jordan(A, b)
    print("Solution:", solution)
