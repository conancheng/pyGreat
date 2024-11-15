import numpy as np

a1 = np.array(np.arange(10, 70, 10).reshape((2,3)))
# [[10 20 30]
#  [40 50 60]]
a2 = np.array(np.arange(6).reshape((2,3)))
# [[0 1 2]
#  [3 4 5]]

# 矩阵减法：对应位相减
b = a1-a2
# [[10 19 28]
#  [37 46 55]]

# 矩阵加法：对应位相加
b = a1+a2
# [[10 21 32]
#  [43 54 65]]

# 矩阵乘法：对应位相乘
b = a1*a2
# [[  0  20  60]
#  [120 200 300]]

# 矩阵除法：对应位相除
b = a2/a1
# [[0.         0.05       0.06666667]
#  [0.075      0.08       0.08333333]]

# 以sin()为例
b = np.sin(a2)
# [[ 0.          0.84147098  0.90929743]
#  [ 0.14112001 -0.7568025  -0.95892427]]

# 乘方：各位分别乘方
b = a1**2
# [[ 100  400  900]
#  [1600 2500 3600]]

# 逻辑判断：各位进行判断，生成判断结果的列表
b = a1<30
# [[ True  True False]
#  [False False False]]

# 点乘
b = np.dot(a1, a2.reshape((3,2)))
# [[160 220]
#  [340 490]]
b = a1.dot(a2.reshape((3,2)))
# [[160 220]
#  [340 490]]

# # 求和
b = np.sum(a1)
# 210
# # 最小值
b = np.min(a1)
# 10
# # 最大值
b = np.max(a1)
# 60

# 最大值索引/最小值索引
print(np.argmax(a1))    # 5
print(np.argmin(a1))    # 0

# 平均值
b = np.mean(a1)        # 35.0
# 或
b = np.average(a1)     # 35.0
# 还可以通过矩阵A来调用
b = a1.mean()          # 35.0
# 没有a1.average()

# 中位数
b = np.median(a1)       # 35.0

# 逐个累加
b = np.cumsum(a1)
# [ 10  30  60 100 150 210]

# 逐个累减
b = np.ediff1d(a1)
# [10 10 10 10 10]  # 去掉了第一个，后面a(k)=a(k)-a(k-1)
b = np.diff(a1)
# [[10 10]      # 去掉了第一列，后面列a(k)=a(k)-a(k-1)
#  [10 10]]

# nonzero()：将所有非0元素的横纵坐标展开，所有横坐标生成一个数组，所有纵坐标生成一个数组
b = np.nonzero(a1)
# (array([0, 0, 0, 1, 1, 1], dtype=int64), array([0, 1, 2, 0, 1, 2], dtype=int64))

# sort排序（只进行行内排序）
b = np.sort(a1)
# [[10 20 30]
#  [40 50 60]]

# 转置
b = np.transpose(a1)
# [[10 40]
#  [20 50]
#  [30 60]]
# 或者
b = a1.T
# [[10 40]
#  [20 50]
#  [30 60]]

# clip(Array,Array_min,Array_max)大于max替换成max，小于min的替换成min
b = np.clip(a1, 20, 40)

print(b)
