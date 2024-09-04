import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Juego:
    """
    Clase principal que gestiona el flujo del juego del Gato (Tres en Raya).
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

class Tablero:
    """
    Clase que representa el tablero de juego.
    """

    def __init__(self):
        """
        Inicializa el tablero con una matriz vacía y un contenedor gráfico de botones.
        """
        self.botones = []
        self.matriz = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        self.frame = tk.Frame()

    def crear_tablero(self):
        """
        Crea los botones gráficos del tablero y los organiza en una cuadrícula.
        """
        for fila in range(3):
            fila_botones = []
            for columna in range(3):
                boton = tk.Button(self.frame, text=" ", font=('Helvetica', 20), width=5, height=2,
                                  command=lambda f=fila, c=columna: juego.set_boton(f, c))
                boton.grid(row=fila, column=columna)
                fila_botones.append(boton)
            self.botones.append(fila_botones)
        self.frame.pack()

    def verificar_ganador(self):
        """
        Verifica si existe un ganador en filas, columnas o diagonales.
        Returns:
            str: La marca del jugador ganador ("X" o "O"), o None si no hay ganador.
        """
        for i in range(3):
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] and self.matriz[i][0] is not None:
                return self.matriz[i][0]  # Ganador en fila
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] and self.matriz[0][i] is not None:
                return self.matriz[0][i]  # Ganador en columna

        # Verificar diagonales
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] and self.matriz[0][0] is not None:
            return self.matriz[0][0]
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] and self.matriz[0][2] is not None:
            return self.matriz[0][2]

        return None  # No hay ganador aún

    def set_boton(self, fila, columna, marca):
        """
        Configura el botón seleccionado con la marca del jugador y lo desactiva.
        Args:
            fila (int): La fila del botón.
            columna (int): La columna del botón.
            marca (str): La marca del jugador ("X" o "O").
        """
        self.botones[fila][columna].config(text=marca, state=tk.DISABLED)
        self.matriz[fila][columna] = marca

    def reiniciar_tablero(self):
        """
        Reinicia el tablero gráfico y la matriz para un nuevo juego.
        """
        for fila in self.botones:
            for boton in fila:
                boton.config(text=" ", state=tk.NORMAL)
        self.matriz = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

class Jugadores:
    """
    Clase base para los jugadores del juego.
    """

    def __init__(self):
        """
        Inicializa el contador de clics para los jugadores.
        """
        self.contador_clicks = 0

    def verificar_turno(self):
        """
        Verifica si es el turno del jugador actual.
        Returns:
            bool: True si es el turno del jugador, False de lo contrario.
        """
        return juego.verificar_turno() == self

    def dar_turno(self):
        """
        Método para ser sobrescrito por las subclases, para la lógica del turno.
        """
        pass
class Jugador1(Jugadores):
    """
    Clase que representa al Jugador 1, que usa la marca "X".
    """

    def __init__(self):
        """
        Inicializa al Jugador 1 con la marca "X".
        """
        super().__init__()
        self.marca = "X"

    def dar_turno(self):
        """
        Ejecuta la lógica del turno para el Jugador 1.
        """
        if self.verificar_turno():
            juego.verificar_ganador()

class Jugador2(Jugadores):
    """
    Clase que representa al Jugador 2, que usa la marca "O".
    """

    def __init__(self):
        """
        Inicializa al Jugador 2 con la marca "O".
        """
        super().__init__()
        self.marca = "O"

    def dar_turno(self):
        """
        Ejecuta la lógica del turno para el Jugador 2.
        """
        if self.verificar_turno():
            juego.verificar_ganador()

juego = Juego()
juego.inicializar()
juego.tablero.frame.mainloop()