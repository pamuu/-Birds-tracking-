# -Birds-tracking-
One fascinating area of research uses GPS to track the movements of animals. It is now possible to manufacture a small GPS device that is solar charged, so you don’t need to change batteries and use it to track flight patterns of birds. 
The data for this case study comes from the LifeWatch INBO project. Several data sets have been released as part of this project. We will use a small data set that consists of migration data for three gulls named Eric, Nico, and Sanne. The official_datasets; used dataset – CSV”>csv file contains eight columns and includes variables like latitude, longitude, altitude, and time stamps. In this case study, we will first load the data, visualize some simple flight trajectories, track flight speed, learn about daytime, and much, much more.

Aim: Track the movement of three gulls namely – Eric, Nico & Sanne
Dataset: official_datasets; used dataset – csv 
Dependencies: Matplotlib, Pandas, Numpy, Cartopy, Shapely
Repository(Github): source code 
(check the repository for the documentation of source code.) 
Writeup: explanation(.pdf)

We will divide our case study into five parts: 
1. Visualizing longitude and latitude data of the gulls. 
2. Visualize the variation of the speed of the gulls. 
3. Visualize the time required by the gulls to cover equal distances over the journey. 
4. Visualize the daily mean speed of the gulls. 
5. Cartographic view of the journey of the gulls.

PART (1/5): Latitude and Longitude 
In this part, we are going to visualize the location of the birds. We are going to plot latitude and longitude along the y and x-axis respectively and visualize the location data present in the csv file. 
