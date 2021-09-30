per.nombre = "Pedro" # Esto no se recomienda
print(per.to_string())

per.estatura = 3.9
per.set_estatura(3.9)
print(per.to_string())

print("Estatura " , end = "")

print(per.get_estatura())

