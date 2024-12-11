import tkinter as tk
from tkinter import ttk

# Funciones del problema
def calcularRaicesCuadraticas():
    raices = 0.0
    try:
        raices = float(input_ecuacion.get())
        etiqueta_error_raices(text=f"")
    except ValueError as ve:
        etiqueta_error_raices.config(text=f"introduce una formula")
        #crear un objeto de la clase Raices
        conversionRaices = Raices()
        etiqueta_coeficienteA.config(text=f"la coeficienteA son: {conversionRaices.calcularRaicesCuadraticas(raices)}")
        etiqueta_coeficienteB.config(text=f"la coeficienteB son: {conversionRaices.calcularRaicesCuadraticas(raices)}")
        etiqueta_coeficienteC.config(text=f"la coeficienteC son: {conversionRaices.calcularRaicesCuadraticas(raices)}")

ventana =tk.Tk()
ventana.title("Ecuacion")
ventana.config(width=100, height=200)
etiqueta_raices=ttk.Lbel(text="introduce la raiz cuadrada")
etiqueta_raices.place(x=6, y=6)

input_Ecuacion = ttk.Entry()
input_Ecuacion.place(x=50, y=30, width=80)

#etiquetas para los errores
etiqueta_error_raices = ttk.Label(text="-")
etiqueta_error_raices.place(x=250, y=20)

bon_convertir = ttk.Button(text="convertir",command=calcularRaicesCuadraticas)
boton_convertir.place(x=50, y=50)

etiqueta_coeficienteA = ttk.Label(text="la coeficienteA son:")
etiqueta_coeficienteA.place(x=25, y=80)
etiqueta_coeficienteB = ttk.Label(text="la coeficienteB son:")        
etiqueta_coeficienteB.place(x=25, y=90)
etiqueta_coeficienteC = ttk.Label(text="la coeficienteC son:")
etiqueta_coeficienteC.place(x=25, y=100)
ventana.mainloop()