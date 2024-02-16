import matplotlib.pyplot as plt
plt.title('My First Matplotlib Plot')

# 添加轴标签
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

x=[1,3,5,7,9]
y=[2,4,6,8,10]
plt.plot(x,y)
# 添加图例
plt.legend(['Line A'])

# 显示图表
plt.show()