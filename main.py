'''fidel valdez palma'''

'''funcion para evaluar la funcion (String) y convertirla a exprecion matematica
        tambien enviarle que quieres sustituir por "x", ya sea x0,x1 o xr
'''
def evaluar_Funcion(funcion, x):
    return eval(funcion)
    
''' metodo de biseccion, le envias x0, x1 y la funcion para que resuelva xr y la sustitucion en las funciones
    por defecto en los trabajos nos ponia con un error de 5%, asi que por defecto tiene ese error
'''
def metodo_biseccion(x0, x1, funcion, error_Aceptado=0.5): 
    xr = (x0 + x1) / 2                      # Sacar el punto medio
    error = abs((x1 - x0) / x1) * 100       # Calcular el error %
    contador = 0                            # Contador para ver las iteraciones
   
    while error > error_Aceptado:           # Mientras el error sea mayor al 5%
        fx0 = evaluar_Funcion(funcion, x0)  # Evaluar la funcion en x0, x1 y xr
        fx1 = evaluar_Funcion(funcion, x1)
        fxr = evaluar_Funcion(funcion, xr)
       
        if fx0 * fxr < 0:                   # Si es menor a 0, la raiz esta en el intervalo de x0 a xr
            x1 = xr
        else:                               # Si es mayor a 0, la raiz esta en el intervalo de xr a x1
            x0 = xr
            
        xr = (x0 + x1) / 2                  # Con el nuevo x0 o x1, segun el xr anterior, se vuelve a calcular xr y el error%
        error = abs((x1 - x0) / x1) * 100
        
                #Ir mostrando el proceso  
        xr_Redondeado = round(xr,3)
        error_Redondeado = round(error,3)
        print(f"Iteracion:{contador}, Raiz:{xr_Redondeado}, Error:{error_Redondeado}%")      
        contador += 1                       # Incrementar el contador de iteraciones
    
    return xr, contador, error              # Devolver la raiz, el contador y el error

print("NOTA: para enviar ^ ocupas poner **, ejemplo: f(x)=x^3-4x-9, en codigo es: x**3-4*x-9\n")  # Nota para probar el codigo
x0 = float(input("Teclea X0: "))            # Pedir x0, x1 y la funcion
x1 = float(input("Teclea X1: "))
funcion = input("Teclea la funcion f(x):")
print("")

# Calcular la raiz segun lo que envio el usuario
raiz, iteraciones, error = metodo_biseccion(x0, x1, funcion)

# Mostrar la raiz aproximada, las iteraciones y el error
print(f"\nEn {iteraciones-1} iteraciones, la raiz aproximada fue de: {raiz} con un % de error de {error}%")