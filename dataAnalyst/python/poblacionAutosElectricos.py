# Libraries
import json
import pandas as pd
import matplotlib.pyplot as plt

# import .csv in order
df = pd.read_csv('/media/fode/PRO TOOLS/dataSets/Electric_Vehicle_Population_Data.csv', sep=',')

"""
# print first 5 rows
print(df.head())

# shape of data
print(df.shape)

# column names list of data 
print(df.columns.tolist())

# summary of data
print(df.describe())
"""

"""
countModelYear = df.groupby("Model Year")["Model Year"].count()
# plot x-label years and y-label count
countModelYear.plot(kind="bar", title="Count of Model Year")
plt.show()
"""

"""
df1 = df[["Model Year","Make","Model"]]

model = df1.pivot_table(values = "Model", index=["Make"],columns="Model Year", aggfunc="count",fill_value="-",margins=True)
timeCar = model.sort_values("All",ascending=True)

# groupby model and make
groupModel = df.groupby(["Make","Model"])["Model"].count()
"""

dfgeo = df[["Make","Vehicle Location"]]

print(dfgeo["Vehicle Location"].head())


"""
dfgeo.plot(kind="scatter", x="Make", y="Vehicle Location", title="Make and Vehicle Location")
plt.show()
"""



























