import numpy as np

A = [1, 2, 3]
B = [4, 7, 9]

A = np.array(A)
B = np.array(B)

print(A + B)

m = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(m[0][1]) # 20
print(m[2][2]) # 90

n = np.array(m)

print(n[0, 1])
print(n[2, 2])

print(n + n)
print(2 * n)
