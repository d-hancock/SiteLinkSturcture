import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))

# create dataframe from outlinks csv

df_full_links = pd.read_csv("/Users/dale/PycharmProjects/SiteLinkSturcture/data/all_outlinks.csv",
                            names=["type", "from", "to", "size", "alt", "ancor", "status code", "status", "follow"])
df_full_links.head()
# clean first two rows
df_full_links = df_full_links.drop(df_full_links.index[[0, 1]])

# remove domain
df_full_links["from"] = df_full_links["from"].str[21:]
df_full_links["to"] = df_full_links["to"].str[21:]

# create edgelist representation of graph

G = nx.from_pandas_edgelist(df_full_links, "from", "to", create_using=nx.MultiDiGraph())

#draw graph
nx.draw(G)

plt.show()