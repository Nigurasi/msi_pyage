import numpy as np

rand_x = np.random.sample(20) * 200
rand_y = np.random.sample(20) * 200

with open("points.csv", "w") as f:
    f.write("Name,x,y\n")
    for point in range(20):
        f.write(str(point) + "," + str(int(rand_x[point])) + "," + str(int(rand_y[point])) + "\n")