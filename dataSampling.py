import csv
import plotly.figure_factory as pf
import pandas as pd
import statistics
import random
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
print("Mean: ",mean)
result = []
count = []
for i in range(0,100):
    number = random.randint(30,len(data))
    value = data[number]
    result.append(value)
    count.append(i)
#mean
fig = pf.create_distplot([result],["Reading Time"],show_hist = False)
fig.show()