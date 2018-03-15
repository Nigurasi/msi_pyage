import logging
import numpy as np

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.elect.el_init import root_agents_factory
from pyage.elect.el_selection import TournamentSelection
from pyage.elect.naming_service import NamingService
from pyage.Alberska_Tsp.tsp_crossover import Crossover
from pyage.Alberska_Tsp.tsp_evaluator import Evaluator
from pyage.Alberska_Tsp.tsp_init import EmasInitializer, PointsInitializer
from pyage.Alberska_Tsp.tsp_mutation import RandomOrderMutation, CutAndChangeMutation, MoveOneBackMutation

logger = logging.getLogger(__name__)

# parameters
if_EMAS = False
number_of_points = 10
population = 200
mut_probability = 1
mut_type = "CutAndChangeMutation"  # available: RandomOrderMutation, CutAndChangeMutation, MoveOneBackMutation
filename = "./pyage/Alberska_Tsp/points.csv"

if filename == "":
    rand_x = np.random.sample(20) * 200
    rand_y = np.random.sample(20) * 200

    with open("points.csv", "w") as f:
        f.write("Name,x,y\n")
        for point in range(20):
            f.write(str(point) + "," + str(int(rand_x[point])) + "," + str(int(rand_y[point])) + "\n")

agents_count = 10
stop_condition = lambda: StepLimitStopCondition(4500)

if if_EMAS:
    logger.debug("EMAS, %s agents", agents_count)
    agents = root_agents_factory(agents_count, AggregateAgent)
    agg_size = 40
    aggregated_agents = EmasInitializer(filename=filename, size=agg_size, energy=40)

    emas = EmasService

    minimal_energy = lambda: 10
    reproduction_minimum = lambda: 100
    migration_minimum = lambda: 120
    newborn_energy = lambda: 100
    transferred_energy = lambda: 40

    budget = 0
    evaluation = lambda: Evaluator()
    crossover = lambda: Crossover(size=30)

    if mut_type == "MoveOneBackMutation":
        mutation = lambda: MoveOneBackMutation(probability=mut_probability)
    elif mut_type == "RandomOrderMutation":
        mutation = lambda: RandomOrderMutation(probability=mut_probability)
    elif mut_type == "CutAndChangeMutation":
        print("CutAndChange")
        mutation = CutAndChangeMutation(probability=mut_probability)


    def simple_cost_func(x):
        return abs(x) * 10

else:
    logger.debug("Evolutionary algorithm, " + str(agents_count) + " agents")

    agents = generate_agents("agent", agents_count, Agent)

    size = 130

    if mut_type == "MoveOneBackMutation":
        operators = lambda: [Evaluator(), TournamentSelection(size=125, tournament_size=125),
                             Crossover(size=size), MoveOneBackMutation(probability=mut_probability)]
    elif mut_type == "RandomOrderMutation":
        operators = lambda: [Evaluator(), TournamentSelection(size=125, tournament_size=125),
                             Crossover(size=size), RandomOrderMutation(probability=mut_probability)]
    elif mut_type == "CutAndChangeMutation":
        operators = lambda: [Evaluator(), TournamentSelection(size=125, tournament_size=125),
                             Crossover(size=size), CutAndChangeMutation(probability=mut_probability)]

    initializer = lambda: PointsInitializer(population_size=population, filename=filename)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator
stats = lambda: StepStatistics('./pyage/Alberska_Tsp/Dane/Evolutionary_CutAndChange_1_10x200_4500iter.csv')

naming_service = lambda: NamingService(starting_number=2)
