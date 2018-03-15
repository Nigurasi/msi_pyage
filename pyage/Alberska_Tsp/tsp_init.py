import numpy

from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.core.inject import Inject
from pyage.Alberska_Tsp.point_class import Point
from pyage.Alberska_Tsp.tsp_genotype import Genotype


class EmasInitializer(object):

    def __init__(self, filename, energy, size):
        self.points = generate_points(filename)
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(Genotype(self.points), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


def generate_points(filename):
    with open(filename, "r") as f:
        points = f.readlines()
        points = points[1:]

    point_list = []
    for p in points:
        name, x, y = p.split(",")
        point = Point(name, x, y)
        point_list.append(point)
    return point_list


class PointsInitializer(Operator):
    def __init__(self, population_size, filename):
        super(PointsInitializer, self).__init__(Genotype)
        self.population_size = population_size

        self.points = generate_points(filename)
        self.population = []

        for _ in range(self.population_size):
            self.population.append(Genotype(self.points))

    def __call__(self):
        return self.population

    def process(self, population):
        for i in range(self.population_size):
            population.append(self.population[i])
