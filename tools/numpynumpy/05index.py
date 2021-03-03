import numpy as np

# 定义测试数据
A = np.arange(12)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
B = A.reshape((3,4))
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

# 一维索引
cell = A[3]
# 3

# 二维索引
## 取一个值
cell = B[2][3]
# 11
# 或
cell = B[2,3]
# 11

## 取一行
sub = B[2]
# [ 8  9 10 11]
# 等价于
sub = B[2,:]
# [ 8  9 10 11]

## 取一列，其中':'表示取全部
sub = B[:,2]
# [ 2  6 10]
# 或者
sub = B.T[2]    # 取列即取转置后的行
# [ 2  6 10]

# 二维中的切片
## 取n行
sub = B[1:3]    # 含首不含尾
# [[ 4  5  6  7]
#  [ 8  9 10 11]]
## 取n列
sub = B[:,1:3]
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]]

# 迭代获取
## 迭代取行
for row in B:
    print(row)
# [0 1 2 3]
# [4 5 6 7]
# [ 8  9 10 11]
## 迭代取列
for col in B.T:
    print(col)
# [0 4 8]
# [1 5 9]
# [ 2  6 10]
# [ 3  7 11]
## 迭代取出所有元素
# B.flatten()=B.reshape((1,-1))[0]  # 相当于取所有元素生成一行的行向量
_B = B.flatten()
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
for element in B.flat:
    print(element)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
