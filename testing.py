planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print ("calculate your weight in a different planet of our solar system")
myWeight = float(input("what is your weight (pounds)? "))

myPlanet = input(f"select a planet from the list: {planets}\n")
def CalculatedWeight(planet,mass):
    print(f"earth mass in pounds is: {mass}")

    w_kg = mass/2.2046
    print(f"Mass in kg: {w_kg}")

    n_lb = 4.45

    planet_index = planets.index(planet)
    print(f"Your weight in {planets[planet_index]} is {(w_kg * g_ms2[planet_index]) /n_lb}") 

CalculatedWeight(myPlanet, myWeight)

