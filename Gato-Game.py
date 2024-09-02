import tkinter as tk
from tkinter import messagebox

class Juego:
    """
    Clase principal que gestiona el flujo del juego de Tic-Tac-Toe (Tres en Raya).
    """

    def __init__(self):
        """
        Inicializa el juego creando instancias del tablero y de los jugadores.
        """
        self.tablero = Tablero()
        self.jugador1 = Jugador1()
        self.jugador2 = Jugador2()
        self.contador_clicks = 0

    def verificar_turno(self):
        """
        Verifica de quién es el turno según la cantidad de clics realizados.
        Returns:
            Jugador1 o Jugador2: El jugador cuyo turno es el actual.
        """
        if self.contador_clicks % 2 == 0:
            return self.jugador1
        else:
            return self.jugador2

    def inicializar(self):
        """
        Inicializa el juego creando el tablero gráfico.
        """
        self.tablero.crear_tablero()

    def verificar_ganador(self):
        """
        Verifica si hay un ganador o si se ha alcanzado un empate.
        Si hay un ganador o empate, muestra un mensaje emergente y reinicia el juego.
        """
        ganador = self.tablero.verificar_ganador()
        if ganador:
            messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
            self.reiniciar()
        elif self.contador_clicks == 9:
            messagebox.showinfo("Fin del juego", "¡Empate!")
            self.reiniciar()

    def set_boton(self, fila, columna):
        """
        Asigna la marca del jugador actual a la celda seleccionada en el tablero.
        Luego, verifica si hay un ganador o si se debe continuar el juego.
        Args:
            fila (int): La fila del botón seleccionado.
            columna (int): La columna del botón seleccionado.
        """
        jugador_actual = self.verificar_turno()
        self.tablero.set_boton(fila, columna, jugador_actual.marca)
        self.contador_clicks += 1
        self.verificar_ganador()
        jugador_actual.dar_turno()

    def reiniciar(self):
        """
        Reinicia el juego, restableciendo el tablero y el contador de clics.
        """
        self.tablero.reiniciar_tablero()
        self.contador_clicks = 0
        self.jugador1.contador_clicks = 0
        self.jugador2.contador_clicks = 0

