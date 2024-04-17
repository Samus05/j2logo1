
# mi solucion
palabras = input("ingresa palabras: ").upper()
arreglo = palabras.split(" ")
arreglo.sort()
texto = ""
for palabra in arreglo:
    texto += palabra + " "
print(' '.join(sorted(arreglo)))

# Solucion en solo 3 lineas
palabras = input("ingresa palabras: ").upper()
arreglo = palabras.split(" ")
print(' '.join(sorted(arreglo)))