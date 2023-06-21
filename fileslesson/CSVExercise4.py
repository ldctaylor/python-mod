import csv
import os

#reset the command prompt before running, just for neatness
os.system("clear")
galaxies = []
with open("galaxies.csv") as my_file: #use with to prevent data leakage - file closes after
    galaxies = list(csv.reader(my_file)) #create a reader object

for index in range(len(galaxies)):
    for galaxy in range(2):
        galaxies[index][galaxy] = int(galaxies[index][galaxy])

velocities = [_[1] for _ in galaxies]
#Calculate index posiiton of the minimum velocity galaxy and retrieve galaxy name(number) from galaxies list (index 0 for each element)
min_galaxy_name = galaxies[velocities.index(min(velocities))][0]
#Retrieve the galaxy velocity of lowest velocity
min_galaxy_velocity = galaxies[velocities.index(min(velocities))][1]

#find maximums
#Calc index position of the max vel galaxy and retrieve galaxy name from galaxies list
max_galaxy_name = galaxies[velocities.index(max(velocities))][0]
#retrieve galaxy velocity of the max velocity
max_galaxy_velocity = galaxies[velocities.index(max(velocities))][1]

print(f"Galaxy {min_galaxy_name} has the min velocity of {min_galaxy_velocity}km/sec.\nGalaxy {max_galaxy_name} has the max velocity of {max_galaxy_velocity}km/sec.")
