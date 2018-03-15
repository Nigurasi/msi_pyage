import random
from pyage.Alberska_Tsp.tsp_genotype import Genotype
from pyage.Alberska_Tsp.tsp_evaluator import Evaluator
from pyage.Alberska_Tsp.point_class import Point
p1 = Genotype([Point(0, 0, 1), Point(1, 2, 5), Point(2, 4, 2), Point(3, 6, 7), Point(4, 32, 11)])
p2 = Genotype([Point(0, 0, 1), Point(1, 2, 5), Point(2, 4, 2), Point(3, 6, 7), Point(4, 32, 11)])
p1.fitness = Evaluator().evaluate(p1)
p2.fitness = Evaluator().evaluate(p2)
print(p1)
print(p2)
parent1_way = list(p1.way)
parent2_way = list(p2.way)
number_of_points = p1.number_of_points

left = int(random.random() * (number_of_points - 1))
right = int(random.random() * (number_of_points - 1))
print(left)
print(right)
if left > right:
    left, right = right, left

parent1_way_leave = parent1_way[left:right]
print(parent1_way_leave)
for point in parent1_way_leave:
    parent2_way.remove(point)

child = Genotype(p1.points)
child.set_new_way(parent2_way + parent1_way_leave)

print(child)