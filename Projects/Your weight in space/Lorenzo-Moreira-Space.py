planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print ("Weight in a different planet calculator :OOOO")
leweight = float(input("how much do you weigh? (in pounds viva la america)"))

planetinput = input(f"choose a planet from the given list: {planets}\n")
def calculatedweight(planet, mass): 
    print(f"your mass on earth is: {mass}")

    weightKG = mass/2.2046
    print(f"Mass in kg: {weightKG}")

    n_lb = 4.45
    
    planet_index = planets.index(planet)
    print (f"Your weight in {planets[planet_index]} is {(weightKG * gravity[planet_index]) / n_lb}") 

calculatedweight(planetinput, leweight) 

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
# print ("check out this sick space weight calculator bro :OOO")
# weightinput = float(input("how much do you weigh bro? (in pounds viva la america): "))
# print (planets)
# mass_kg = weightinput / 2.205
# planetinput = input("choose one of the main 8 planets from our solar system: ") 
# print ("your mass on earth is: ")


