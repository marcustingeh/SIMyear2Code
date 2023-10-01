import sqlite3
import os
import pandas as pd

#Change directory
os.chdir("C:/Users/xavie/OneDrive/Desktop/Rstudio files/dataverse_files")

try:
    os.remove('airlinespyder.db')
except OSError:
    pass

#Create database for sypder
conn=sqlite3.connect('airlinespyder.db')

c = conn.cursor()
conn.commit()
planedata = pd.read_csv("plane-data.csv")
data7 = pd.read_csv("2007.csv")
data8 = pd.read_csv("2008.csv")

data78 = data7.merge(data8,how='outer')
data78.to_sql('data78', con = conn, if_exists = 'append', index = False)
conn.commit()

planedata.to_sql('planedata', con=conn, if_exists ='append', index = False)
conn.commit()

c.execute('''
SELECT model AS model, AVG(data78.DepDelay+data78.ArrDelay+data78.CarrierDelay+data78.WeatherDelay+data78.NASDelay+data78.SecurityDelay+data78.LateAircraftDelay) AS avg_delay, planedata.year AS year
FROM planedata JOIN data78 USING(tailnum)
WHERE data78.Cancelled = 0 AND data78.Diverted = 0 AND planedata.year > 1900
GROUP BY model
ORDER BY year
''')

print(c.fetchall()[0], "- Represents the average delay of the oldest model")


c.execute('''
SELECT model AS model, AVG(data78.DepDelay+data78.ArrDelay+data78.CarrierDelay+data78.WeatherDelay+data78.NASDelay+data78.SecurityDelay+data78.LateAircraftDelay) AS avg_delay, planedata.year AS year
FROM planedata JOIN data78 USING(tailnum)
WHERE data78.Cancelled = 0 AND data78.Diverted = 0 AND planedata.year > 1900 AND planedata.year != 'None'
GROUP BY model
ORDER BY year DESC
''')

print(c.fetchall()[0], "- Represents the average delay of the newest model")

conn.close()
