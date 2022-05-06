import random
import numpy

numbers = lambda: list(numpy.random.randint(2000, 5000, 30))
numbers_list = lambda: list(random.randint(1000, 5000) for _ in range(30))
celeron = [i for i in numbers() if i < 3000]
core3 = [i for i in numbers() if (3000 < i < 4000)]
core5 = [i for i in numbers() if i > 4000]



print(core5)
