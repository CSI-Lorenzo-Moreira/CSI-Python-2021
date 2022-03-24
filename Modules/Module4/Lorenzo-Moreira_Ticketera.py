print ("Bienvenido a  Miss Mundo 2021")
print ("El precio de cada taquilla es: Nivel Superior = $50.00. Nivel Princpal = $150.00, Club Seat= $350.00")
clubseat = int(input('Inserte la cantidad de taquillas "clubseat" deseadas: '))
nivelprincipal = int(input("Inserte la cantidad de taquillas de Nivel Principal deseadas: "))
nivelsuperior = int(input("Inserte la cantidad de taquillas de Nivel Superior: "))

def ventas(Club_Seat, Nivel_Principal, Nivel_Superior):
    print(f"El costo de las taquillas club seat sera: {float(clubseat)*350.00}")
    print(f"El costo de las taquilals de nivel principal sera:  {float(nivelprincipal)*150.00}")
    print(f"El costo de las taquillas de nivel suerior sera: {float(nivelsuperior)*50.00}")
print()
ventas(nivelsuperior, nivelprincipal, clubseat)
ventas_nivelsuperior = nivelsuperior * 50.00
ventas_nivelprincipal = nivelprincipal * 150.00
ventas_clubseat = clubseat * 350.00

def taquillastotal(ventas_nivelsuperior, ventas_nivelprincipal, ventas_clubseat):
    print(f"El total sera: ${float(ventas_nivelsuperior) + float(ventas_nivelprincipal) + float(ventas_clubseat)}")
print()
taquillastotal(ventas_nivelsuperior, ventas_nivelprincipal, ventas_clubseat) 