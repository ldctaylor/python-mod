import csv
import os

#reset the command prompt before running, just for neatness
os.system("clear")

with open("galaxies.csv") as my_file: #use with to prevent data leakage - file closes after
    galaxies = csv.reader(my_file)
    min_galaxy_index, min_galaxy_velocity = next(galaxies)
    max_galaxy_index,max_galaxy_velocity = min_galaxy_index, min_galaxy_velocity
    min_galaxy_velocity = int(min_galaxy_velocity)
    max_galaxy_velocity = int(max_galaxy_velocity)
    for row in galaxies:
        if int(row[1]) < min_galaxy_velocity:
            min_galaxy_index = int(row[0])
            min_galaxy_velocity = int(row[1])
        if int(row[1]) > max_galaxy_velocity:
            max_galaxy_index = int(row[0])
            max_galaxy_velocity = int(row[1])

print(f"Galaxy {min_galaxy_index} has the min velocity of {min_galaxy_velocity}km/sec.\nGalaxy {max_galaxy_index} has the max velocity of {max_galaxy_velocity}km/sec.")
