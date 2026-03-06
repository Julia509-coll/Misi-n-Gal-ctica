# ==========================================================
# EJERCICIO: ADIVINA EL NÚMERO (VERSIÓN CON FUNCIONES)
# ==========================================================
# REQUISITOS:
# 1. Usar random.randint(1, 100) para el número secreto.
# 2. Pedir intentos hasta que el usuario acierte.
# 3. Dar pistas: "Más alto" o "Más bajo".
# 4. Contar los intentos realizados.
# 5. Validar que la entrada sea un número (try/except).
# ==========================================================

import random

def pedir_numero():
    """Responsabilidad: Pedir, validar y devolver un entero."""
    while True:
        entrada = input("Tu intento: ")
        try:
            # Intentamos convertir el texto a número
            return int(entrada)
        except ValueError:
            # Si el usuario escribe letras, saltamos aquí
            print("⚠️ Error: Introduce un número válido.")

def jugar_partida():
    """Responsabilidad: Ejecutar una partida completa."""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("\n[NUEVA PARTIDA] He pensado un número entre 1 y 100.")
    
    while True:
        intento = pedir_numero()
        intentos += 1
        
        if intento < numero_secreto:
            print("Más alto")
        elif intento > numero_secreto:
            print("Más bajo")
        else:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            return intentos

def main():
    """Responsabilidad: Controlar el flujo y el récord."""
    mejor_record = None
    
    while True:
        intentos_actuales = jugar_partida()
        
        # Lógica para guardar el récord (el número más bajo de intentos)
        if mejor_record is None or intentos_actuales < mejor_record:
            mejor_record = intentos_actuales
            print(f"🌟 ¡NUEVO RÉCORD! Has bajado a {mejor_record} intentos.")
        
        # Preguntar si quiere seguir
        opcion = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if opcion != 's':
            print(f"\nGracias por jugar. Tu récord final fue: {mejor_record}")
            break

# Este bloque asegura que el juego solo empiece si ejecutas este archivo
if __name__ == "__main__":
    main()