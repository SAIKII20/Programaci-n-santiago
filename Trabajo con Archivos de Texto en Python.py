# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AIV3leUlgw4Xkpgm_mjRGlmKKsPjDkgK
"""

# Crear un archivo de texto y escribir notas personales
with open("my_notes.txt", "w") as file:
    file.write("Hola mundo.\n")
    file.write("Hoy aprendí sobre el manejo de archivos en Python.\n")
    file.write("recuerda estudiar.\n")

# Leer el contenido del archivo y mostrarlo en consola
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # Elimina saltos de línea al final de cada línea