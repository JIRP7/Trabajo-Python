#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:25:42 2024

@author: joelleRios
"""

import tkinter as tk
from tkinter import ttk
import networkx as nx

# Crear el grafo con las ciudades y distancias
grafo = nx.Graph()
grafo.add_edge("Medellín", "Puerto Berrio", weight=186)
grafo.add_edge("Puerto Berrio", "Puerto Triunfo", weight=129)
grafo.add_edge("Puerto Triunfo", "Honda", weight=102)
grafo.add_edge("Honda", "Bogotá", weight=169)
grafo.add_edge("Medellín", "Puerto Triunfo", weight=190)
grafo.add_edge("Medellín", "Manizales", weight=200)
grafo.add_edge("Manizales", "Honda", weight=141)
grafo.add_edge("Manizales", "Ibagué", weight=174)
grafo.add_edge("Ibagué", "Girardot", weight=66)
grafo.add_edge("Girardot", "Bogotá", weight=133)
grafo.add_edge("Ibagué", "Honda", weight=141)
grafo.add_edge("Honda", "Bogotá", weight=169)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Rutas Mínimas entre Ciudades")

# Variables de las ciudades seleccionadas
origen = tk.StringVar()
destino = tk.StringVar()

# Función para calcular la ruta mínima
def calcular_ruta():
    ciudad_origen = origen.get()
    ciudad_destino = destino.get()
    tree_1.delete(*tree_1.get_children())

    # Calcular ruta más corta usando Dijkstra
    try:
        ruta_minima = nx.dijkstra_path(grafo, ciudad_origen, ciudad_destino, weight='weight')
        
        lista_rutas = [0.0]
        suma = 0.0
        for rutas in range(len(ruta_minima)-1):
            suma += grafo[ruta_minima[rutas]][ruta_minima[rutas+1]]['weight']
            lista_rutas.append(suma)    
        
        for rutas in range(len(ruta_minima)):
            tree_1.insert("", "end", values=(ruta_minima[rutas], lista_rutas[rutas]))
    except nx.NetworkXNoPath:
        return "No hay ruta disponible entre las ciudades seleccionadas."


frame_tabla = tk.Frame(root)
frame_tabla.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Crear el widget Treeview para la tabla
tree = ttk.Treeview(frame_tabla, columns=("Destino"), show="headings")
tree.heading("Destino", text="Ciudad Destino")
tree.column("Destino", width=250)
ciudades = ['Medellín', 'Puerto Berrio', 'Puerto Triunfo', 'Manizales', 'Honda', 'Bogotá', 'Girardot', 'Ibagué']
for ciudad in ciudades:
    tree.insert("", "end", values=(ciudad,))
tree.pack()

frame_tabla = tk.Frame(root)
frame_tabla.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

# Crear el widget Treeview para la tabla
tree = ttk.Treeview(frame_tabla, columns=("nodo1", "nodo2", "valor"), show="headings")
tree.heading("nodo1", text="Nodo 1")
tree.heading("nodo2", text="Nodo 2")
tree.heading("valor", text="Valor")
tree.column("nodo1", width=100)
tree.column("nodo2", width=100)
tree.column("valor", width=100)

scrollbar_y = tk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar_y.set)

# Insertar las conexiones en la tabla
for nodo1, nodo2, datos in grafo.edges(data=True):
    # Extraer el valor del peso de la conexión
    peso = datos['weight']
    # Insertar en la tabla
    tree.insert("", "end", values=(nodo1, nodo2, peso))

tree.pack()

# Etiqueta de selección de ciudad origen

# Crear un LabelFrame para agrupar los widgets
frame_origen_destino = ttk.LabelFrame(root, text="Seleccionar Ciudad", padding=(10, 5))
frame_origen_destino.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Etiqueta de selección de ciudad origen dentro del LabelFrame
ttk.Label(frame_origen_destino, text="Ciudad Origen:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Combobox de origen dentro del LabelFrame
origen_menu = ttk.Combobox(frame_origen_destino, textvariable=origen)
origen_menu['values'] = list(grafo.nodes)
origen_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Etiqueta de selección de ciudad destino dentro del LabelFrame
ttk.Label(frame_origen_destino, text="Ciudad Destino:").grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Combobox de destino dentro del LabelFrame
destino_menu = ttk.Combobox(frame_origen_destino, textvariable=destino)
destino_menu['values'] = list(grafo.nodes)
destino_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Botón para calcular la ruta mínima
boton_calcular = ttk.Button(root, text="Calcular Ruta Mínima", command=calcular_ruta)
boton_calcular.grid(row=2, column=0, columnspan=2, pady=20)

frame_tabla = tk.Frame(root)
frame_tabla.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

# Crear el widget Treeview para la tabla
tree_1 = ttk.Treeview(frame_tabla, columns=("Nombre", "valor"), show="headings", height=8)
tree_1.heading("Nombre", text="Nombre")
tree_1.heading("valor", text="Valor")
tree_1.column("Nombre", width=150)
tree_1.column("valor", width=150)
tree_1.pack()

# Ejecutar la ventana principal
root.mainloop()


