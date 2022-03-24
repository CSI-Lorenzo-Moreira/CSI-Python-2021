planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print ("jump in a different planet calculator :OOOO")
jumplength = float(input("how long can you jump bro? (in inches viva la america)"))

planetinput = input(f"choose a planet from the given list: {planets}\n")
def calculatedweight(planet, mass): 
    print(f"you'r'é jump on earth is: {mass}")

    weightKG = mass/2.2046
    print(f"Mass in kg: {weightKG}")

    n_lb = 4.45
    
    planet_index = planets.index(planet)
    print (f"Your weight in {planets[planet_index]} is {(weightKG * gravity[planet_index]) / n_lb}") 

calculatedweight(planetinput, leweight)