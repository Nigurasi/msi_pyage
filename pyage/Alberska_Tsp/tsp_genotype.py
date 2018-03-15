import numpy as np


class Genotype(object):
    def __init__(self, points):
        self.points = points
        self.number_of_points = len(points)

        self.way = []
        for p in range(self.number_of_points):
            self.way.append(p)
        np.random.shuffle(self.way)

        self.fitness = None

    def __str__(self):
        return "Way: " + str(self.way) + "; fitness: " + str(self.fitness)

    def set_new_way(self, way):
        self.way = way[:]
