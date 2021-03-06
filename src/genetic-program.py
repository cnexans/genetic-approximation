from numpy import linspace, sum, absolute
from math import log
from population import Population, PopulationProperties
from program_trees import IfWrapper, MultiplicationWrapper, AdditionWrapper, IsGreaterWrapper
from environment import Environment, EnvironmentProperties
from program_evolution import Evolution, EvolutionProperties

target_function = lambda x: float(x**2 + 2*x + 1)
create_training_set = lambda P: [(x, P(x)) for x in linspace(-50, 50)]
training_set = create_training_set(target_function)

def compute_function_score(training_set, evaluable_tree):
    evalue_tree = lambda x: evaluable_tree.evaluate([x])
    errors = [absolute(evalue_tree(x) - y) for (x, y) in training_set]
    return sum(errors)

population_size = 100
function_wrappers = [MultiplicationWrapper, AdditionWrapper]

polynomial_population_properties = PopulationProperties()

polynomial_population = Population(
    function_wrappers,
    population_size,
    polynomial_population_properties
)

environment_properties = EnvironmentProperties(
    fitness_function = lambda tree: compute_function_score(training_set, tree),
    population = polynomial_population
)

environment = Environment(environment_properties)

environment.evolve()