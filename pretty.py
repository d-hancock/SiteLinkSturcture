import pandas as pd
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))

# create dataframe from outlinks csv

df_full_links = pd.read_csv("/Users/dale/PycharmProjects/SiteLinkSturcture/data/all_outlinks.csv",
                            names=["type", "source", "target", "size", "alt", "ancor", "status code", "status", "follow"])
df_full_links.head()
# clean first two rows
df_full_links = df_full_links.drop(df_full_links.index[[0, 1]])

# remove domain
df_full_links["source"] = df_full_links["source"].str[21:]
df_full_links["target"] = df_full_links["target"].str[21:]
df_full_links["group"] = df_full_links.np
#list of pages
pages = list(df_full_links.target.unique())




# create graph from edgelist dataframe

G = nx.from_pandas_edgelist(df_full_links, "from", "to", create_using=nx.Graph())

#create layout for nodes
layout = nx.spring_layout(G)

# Draw our relationships
# Sizes corespond to number of links
#color is type of page

link_number = [G.degree(page) * 50 for page in pages]
link_color =
nx.draw_networkx_nodes(G, layout,
                       nodelist=pages,
                       node_size=link_number,
                       node_color= 'lightblue')

#draw graph
nx.draw(G)
