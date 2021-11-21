
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
X_axis = np.array([1,600,50,500,7.5,650])
Y_axis = np.array([7,45,75,5,50,100])
plt.title('Tax Rate')
plt.xlabel('Taxes')
plt.ylabel('Income')
plt.plot(X_axis,  marker = '*', ls = '-', color='g')
plt.plot(Y_axis,'o:', linewidth='3.5')
plt.grid(axis = 'y', ls = '--', color = 'g')
plt.show()