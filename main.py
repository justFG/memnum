def gauss_jordan(A, b):
    n = len(A)

    for k in range(n):
        pivot = A[k][k]
        for j in range(k, n):
            A[k][j] /= pivot
        b[k] /= pivot

        for i in range(n):
            if i != k:
                factor = A[i][k]
                for j in range(k, n):
                    A[i][j] -= factor * A[k][j]
                b[i] -= factor * b[k]

    return b

if __name__ == "__main__":
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    solution = gauss_jordan(A, b)
    print("Solution:", solution)
