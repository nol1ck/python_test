import random
import numpy

numbers = lambda: list(numpy.random.randint(2000, 5000, 30))
numbers_list = lambda: list(random.randint(1000, 5000) for _ in range(30))
celeron = [i for i in numbers() if i < 3000]
core3 = [i for i in numbers() if (3000 < i < 4000)]
core5 = [i for i in numbers() if i > 4000]


frequency = [1000, 1400, 1700, 2200, 2800, 3200, 3500, 3700, 4000, 4300, 4600, 4800, 5000, 5100]

duron = [item for item in frequency if item <= 1500]
sempron = [item for item in frequency if 1500 < item <= 2500]
athlon = [item for item in frequency if 2500 < item <= 3500]
ryzen = [item for item in frequency if item > 3500]
print(ryzen)
