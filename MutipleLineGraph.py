import matplotlib.pyplot as plt
x = [1,2,3,4, 5]
y1 = [2,3,5,7, 11]
y2 = [1,4,6,8, 10]
plt.plot(x, y1,label='Line 1' , marker='o')
plt.plot(x, y2,label='Line 2' , marker='s')
plt.title('Mutiple Line Graphs')
plt.xlabel('X-axis')
plt.xlabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()


