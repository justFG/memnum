#include <iostream>
using namespace std;

const int N = 3;

void gauss_jordan(float A[N][N], float b[N], float result[N]) {
    float tempA[N][N];
    float tempB[N];

    for (int i = 0; i < N; i++) {
        tempB[i] = b[i];
        for (int j = 0; j < N; j++)
            tempA[i][j] = A[i][j];
    }

    for (int k = 0; k < N; k++) {
        float pivot = tempA[k][k];

        for (int j = k; j < N; j++)
            tempA[k][j] /= pivot;
        tempB[k] /= pivot;

        for (int i = 0; i < N; i++) {
            if (i != k) {
                float factor = tempA[i][k];
                for (int j = k; j < N; j++)
                    tempA[i][j] -= factor * tempA[k][j];
                tempB[i] -= factor * tempB[k];
            }
        }
    }

    for (int i = 0; i < N; i++)
        result[i] = tempB[i];
}

int main() {
    float A[N][N] = {
        {2, 1, -1},
        {-3, -1, 2},
        {-2, 1, 2}
    };
    float b[N] = {8, -11, -3};
    float solution[N];

    gauss_jordan(A, b, solution);

    // Print the solution
    cout << "Solution: ";
    for (int i = 0; i < N; i++)
        cout << solution[i] << " ";
    cout << endl;

    return 0;
}
