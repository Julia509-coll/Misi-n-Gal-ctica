# Inicializamos la variable como "vacía" usando None
numero_usuario = None

# El bucle se ejecuta mientras numero_usuario no tenga un valor válido
while numero_usuario is None:
    try:
        entrada = int(input("Introduce un número (1-100): "))
        
        # Verificamos el rango
        if 1 <= entrada <= 100:
            # Si es válido, se lo asignamos a nuestra variable
            numero_usuario = entrada
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
            
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# Al salir del bucle, numero_usuario ya no es None, así que calculamos
if numero_usuario % 2 == 0:
    print(f"El resultado final es: {numero_usuario} es PAR.")
else:
    print(f"El resultado final es: {numero_usuario} es IMPAR.")

