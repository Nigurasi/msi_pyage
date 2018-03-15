import logging
import random

from pyage.core.operator import Operator
from pyage.Alberska_Tsp.tsp_genotype import Genotype


logger = logging.getLogger(__name__)


class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)


class Crossover(AbstractCrossover):
    def __init__(self, size):
        super(Crossover, self).__init__(Genotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing\n\t" + str(p1) + "\nand\n\t" + str(p2))

        parent1_way = list(p1.way)
        parent2_way = list(p2.way)
        number_of_points = p1.number_of_points

        left = int(random.random() * (number_of_points - 1))
        right = int(random.random() * (number_of_points - 1))
        if left > right:
            left, right = right, left

        parent1_way_leave = parent1_way[left:right]
        for point in parent1_way_leave:
            parent2_way.remove(point)

        child = Genotype(p1.points)
        child.set_new_way(parent2_way + parent1_way_leave)

        logger.debug("A child was created: " + str(child))
        return child
