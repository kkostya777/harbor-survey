

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [100,200,300,400,500]

plt.barh(x,y, color='purple', label='The Label for Legend')
plt.title ('bar chart')
plt.xlabel('Xlabel')
plt.ylabel('Y label')
plt.legend(facecolor='gray', shadow=True)
plt.figtext(.5,.7, 'stuff', color='black')
plt.show()
