import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json
# weapon = "AKMN"
# caliber = "7.62x39 mm"
# ammunition = "BP gzh"
# speed_ms = 730

# building = "Torre Norte"
# building_height = 243

# gravity = 9.81

import math

def projectilefunction(experimentalData: ExperimentalData):

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentalData.planet)

    time_s = math.sqrt((2 * experimentalData.building_height)/gravity[planet])
    distance_m = (experimentalData.speed_ms * time_s)
    print(f"The gun chosen was the {experimentalData.weapon}. It is an astounding assault riffle with an intermediate caliber of {experimentalData.caliber}. This one in particular will utilize {experimentalData.ammunition} type bullets. Utilizing this ammunition allows the rifle to shoot a bullet at a speed of {experimentalData.speed_ms} meters per second, and would take a time of {time_s} to reach the ground.")
# projectilefunction("AKMN", "7.62x39mm", "BP gzh", 730, "Torre Norte", 243, 9.81)

# experimentaldata = {
#     "weapon": "AKMN",
#     "caliber": "7.62x39 mm",
#     "ammunition": "BP gzh",
#     "speed_ms": 730,
#     "building": "Torre Norte",
#     "building_height":  243,
#     "gravity":  9.81
# }

mydataset = [
ExperimentalData("AKMN", "7.62x39mm", "HP", 730, "Torre Norte", 243, "Earth"),
ExperimentalData("AKMN", "7.62x39mm", "MAI AP", 730, "Torre Norte", 243, "Mars"),
ExperimentalData("AKMN", "7.62x39mm", "PS GZH", 730, "Torre Norte", 243, "Jupiter"),
ExperimentalData("AKMN", "7.62x39mm", "US GZH", 730, "Torre Norte", 243, "Venus")
]

for data in mydataset:
    print("\n-------------------------------------------\n")
    projectilefunction(data)

#serialization

myoutput = Path(__file__).parents[0]
myoutputfilepath = os.path.join(myoutput, 'Projectile-Motion.json')

print(myoutputfilepath)

with open(myoutputfilepath, 'w') as outfile:
    json.dump([data.__dict__ for data in mydataset], outfile)

