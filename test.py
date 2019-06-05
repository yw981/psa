import numpy as np
import matplotlib.pyplot as plt

a = np.load('out_cam/2007_000032.npy')
print(type(a))
# a = np.array(a)
# print(a)
data = a.item()
print(type(data))

for k, v in data.items():
    print(type(v))
    print(str(k) + " : " + str(v.shape))
    plt.imshow(v)
    plt.show()
