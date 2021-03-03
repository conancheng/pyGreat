import numpy as np

# np.array()定义一个数组
a = np.array([2,23,4])
print(a)
# [ 2 23  4]

# dtype属性,指定数据类型
a = np.array([2,23,4],dtype=np.float)
# np.int32 np.float np.float32...
print(a)
# [ 2. 23.  4.]

# np.zeros()定义一个全0的数组
a = np.zeros((3,4)) # 数据全为0，3行4列
print(a)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# np.ones() # 定义一个全1的数组
a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列
print(a)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

# np.empty() # 定义一个全empty的数组
a = np.empty((3,4)) # 数据为empty，3行4列
print(a)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# 注：虽然显示的都是0，但实际上它们都是极小接近于0的数，并非真正的0

# 定义公差为2，[10,20)上的等差数组（注意是含首部不含尾部的）
a = np.arange(10,20,2) # 10-19 的数据，2步长
print(a)
# [10 12 14 16 18]

# reshape()改变形状
a = np.arange(12)
print(a)    # 默认形状1x：
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(a.reshape((3,4)))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(np.arange(12).reshape((2,-1)))    # 其中-1表示不对该维度做限定，程序处理的是多少就是多少
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

# np.linspace() # 定义均匀数组，不指定公差，指定总个数，程序算公差
a = np.linspace(1,10,20)    # 开始端1，结束端10，且均匀分割成20个数据，生成线段
print(a)
# [ 1.          1.47368421  1.94736842  2.42105263  2.89473684  3.36842105
#   3.84210526  4.31578947  4.78947368  5.26315789  5.73684211  6.21052632
#   6.68421053  7.15789474  7.63157895  8.10526316  8.57894737  9.05263158
#   9.52631579 10.        ]

np.random.seed(1)	# 传入一个int值，每次随机生成的数据都会是一样的
a=np.random.random()	# 生成0-1之间的随机小数
print(a)
# 0.417022004702574
a=np.random.random((2,4))	# 2*4的矩阵，每个值都是0-1之间的小数值
print(a)
# [[7.20324493e-01 1.14374817e-04 3.02332573e-01 1.46755891e-01]
#  [9.23385948e-02 1.86260211e-01 3.45560727e-01 3.96767474e-01]]