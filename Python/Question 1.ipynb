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

data7 = pd.read_csv("2007.csv")
data8 = pd.read_csv("2008.csv")

data78 = data7.merge(data8,how='outer')
data78.to_sql('data78', con = conn, if_exists = 'append', index = False)

conn.commit()

c.execute('''
SELECT deptime AS deptime, AVG(data78.DepDelay+data78.ArrDelay+data78.CarrierDelay+data78.WeatherDelay+data78.NASDelay+data78.SecurityDelay+data78.LateAircraftDelay) AS avg_delay
FROM data78
WHERE data78.Cancelled = 0 AND data78.Diverted = 0
GROUP BY deptime
ORDER BY avg_delay
''')

print(c.fetchone()[0], "hrs is the best time of day to fly with minimal delay")


c.execute('''
SELECT dayofweek AS dayofweek, AVG(data78.DepDelay+data78.ArrDelay+data78.CarrierDelay+data78.WeatherDelay+data78.NASDelay+data78.SecurityDelay+data78.LateAircraftDelay) AS avg_delay
FROM data78
WHERE data78.Cancelled = 0 AND data78.Diverted = 0
GROUP BY dayofweek
ORDER BY avg_delay
''')

print(c.fetchone()[0], "is the best day of the week to fly with minimal delay.")

c.execute('''
SELECT year AS year, AVG(data78.DepDelay+data78.ArrDelay+data78.CarrierDelay+data78.WeatherDelay+data78.NASDelay+data78.SecurityDelay+data78.LateAircraftDelay) AS avg_delay
FROM data78
WHERE data78.Cancelled = 0 AND data78.Diverted = 0
GROUP BY year
ORDER BY avg_delay
''')

print(c.fetchone()[0], "is the best year to fly with minimal delay.")


conn.close()
