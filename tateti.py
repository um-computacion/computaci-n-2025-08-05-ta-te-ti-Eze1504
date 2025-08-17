from tablero import Tablero, PosOcupadaException, PosicionInvalidaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.ganador = None
        self.juego_terminado = False
    
    def cambiar_turno(self):
        """Cambia el turno al siguiente jugador"""
        self.turno = "O" if self.turno == "X" else "X"
    
    def verificar_linea(self, pos1, pos2, pos3):
        """Verifica si tres posiciones forman una línea ganadora"""
        ficha1 = self.tablero.obtener_ficha(*pos1)
        ficha2 = self.tablero.obtener_ficha(*pos2)
        ficha3 = self.tablero.obtener_ficha(*pos3)
        
        return (ficha1 != "" and ficha1 == ficha2 == ficha3)
    
    def verificar_ganador(self):
        """Verifica si hay un ganador en el tablero"""
        # Verificar filas
        for i in range(3):
            if self.verificar_linea((i, 0), (i, 1), (i, 2)):
                return self.tablero.obtener_ficha(i, 0)
        
        # Verificar columnas
        for j in range(3):
            if self.verificar_linea((0, j), (1, j), (2, j)):
                return self.tablero.obtener_ficha(0, j)
        
        # Verificar diagonales
        if self.verificar_linea((0, 0), (1, 1), (2, 2)):
            return self.tablero.obtener_ficha(1, 1)
        
        if self.verificar_linea((0, 2), (1, 1), (2, 0)):
            return self.tablero.obtener_ficha(1, 1)
        
        return None
    
    def ocupar_casilla(self, fila, col):
        """Ocupa una casilla del tablero con la ficha del jugador actual"""
        if self.juego_terminado:
            raise Exception("El juego ya ha terminado!")
        
        # Intentar poner la ficha
        self.tablero.poner_la_ficha(fila, col, self.turno)
        
        # Verificar si hay ganador
        ganador = self.verificar_ganador()
        if ganador:
            self.ganador = ganador
            self.juego_terminado = True
            return f"¡{ganador} ha ganado!"
        
        # Verificar empate
        if self.tablero.esta_lleno():
            self.juego_terminado = True
            return "¡Es un empate!"
        
        # Cambiar turno solo si el juego continúa
        self.cambiar_turno()
        return None
    
    def reiniciar_juego(self):
        """Reinicia el juego a su estado inicial"""
        self.turno = "X"
        self.tablero.reiniciar()
        self.ganador = None
        self.juego_terminado = False
    
    def obtener_estado(self):
        """Retorna el estado actual del juego"""
        return {
            'tablero': str(self.tablero),
            'turno': self.turno,
            'ganador': self.ganador,
            'terminado': self.juego_terminado
        }