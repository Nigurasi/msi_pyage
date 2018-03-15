import logging

from pyage.Alberska_Tsp.tsp_genotype import Genotype
from pyage.core.operator import Operator


logger = logging.getLogger(__name__)


class Evaluator(Operator):
    def __init__(self):
        super(Evaluator, self).__init__(Genotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        fitness = 0.0
        point = 1

        while point < genotype.number_of_points:
            x = int(genotype.points[genotype.way[point]].x) - int(genotype.points[genotype.way[point-1]].x)
            y = int(genotype.points[genotype.way[point]].y) - int(genotype.points[genotype.way[point-1]].y)
            fitness -= x ** 2 + y ** 2
            point += 1
        return fitness