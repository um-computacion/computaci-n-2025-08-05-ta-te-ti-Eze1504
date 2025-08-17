from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fil, col):
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno)
        # condicion para ganar
        # cambia turno... va a suceder solo si se pudo poner la ficha
        if self.turno == "X":
            self.turno = "0"
        else:
            self.turno = "X"