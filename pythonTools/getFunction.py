import numpy as np


def yValue(x, a, b, c):
    return a * x**2 + b * x + c
# 定义三个点的坐标
x = np.array([0, 1, 2])
y = np.array([1, 0, 1])

# 构建矩阵A和向量b
A = np.column_stack((x**2, x, np.ones_like(x)))
b = y

# 使用numpy的linalg.solve函数解方程组
coefficients = np.linalg.solve(A, b)

# 输出二次函数的系数
a, b, c = coefficients
print(f"The quadratic function is: y = {a}x^2 + {b}x + {c}")
print(yValue(3, a, b, c))