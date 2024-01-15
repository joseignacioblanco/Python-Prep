
# los comentarios van con numeral o con triple comillas

'''
comentarios de varias lineas
asi comenta paiton
'''

print('mondongo')
a=15
print(a)

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

print("La suma es de: ", n1+n2)

print("La suma con formato es: {}".format(n1+n2))

print(f"La suma de {n1} mas {n2} es: {n1+n2}")

print("la suma de {} mas {} es: {}".format(n1, n2, n1+n2))

#tambien podemos formatiar con las expresiones regulares

print(f"La suma de {n1:^10} mas {n2} es: {n1+n2}")
                   #{n1:-^10}
                   #{n1:->10} 
#para saber que tipo de dato tiene mi variable puedo usar la funcion
# type() que me devuelve el tipo de dato 

print(type(n1))  #como en paiton todo es una clase entosne devuelve class int

#para hacer casting

pi= "3.14159"

print(type(pi))

print(type(float(pi)*2))

# operadores = asignacion == igualdad  <= , >= , != distinto, and, not, or, xor,
# +, -, *, /, // parte entera , ** potencia, % resto, |or, &and, ~not,
# no se si hay operadores a nivel de bits para corrimiento << >>.


#Ahora vemos el if

'''
if condicion:  parece que no hace falta parentesis
    codigo identado
    mas codigo identado
elif:
    codigo
    mas codigo
else:
    mas codigo
    mas codigo
    
codigo fuera del if 
'''

#pass sirve para que el cdigo siga y no le de boliya por ejemplo para cuand
# me falta codigo y lo voy a hacer mas tarde.


