# cuenta-elementos-de-lista-1.py

cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras] # a list comprehension

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))