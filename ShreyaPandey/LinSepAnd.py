import numpy as np
import matplotlib as plt
x = np.array([0,1,0])
y = np.array([0,0,1])
plt.pyplot.scatter(x,y,c='red')
plt.pyplot.scatter(1,1,c="blue")
plt.pyplot.xlabel('Input 1')
plt.pyplot.ylabel('Input 2')
w=-1
b=1.5
x = np.linspace(0,1.5)
plt.pyplot.plot(x,w*x+b,c='black')
plt.pyplot.show()
