import numpy as np
from matplotlib import pyplot as plt

# 简单的画图
# plt.plot([1, 2, 3, 4])
# plt.show()

# 图形颜色
# plt.plot([1, 3, 4], color = 'r')
# plt.plot([1, 2, 3], color = (1, 0, 1))
# plt.show()

# 图形样式
# plt.plot(plot[1, 2, 3, 4], linestyle = "--")
# plt.show()

# 标记样式
# plt.plot([1, 2, 3], marker = "o")
# plt.show()

# 标题、轴标题
# plt.title("D4")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()

# 图形范围，两种等价
# plt.axis([0, 5, 2, 20])
# plt.xlim([0, 35])
# plt.ylim([0, 20])
# plt.show()

# 图例
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label = 'label')
# plt.legend()
# plt.show()

# 文本
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro', label = 'label')
# plt.text(2, 2, 'First')
# plt.text(3, 3, 'Second')
# plt.show()

# 网格
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro', label = 'label')
# plt.grid(True, linestyle = '--', color = 'r', alpha = 0.5)
# plt.show()

# 刻度
# value = [1.5, 2.5, 3.5, 4.5]
# label = ['aa', 'bb', 'cc', 'aa']
# plt.xticks(value, label)
# plt.show()

# 线性图
# x = np.arange(0, 10, 0.3)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

# 直方图
# pop = np.random.randint(0, 100, 100)
# plt.hist(pop, bins = 20)
# plt.show()

# 条形图
# index = [1, 2, 3, 4]
# value = [2, 3, 4, 5]
# plt.bar(index, value)
# plt.show()

# 水平条形图
# index = [1, 2, 3, 4]
# value = [2, 3, 4, 5]
# plt.barh(index, value)
# plt.show()

# 饼图
# label = ["1a", "2b", "3c"]
# value = [19, 20, 50]
# color = ['yellow', 'green', 'red']
# plt.pie(value, labels = label, colors = color)
# plt.axis('equal')
# plt.show()

# 等值画图
# def f(x, y):
#     return (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#
# x = np.arange(-2.0, 2.0, 0.01)
# y = np.arange(-2.0, 2.0, 0.01)
# X, Y = np.meshgrid(x, y)
# C = plt.contour(X, Y, f(X, Y), 8, colors = 'black')
# plt.contourf(X, Y, f(X, Y), 8)
# plt.clabel(C, inline = 1, fontsize = 10)
# plt.show()

# 3D绘图（有错误）
# from mpl_toolkits.mplot3d import Axes3D
# def f(x, y):
#     return (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-2, 2, 0.1)
# Y = np.arange(-2, 2, 0.1)
# X, Y = np.meshgrid(X, Y)
# ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1)
# plt.show()

