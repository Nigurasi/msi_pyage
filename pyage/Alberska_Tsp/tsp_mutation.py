import logging
import random

from pyage.core.operator import Operator
from pyage.Alberska_Tsp.tsp_genotype import Genotype
from pyage.Alberska_Tsp.tsp_evaluator import Evaluator

logger = logging.getLogger(__name__)


class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)


class RandomOrderMutation(AbstractMutation):
    def __init__(self, probability):
        super(RandomOrderMutation, self).__init__(Genotype, probability)

    def mutate(self, genotype):
        logger.debug("Random order mutation of a genotype: " + str(genotype))

        new_genotype = Genotype(genotype.points)
        number_of_points = genotype.number_of_points
        number_of_swaps = int(random.random() * (number_of_points - 1) + 1)
        new_way = genotype.way[:]

        for n in range(number_of_swaps):
            indeks_1 = int(random.random() * (number_of_points - 1))
            indeks_2 = int(random.random() * (number_of_points - 1))
            new_way[indeks_1], new_way[indeks_2] = new_way[indeks_2], new_way[indeks_1]

        new_genotype.set_new_way(new_way)
        new_genotype.fitness = Evaluator().evaluate(new_genotype)

        logger.debug("New genotype after random order mutation: " + str(new_genotype))

        return new_genotype


class CutAndChangeMutation(AbstractMutation):
    def __init__(self, probability):
        super(CutAndChangeMutation, self).__init__(Genotype, probability)

    def mutate(self, genotype):
        logger.debug("Cut and change mutation of a genotype: " + str(genotype))

        number_of_points = genotype.number_of_points
        new_genotype = Genotype(genotype.points)
        point_of_division = int(random.random() * (number_of_points - 1))

        new_way_1 = genotype.way[:point_of_division + 1]
        new_way = genotype.way[point_of_division + 1:]
        new_way.extend(new_way_1)

        new_genotype.set_new_way(new_way)
        new_genotype.fitness = Evaluator().evaluate(new_genotype)

        logger.debug("New genotype after cut and change mutation: " + str(new_genotype))
        return new_genotype


class MoveOneBackMutation(AbstractMutation):
    def __init__(self, probability):
        super(MoveOneBackMutation, self).__init__(Genotype, probability)

    def mutate(self, genotype):
        logger.debug("Move One back mutation of genotype: " + str(genotype))

        number_of_points = genotype.number_of_points
        new_genotype = Genotype(genotype.points)

        new_way = []

        for p in range(1, number_of_points):
            new_way.append(genotype.way[p])
        new_way.append(genotype.way[0])

        new_genotype.set_new_way(new_way)
        new_genotype.fitness = Evaluator().evaluate(new_genotype)

        logger.debug("New genotype after move one back mutation: " + str(new_genotype))
        return new_genotype