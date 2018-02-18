import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
'''
polygons = [Polygon([[510.66, 423.01], [511.72, 420.03], [510.45, 416], [510.34, 413.02], [510.77, 410.26], [510.77, 407.5], [510.34, 405.16], [511.51, 402.83], [511.41, 400.49], [510.24, 398.16], [509.39, 397.31], [504.61, 399.22], [502.17, 399.64], [500.89, 401.66], [500.47, 402.08], [499.09, 401.87], [495.79, 401.98], [490.59, 401.77], [488.79, 401.77], [485.39, 398.58], [483.9, 397.31], [481.56, 396.35], [478.48, 395.93], [476.68, 396.03], [475.4, 396.77], [473.92, 398.79], [473.28, 399.96], [473.49, 401.87], [474.56, 403.47], [473.07, 405.59], [473.39, 407.71], [476.68, 409.41], [479.23, 409.73], [481.56, 410.69], [480.4, 411.85], [481.35, 414.93], [479.86, 418.65], [477.32, 420.03], [476.04, 422.58], [479.02, 422.58], [480.29, 423.01], [483.79, 419.93], [486.66, 416.21], [490.06, 415.57], [492.18, 416.85], [491.65, 420.24], [492.82, 422.9], [493.56, 424.39], [496.43, 424.6], [498.02, 423.01], [498.13, 421.31], [497.07, 420.03], [497.07, 415.15], [496.33, 414.51], [501.1, 411.96], [502.06, 411.32], [503.02, 415.04], [503.33, 418.12], [501.1, 420.24], [498.98, 421.63], [500.47, 424.39], [505.03, 423.32], [506.2, 421.31], [507.69, 419.5], [506.31, 423.32], [510.03, 423.01], [510.45, 423.01]])]

fig = plt.figure()
ax = plt.gca()

img = plt.imread('/home/hans/Datasets/COCO/val2017/000000289343.jpg')
ax.imshow(img)

p = PatchCollection(polygons, facecolor='red', linewidths=0, alpha=0.4)
ax.add_collection(p)

p = PatchCollection(polygons, facecolor='none', edgecolors='blue', linewidths=2)
ax.add_collection(p)
'''
plt.plot([1.,2.], [2.,3.])
plt.show()
