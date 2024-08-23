import numpy as np
import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a raccoon!
from PIL import Image  # for reading image files

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])


print(mystery_array[2,1,3])
# 18

print(mystery_array[2,1,:])
# [97 0 27 18]

# print(mystery_array[[(0,0),(0,1)], [(1,0),(1,1)], [(2,0),(2,1)]])

result = np.array([
    [mystery_array[0, 0, 0], mystery_array[0, 1, 0]],  # [0, 4]
    [mystery_array[1, 0, 0], mystery_array[1, 1, 0]],  # [7, 5]
    [mystery_array[2, 0, 0], mystery_array[2, 1, 0]]   # [5, 97]
])

print(result)

# OR you can do this:
# All the first elements on axis number 3
print(mystery_array[:, :, 0])