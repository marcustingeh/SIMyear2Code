import os
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



#Change directory
os.chdir("C:/Users/xavie/OneDrive/Desktop/Rstudio files/dataverse_files")

data7 = pd.read_csv("2007.csv")
data8 = pd.read_csv("2008.csv")

data78 = data7.merge(data8,how='outer')

data78['TotalDelay']=data78['DepDelay']+data78['CarrierDelay']
+data78['WeatherDelay']+data78['NASDelay']+data78['SecurityDelay']

data78['TF'] = np.where(data78['TotalDelay'] >0, 1,0)
data78 = data78.drop(['Year','Month','DayofMonth','DayOfWeek','DepTime','ArrTime','CRSArrTime','UniqueCarrier','FlightNum','TailNum','ActualElapsedTime','CRSElapsedTime','AirTime','ArrDelay','DepDelay','Distance','TaxiIn','TaxiOut','Cancelled','CancellationCode','Diverted','CarrierDelay','WeatherDelay','NASDelay','SecurityDelay','LateAircraftDelay','TotalDelay','CRSDepTime'],axis=1)
G = nx.Graph()

for index, row in data78.iterrows():
    G.add_edge(row['Origin'], row['Dest'], weight=row['TF'])

# remove isolated vertices (if any)    
remove = [node for node,degree in G.degree() if degree ==0]
G.remove_nodes_from(remove)

#Setting size and colours
options = {
     'node_color': 'lightblue',
     'edge_color': 'lightblue',
     'node_size': 1,
     'width': 1,
     'alpha': 1.0}

plt.subplots(figsize=(5,5))
pos=nx.circular_layout(G)
nx.draw(G,pos=pos,font_size=9,**options)
nx.draw_networkx_labels(G,pos=pos,font_size=9)
plt.tight_layout()
plt.axis('off');
plt.show()
