from tateti import Tateti
from jugador import Jugador
from tablero import PosOcupadaException, PosicionInvalidaException

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("         TATETI - MENÚ PRINCIPAL")
    print("="*40)
    print("1. Jugar nueva partida")
    print("2. Ver estadísticas")
    print("3. Salir")
    print("="*40)

def obtener_nombres_jugadores():
    """Obtiene los nombres de los jugadores"""
    print("\n--- CONFIGURACIÓN DE JUGADORES ---")
    nombre1 = input("Nombre del Jugador 1 (X): ").strip() or "Jugador 1"
    nombre2 = input("Nombre del Jugador 2 (O): ").strip() or "Jugador 2"
    return nombre1, nombre2

def obtener_movimiento():
    """Obtiene y valida el movimiento del jugador"""
    while True:
        try:
            entrada = input("Ingrese fila y columna (ej: 1 2) o 'q' para salir: ").strip()
            
            if entrada.lower() == 'q':
                return None, None
            
            partes = entrada.split()
            if len(partes) != 2:
                print("Por favor ingrese dos números separados por espacio.")
                continue
            
            fila = int(partes[0])
            col = int(partes[1])
            
            if not (0 <= fila <= 2 and 0 <= col <= 2):
                print("Los números deben estar entre 0 y 2.")
                continue
                
            return fila, col
            
        except ValueError:
            print("Por favor ingrese números válidos.")
        except KeyboardInterrupt:
            return None, None

def jugar_partida(jugador1, jugador2):
    """Ejecuta una partida completa"""
    juego = Tateti()
    jugadores = {
        'X': jugador1,
        'O': jugador2
    }
    
    print(f"\n¡Comienza la partida!")
    print(f"{jugador1.nombre} vs {jugador2.nombre}")
    
    while not juego.juego_terminado:
        # Mostrar estado actual
        print("\n" + "="*30)
        print(juego.tablero)
        
        jugador_actual = jugadores[juego.turno]
        print(f"Turno de {jugador_actual.nombre} ({juego.turno})")
        
        # Obtener movimiento
        fila, col = obtener_movimiento()
        
        if fila is None:  # El jugador quiere salir
            print("Partida cancelada.")
            return False
        
        # Intentar hacer el movimiento
        try:
            resultado = juego.ocupar_casilla(fila, col)
            
            if resultado:  # Hay ganador o empate
                print("\n" + "="*30)
                print(juego.tablero)
                print(resultado)
                
                if juego.ganador:
                    jugador_ganador = jugadores[juego.ganador]
                    jugador_ganador.incrementar_victorias()
                
                return True
                
        except (PosOcupadaException, PosicionInvalidaException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def mostrar_estadisticas(jugador1, jugador2):
    """Muestra las estadísticas de los jugadores"""
    print("\n" + "="*40)
    print("           ESTADÍSTICAS")
    print("="*40)
    print(jugador1)
    print(jugador2)
    print("="*40)

def main():
    print("¡Bienvenidos al TATETI!")
    
    # Configurar jugadores
    nombre1, nombre2 = obtener_nombres_jugadores()
    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                limpiar_pantalla()
                partida_completada = jugar_partida(jugador1, jugador2)
                if partida_completada:
                    input("\nPresione Enter para continuar...")
                    
            elif opcion == "2":
                mostrar_estadisticas(jugador1, jugador2)
                input("\nPresione Enter para continuar...")
                
            elif opcion == "3":
                print("¡Gracias por jugar!")
                break
                
            else:
                print("Opción inválida. Intente nuevamente.")
                
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()