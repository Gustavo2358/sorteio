from random import randint, shuffle

povo = ["Gustavo Oliveira", "Gustavo Silva", "Cinthia", "Gustavo Olmos", "Gabi", "Gabgol", 
        "Larissa", "Nicolau", "Raphael"]

shuffle(povo)

grupo1 = povo[0:5]
grupo2 = povo[5:9]

print("grupo1")

for pessoa in grupo1:
    print(f"    -{pessoa}")

print("grupo2")
for pessoa in grupo2:
    print(f"    -{pessoa}")
