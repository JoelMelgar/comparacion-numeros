from io import open
archivo_texto=open("salida.txt" , "a")

n1 = float(input("Inserte el primer Numero: "))
n2 = float(input("Inserte el segundo numero: "))
n3 = float(input("Inserte el tercer Numero: "))

if n1 == n2 == n3:
    print("Todos son los numeros son iguales: ", str(int(n1)) + ", " + str(int(n2)) + ", " + str(int(n3)))
    archivo_texto.write("Todos son los numeros son iguales: " + str(n1) + ", " + str(n2) + ", " + str(n3) + "\n")
elif n1 == n2:
    print("Hay dos numeros repetidos y el que no se repite es: ", str(int(n3)))
    archivo_texto.write("Hay dos numeros repetidos y el que no se repite es: " + str(n3) + "\n")
elif n1 == n3:
    print("Hay dos numeros repetidos y el que no se repite es: ", str(int(n2)))
    archivo_texto.write("Hay dos numeros repetidos y el que no se repite es: "+ str(n2) + "\n")
elif n2 == n3:
    print("Hay dos numeros repetidos y el que no se repite es: ", str(int(n1)))
    archivo_texto.write("Hay dos numeros repetidos y el que no se repite es: " + str(n1) + "\n")
else:
    if n2 < n1 > n3:
        suma = n1 + n2 + n3
        print("El numero mas grande es: " + str(int(n1)) + " y la suma de los 3 numeros es: ", suma)
        archivo_texto.write("El numero mas grande es: " + str(n1) + " y la suma de los 3 numeros es: " + str(suma) + "\n")
    elif n1 < n2 > n3:
        mult = n1*n2*n3
        print("El numero mas grande es: " + str(int(n2)) + " y Los multiplicacion de los numeros es: ", mult)
        archivo_texto.write("El numero mas grande es: " + str(n2) + " y Los multiplicacion de los numeros es: "+ str(mult) + "\n")
    elif n1 < n3 > n2:
        print("El numero mas grande es: " + str(int(n3)) + " y Los numeros concatenados son: ",
              str(int(n1)) + str(int(n2)) + str(int(n3)))
        archivo_texto.write("El numero mas grande es: " + str(n3) + " y Los numeros concatenados son: " +
                            str(int(n1)) + str(int(n2)) + str(int(n3)) + "\n")
archivo_texto.close()

