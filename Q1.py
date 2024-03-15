from ACOGC import *

HyperParameters1 = {
    'filename': 'queen11.txt',
    'ub': 3,
    'Rho': 0.5,
    'Alpha': 2,
    'Beta' : 2,
    'Iterations': 30,
    'Antsize': 30
}

ACOGC1 = ACOGC(HyperParameters1)
ACOGC1.run()

HyperParameters2 = {
    'filename': 'le450.txt',
    'ub': 33,
    'Rho': 0.5,
    'Alpha': 2,
    'Beta' : 2,
    'Iterations': 10,
    'Antsize': 30
}

ACOGC2 = ACOGC(HyperParameters2)
ACOGC2.run()