import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
birdData = pd.read_csv("bird_tracking.csv")
# To get the unique names of the birds
birdNames = pd.unique(birdData.bird_name)
# To store the indices of the bird Eric
i = birdData.bird_name == "Eric"
x,y = birdData.longitude[i], birdData.latitude[i]
# Create a new figure, or activate an existing figure
plt.figure(figsize = (4.5,6))
plt.plot(x,y,"b.")
#plot each bird in the same figure
plt.figure(figsize = (4.5,6))
# plot latitude & longitude the graph
for name in birdNames:
            i = birdData.bird_name == name
            x,y = birdData.longitude[i], birdData.latitude[i]
            plt.plot(x,y,".", label=name)
# Labelling latitude & logitude
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.text(-6.00,33.44,"eric",color='blue',url='https://www.sonomabirding.com/birds-that-start-with-e/')
plt.text(-5.84,40.08,"Nico",color='orange',url='http://www.google.com')
plt.text(-11.62,32.89,"sanne",color='green',url='http://www.google.com')
# To get the timestamps of the day
timestamps = []
for k in range(len(birdData)):
            timestamps.append(datetime.datetime.strptime(birdData.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
birdData["timestamp"] = pd.Series(timestamps, index = birdData.index)
data = birdData[birdData.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time-times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)
# To find the mean speed zswszwxd
next_day =1 
inds = [] 
daily_mean_speed = [] 
for (i,t) in enumerate(elapsed_days):
            if t < next_day:
                        inds.append(i)
            else:
                        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
                        next_day += 1
                        inds = []
# For plotting the graph and labelling
plt.figure(figsize = (5,6))
plt.plot(daily_mean_speed, "rs-")
plt.xlabel(" Day ")
plt.ylabel(" Mean Speed (m/s) ");
# Display all open figures 
plt.show()
