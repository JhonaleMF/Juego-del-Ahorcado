from funciones_ahorcado import start_game, instructions, exit_game, progress
import tkinter as tk
from tkinter import ttk

#Menu principal del juego
"""
Opciones del juego que ejecuta las diferentes funcionalidades del juego como, instrucciones, comenzar juego, Ver progreso palabra y salir del juego.
Estas opciones ejecutan funciones del script funciones_ahorcado.py
"""
ventana = tk.Tk(className='Python Examples - Window Size')
ventana.geometry("350x100")
ventana.title(f"Menú: JUEGO AHORCADO")
boton = ttk.Button(text= "Ver instrucciones", command=instructions).pack()
boton = ttk.Button(text= "Comenzar Juego", command=start_game).pack()   
boton = ttk.Button(text= "Ver progeso palabra", command=progress).pack() 
boton = ttk.Button(text= "Salir del juego", command=exit_game).pack()      
ventana.mainloop()
