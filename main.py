"""
This is the main file for the CPU Temperatures Project. 
It parses the txt file input, then formats the data to be used in future iterations of the program.

"""


import parse_temps
from temps_data import Dataset 


"""
Gets the users file then parses it and stores the information in a format that allows it to be used for 
Piecewise Linear Interpolation and Least Squares Approximation calculations. 

Args:
    file_name: the user's file name

    time_step: the time step in the users file
    temperatures: the temperatures in the users file

Yields:
    A dataclass object that stores the temperatures at each time for a given set of data in the users' file.

    ----->  Why a dataclass? It will be being used in both the calculations and is generally much easier to handle.
            It allows for quickly distinguishing datasets apart from eachother and calling information from them piece by piece
            rather than having all the information dumped if I ever need only segments of the information for future deployments.
"""

file_name = input().strip()
file_dataset = Dataset(file_name = file_name)
with open(file_name, "r", encoding="utf-8") as tmp_file:
    for time_step, temperatures in parse_temps.parse_raw_temps(tmp_file):
        file_dataset.intervals.append(time_step)
        file_dataset.intervaltemps[time_step] = temperatures


print(file_dataset)