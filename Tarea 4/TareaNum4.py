from math import sqrt

# La ecuacion.

print('ax² + bx + c = 0\n')

# Escribir los coeficientes.

a, b, c = [float(input(f'Escribe el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]

# Calculamos el discriminante.

discriminante =  b * b - 4 * a * c

# Por si no existen soluciones.

if discriminante < 0: 
    
    print(f'La ecuacion no tiene soluciones.')

else:
    
    # Se calcula la raiz.

    raiz = sqrt(discriminante)      

    # Se calcula una primera solucion.

    x_1 = (-b + raiz) / (2 * a)     

    # Buscar si hay otra solucion.

    if discriminante != 0:          

    # Se calcula la segunda solucion.

        x_2 = (-b - raiz) / (2 * a) 

        # Las dos soluciones.

        print(f'Las soluciones son {x_1} y {x_2}.') 

    else:

        # La única solucion.

        print(f'La unica solucion es x = {x_1}.') 