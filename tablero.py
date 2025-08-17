class PosOcupadaException(Exception):
    """Excepción lanzada cuando se intenta ocupar una posición ya ocupada"""
    pass

class PosicionInvalidaException(Exception):
    """Excepción lanzada cuando se intenta acceder a una posición inválida"""
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.tamaño = 3
    
    def es_posicion_valida(self, fila, col):
        """Verifica si la posición está dentro de los límites del tablero"""
        return 0 <= fila < self.tamaño and 0 <= col < self.tamaño
    
    def esta_ocupada(self, fila, col):
        """Verifica si una posición está ocupada"""
        if not self.es_posicion_valida(fila, col):
            return False
        return self.contenedor[fila][col] != ""
    
    def poner_la_ficha(self, fila, col, ficha):
        """Coloca una ficha en la posición especificada"""
        if not self.es_posicion_valida(fila, col):
            raise PosicionInvalidaException(f"Posición ({fila}, {col}) inválida. Debe estar entre 0-2.")
        
        if self.esta_ocupada(fila, col):
            raise PosOcupadaException(f"La posición ({fila}, {col}) ya está ocupada!")
        
        self.contenedor[fila][col] = ficha
    
    def obtener_ficha(self, fila, col):
        """Obtiene la ficha en una posición específica"""
        if not self.es_posicion_valida(fila, col):
            return None
        return self.contenedor[fila][col]
    
    def esta_lleno(self):
        """Verifica si el tablero está completamente lleno"""
        for fila in self.contenedor:
            for celda in fila:
                if celda == "":
                    return False
        return True
    
    def reiniciar(self):
        """Reinicia el tablero a su estado inicial"""
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    
    def __str__(self):
        """Representación visual del tablero"""
        resultado = "  0   1   2\n"
        for i, fila in enumerate(self.contenedor):
            resultado += f"{i} "
            for j, celda in enumerate(fila):
                if celda == "":
                    resultado += " - "
                else:
                    resultado += f" {celda} "
                if j < 2:
                    resultado += "|"
            resultado += "\n"
            if i < 2:
                resultado += "  ---|---|---\n"
        return resultado