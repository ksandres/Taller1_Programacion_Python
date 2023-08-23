print("Ingrese los sets de A:")
a = int(input())
print("Ingrese los sets de B:")
b = int(input())

if a < 0 or b < 0 or a >= 8 or b >= 8:
    print("Los valores ingresados son inválidos.")
elif a == 6 and b < 5:
    print("El set es de A.")
elif b == 6 and a < 5:
    print("El set es de B.")
elif (a == 7 and b < 7) or (b == 7 and a < 7):
    if a == 7:
        print("El set es de A")
    else:
        print("El set es de B")
elif a < 7 or b < 7:
    print("El set no ha terminado.")
