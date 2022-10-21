# Pandas
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv("/Users/akshayvadnere/Desktop/MLCourse/PastHires.csv")
'''
print(df.head(10))
print(df.columns)
print(df.tail())
print(df.shape)
print(df.size)
print(len(df))

print(df["Hired"])
print(df["Hired"][:5])
print(df["Hired"][5])
'''

df2 = df[["Years Experience", "Hired"]]
#print(df2)

df3 = df[["Years Experience", "Hired"]][:5]
#print(df3)

#print(df.sort_values(["Years Experience"]))
degree_counts = df["Years Experience"].value_counts()

plt.bar(degree_counts, height=20, width=2)
plt.show()
#degree_counts.plot(kind='bar')