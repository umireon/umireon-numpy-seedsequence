import numpy as np
from numpy.random import SeedSequence

sq = SeedSequence(1)
s1, s2 = sq.generate_state(2, np.uint64)
print(s1, s2)
