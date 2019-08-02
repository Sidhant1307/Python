import numpy as np
import matplotlib.pyplot as plt

N=10
nodes=np.round(1+(50-1)*np.random.random((N,2)))
print(nodes)


plt.plot(nodes[:,0],nodes[:,1],'go')

for i in range (10):
    plt.text(nodes[i,0],nodes[i,1],i)
plt.show()

plt.plot(nodes[:,0],nodes[:,1],'ko')
a = int(input('Enter the node==='))
print(nodes[a])
b= nodes[a]

for i in range (10):
    d = np.sqrt(np.square(b[0]-nodes[i,0]) + np.square(b[1]-nodes[i,1]))

    if (d<20 and d>0):
        plt.plot([b[0],nodes[i,0]],[b[1],nodes[i,1]],'r--')
        
plt.plot(b[0],b[1],'yo')
for i in range (10):
    plt.text(nodes[i,0],nodes[i,1],i)

plt.show()
