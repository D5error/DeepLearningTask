import skimage.data
from skimage import io
import matplotlib.pyplot as plt
from skimage.data import astronaut
img = io.imread('./whiteD5.png')


# 读入、存储、显示图片
# img = io.imread('./whiteD5.png')
# io.imshow(img)
# plt.show()
# io.imsave('./D5.png', img)
# image = skimage.data.astronaut()
# io.imshow(image)
# plt.show()

# 更改图像样式
# from skimage.color import rgb2gray, rgb2hsv
# imgNew = rgb2gray(astronaut())
# imgNew = rgb2hsv(astronaut())
# plt.subplot(1, 2, 1)
# io.imshow(astronaut())
# plt.subplot(1, 2, 2)
# io.imshow(imgNew)
# plt.show()

# 图像增强操作
# from skimage.transform import resize
# imgResized = resize(img, (1000, 500))
# plt.subplot(1, 2, 1)
# io.imshow(img)
# plt.subplot(1, 2, 2)
# io.imshow(imgResized)
# plt.show()
# from skimage.transform import rescale
# imgRescaled = rescale(img, scale=(0.2, 0.2)) # 有错误
# plt.subplot(1, 2, 1)
# io.imshow(img)
# plt.subplot(1, 2, 2)
# io.imshow(imgRescaled)
# plt.show()

# 旋转图像、翻转图像
# from skimage.transform import rotate
# imgRotated = rotate(img, angle=45, resize=True)
# io.imshow(imgRotated)
# plt.show()

# 改变图像亮度
from skimage import exposure
imgBright = exposure.adjust_gamma(img, gamma=0.5, gain=1)
imgDark = exposure.adjust_gamma(img, gamma=1.5, gain=1)
plt.subplot(1, 3, 1)
io.imshow(img)
plt.subplot(1, 3, 2)
io.imshow(imgBright)
plt.subplot(1, 3, 3)
io.imshow(imgDark)
plt.show()