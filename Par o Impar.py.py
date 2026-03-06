while True: # 1. Empieza el bucle
    try: # 2. Intentamos capturar el dato
        # EL INPUT VA AQUÍ (con 8 espacios a la izquierda)
        numero_usuario = int(input("Introduce un número entre 1 y 100: "))

        if numero_usuario > 100 or numero_usuario < 1:
            print("Número fuera de rango. Vuelve a intentarlo.")
            continue 
        
        if numero_usuario % 2 == 0:
            print(f"El número {numero_usuario} es PAR.") [cite: 1]
        else:
            print(f"El número {numero_usuario} es IMPAR.") [cite: 1]
        
        break # Si todo sale bien, salimos del bucle

    except ValueError:
        print("Error: ¡Debes introducir un número entero!")
        
  
     

