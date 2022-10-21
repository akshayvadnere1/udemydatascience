import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(27000, 15000, 10000) # income, std dev, data points

#print(incomes.mean())
# print(np.mean(incomes))

plt.hist(incomes, 50)
#plt.show()

#print(np.median(incomes))
incomes = np.append(incomes, [1000000000])

#print(incomes.mean())

ages = np.random.randint(18, 90, 500)
print(stats.mode(ages))