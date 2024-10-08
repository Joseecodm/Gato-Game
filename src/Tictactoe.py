import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Juego:
    """Clase principal que gestiona el flujo del juego del Gato."""
    def __init__(self):

        self.tablero = Tablero()
        self.jugador1 = Jugador1()
        self.jugador2 = Jugador2()
        self.contador_clicks = 0

    def verificar_turno(self):
        """Verifica de quién es el turno según la cantidad de clics."""
        return self.jugador1 if self.contador_clicks % 2 == 0 else self.jugador2

    def inicializar(self):
        """Inicializa el juego creando el tablero gráfico."""
        self.tablero.crear_tablero()

    def verificar_ganador(self):
        """Verifica si hay un ganador o si es un empate."""
        ganador = self.tablero.verificar_ganador()
        if ganador:
            messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
            self.reiniciar()
        elif self.contador_clicks == 9:
            messagebox.showinfo("Fin del juego", "¡Empate!")
            self.reiniciar()

    def set_boton(self, fila, columna):
        """Asigna la marca del jugador actual a la celda seleccionada en el tablero."""
        jugador_actual = self.verificar_turno()
        self.tablero.set_boton(fila, columna, jugador_actual.marca)
        self.contador_clicks += 1 
        self.verificar_ganador()
        jugador_actual.dar_turno()

    def reiniciar(self):
        """Reinicia el juego, restableciendo el tablero y el contador de clics."""
        self.tablero.reiniciar_tablero()
        self.contador_clicks = 0
        self.jugador1.contador_clicks = 0
        self.jugador2.contador_clicks = 0

class Tablero:
    """Clase que representa el tablero de juego."""

    def __init__(self):
        self.botones = []
        self.matriz = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        self.frame = ttk.Frame()   

    def crear_tablero(self):
        """Crea los botones gráficos del tablero y los organiza en una cuadrícula."""
        for fila in range(3):
            fila_botones = []
            for columna in range(3):
                boton = ttk.Button(self.frame, text="", style="TicTacToe.TButton", command=lambda f=fila, c=columna: juego.set_boton(f, c))
                boton.grid(row=fila, column=columna, padx=5, pady=5)
                fila_botones.append(boton)
            self.botones.append(fila_botones)
        self.frame.pack()

    def verificar_ganador(self):
        """Verifica si existe un ganador en filas, columnas o diagonales."""
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
        """Configura el botón seleccionado con la marca del jugador y lo desactiva."""
        self.botones[fila][columna].config(text=marca, state=tk.DISABLED)
        self.matriz[fila][columna] = marca

    def reiniciar_tablero(self):
        """Reinicia el tablero gráfico y la matriz para un nuevo juego."""
        for fila in self.botones:
            for boton in fila:
                boton.config(text=" ", state=tk.NORMAL)
        self.matriz = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

class Jugadores:
    """Clase base para los jugadores del juego."""

    def __init__(self):
        self.contador_clicks = 0

    def verificar_turno(self):
        """Verifica si es el turno del jugador actual."""
        return juego.verificar_turno() == self

    def dar_turno(self):
        """Método para ser sobrescrito por las subclases, para la lógica del turno."""
        pass

class Jugador1(Jugadores):
    """Clase que representa al Jugador 1, que usa la marca "X"."""

    def __init__(self):
        super().__init__()
        self.marca = "X"

    def dar_turno(self):
        """Ejecuta la lógica del turno para el Jugador 1."""
        if self.verificar_turno():
            juego.verificar_ganador()

class Jugador2(Jugadores):
    """Clase que representa al Jugador 2, que usa la marca "O"."""

    def __init__(self):
        super().__init__()
        self.marca = "O"

    def dar_turno(self):
        """Ejecuta la lógica del turno para el Jugador 2."""
        if self.verificar_turno():
            juego.verificar_ganador()

def aplicar_estilos():
    estilo = ttk.Style()
    estilo.configure("TicTacToe.TButton", font=('Helvetica', 20), width=5, height=2, background="black", foreground="white",  relief="flat")
    estilo.map("TicTacToe.TButton", background=[("active", "blue"), ("disabled", "red")])

aplicar_estilos()
juego = Juego()
juego.inicializar()
juego.tablero.frame.mainloop()
