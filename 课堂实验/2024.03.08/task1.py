import matplotlib.pyplot as plt
import numpy as np
import os
import skimage
import matplotlib.pyplot as plt

# 迭代器应用场景
path = './img' # 图片路径
img_names = os.listdir(path) # 获取所有图片的名称
flowers = [] # 保存图片的矩阵形式
for name in img_names:
    img = skimage.io.imread(path + "/" + name) # 根据路径读取图片，img为ndarray类型
    flowers.append(img)

num = 5
txt_names = ["./result" + str(i) + ".txt" for i in range(num)]

it = iter(flowers) # 生成迭代器
txtPaths = iter(txt_names)

for i in range(num): # 处理前num张图片
    img = next(it)
    img = skimage.color.rgb2gray(img)
    txtPath = next(txtPaths)
    np.savetxt(txtPath, img, fmt = '%f')

txtPaths = iter(txt_names)
for i in range(num):
    img = np.loadtxt(next(txtPaths), dtype = float)
    plt.imshow(img, cmap = 'gray')
    plt.show()

# 生成器应用场景