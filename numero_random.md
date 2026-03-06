Crear un juego donde el programa piensa un número aleatorio entre 1 y 100, y el usuario debe adivinarlo recibiendo pistas.

Pasos a seguir:
1. Gerar un numero aleatorio o Random
2. Pedir al usuario un intento
3. Comparar el numero generado por el ordenador con el número escrito por el usuario
4. Aportar pista: < y >
5. en caso de acierto, generar mensajes de congratulación
6. Contador intentos hasta el éxito
7. Volver empezar 


**Lista de tareas**
1. Generar un número en el rango numerico del 0 al 100 numer=(1,100)
2. Guardar el numero generado
3. Solicitar al usuario un número en el mismo rango en bucle:
    3.1- Validar que el usuario sea un número en el rango establecido
    3.2- Comparar el numero generado por el ordenador
    3.3- Si el número no esl mismo, aportar pista
    3.4- Contabilizar intentos hasta acertar
4. Imprimir número de intentos    
5. Permitir múltiples partidas

**Extructuras**
1. Bucles
    1.1- Intentos del usuario -> while True 
    1.2- Multiples partidas -> while seguir=="s"

2. Condicionales
    2.1- Validar número: try / except
    2.2- Intento correcto: if elif else

**Que variables se necesitan**

1. numero_aleatorio: entero int()
2. numero_usuario: entero int()
3. contador: entero int()
4. seguir_jugando: string input("s/n")
5. best_score: entero int()

**Pseudocodigo**

1. Generar numero_aleatorio entre 1 y 100.
2. Crear un contador de intentos con valor inicial=0.
3. Crear un mensaje de bienvenida al usuario. 
4. Crear el bucle: Mientras el usuario no acierte.
    4.1. Pedir al usuario que introduzca un numero con input
    4.2. Condicionamos el resultado (if, elif, else): 
        4.2.1. Si el numero no es valido:
            4.2.1.1. Mostrar error y volver a pedir otro numero
        4.2.2. Si el numero es valido: 
            4.2.2.1: Si intento<numero_aleatorio:
                print(El valor es demasiado bajo) 
            4.2.2.2: Si intento>numero_aleatorio:
                print(El valor es demasiado bajo)
            4.2.2.3: Si es correcto:
                print(Has acertado!)


Traducción:
    1. Generar numero_aleatorio entre 1 y 100 | numero_secreto = random.randint(0,100)
    2. Crear un contador de intentos | contador=0
    3. Crear un mensaje de bienvenida al usuario | print("Bienvenido al juego. Adivina el número y sal del bucle)
    4. Crear el bucle | while intento != numero_secreto:
        4.1 intento=input("Introduce un numero entre 0 al 100")
        4.2 if numero not in range(0,100):
            print("Error. Intenta con un numero del 0 al 100)
            intento=input()
        4.3. If intento<numero_aleatorio:
                print("El valor es demasiado bajo")
            elif intento>numero_aleatorio:
                print("El valor es demasiado bajo")
            else: 
                print("Has acertado!")

