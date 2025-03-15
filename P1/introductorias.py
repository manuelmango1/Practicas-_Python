"""
1-Desarrolla un programa que solicite al usuario que ingrese su edad y luego
  calcule y muestre cuántos años le faltan para alcanzar los 100 años.
2-Haz un programa que pida al usuario que ingrese una temperatura en
  grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
  mostrando el resultado.
3-Crea un programa que calcule la suma de los primeros 100 números
  naturales utilizando un bucle for.
4-Cree un programa que dada una lista de números imprima sólo los que son
  pares. Nota: utilice la sentencia continue donde haga falta.
5-Implementa un programa que solicite al usuario que ingrese una lista de
  números. Luego, imprime la lista pero detén la impresión si encuentras un
  número negativo. Nota: utilice la sentencia break cuando haga falta.

"""
#1.
edad = int(input("Ingrese su edad: "))

print(f'Los anos que le faltan para llegar a los 100 son: {100-edad}')

#2.
formula_farenheit = float(9/5)
celsius = float(input("Ingrese el numero en grados celsius: "))
print(f'Los grados celsius ingresados ({celsius}), pasados a farenheit son: {(celsius * formula_farenheit + 32)} ')

#3.
sumaTotal = 0
for i in range(1,101):
  sumaTotal = sumaTotal + i

print(sumaTotal)
#4.
number_list = [1,2,3,4,5,6,7,8,9,10]
for i in number_list:
  if i % 2 == 0:
      print(i)
#5.