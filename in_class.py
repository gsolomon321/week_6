# %%
# load libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# %%
# load data
help(pd.read_csv)
df = pd.read_csv("house_votes_Dem.csv", encoding = 'latin-1')

# %%
# take a look at the data
df.info()
df.head()
# %%
# separate out the numeric features
c_num = df[['aye', 'nay', 'other']]
#we do not need to standardize because the metric is the same
#though it is numerical, since this all the same scale, we do not need to do any conversion

# %%
# documentation for kmeans in sklearn
help(KMeans)

# %% build a kmeans model
kmeans = KMeans(n_clusters = 3, random_state = 42, verbose = 1)
#setting a seed, but it is setting it to the model,
#not the whole thing 

#initiation process, where the cluster is initiated
#it will randomize where the first centroid is, then it will probabilitically determine
#verbose = when the algoritm runs, it will tell you wants going on as its doing it 
#^compuationally lets you know whats going on
#class structures = a menu of items that we could just pick from

kmeans.fit(c_num)
#interia is the value measure that kmeans is trying to minimize -- all of this is the verbose

# %% look at the information in the model
print(kmeans.cluster_centers_)
print(kmeans.labels_)

# %%
# add the cluster labels to the original data frame
df['cluster'] = kmeans.labels_

# %%
inertias = []
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters = k, randomstate = 42)
    kmeans.fit(c_num)
    intertia.append(kmeans.intertia_)
help(KMeans)

# %% simple plot of the clusters
help(plt.scatter)
plt.figure(figsize = (10,5))
plt.plot(k_value, inertias, marker = 'o')
plt.xlabel('Number of Cluter (k)')
plt.ylabel('Inertia') 

#the more you know what is on the menu, the more ou understand 
#whats on the algorithm 
# %%