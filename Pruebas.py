# Calculadora Financiera

# Python 3.11.3

import tkinter as tk

from tkinter import *


# FrontEnd

class VentanaPrincipal:
    def __init__(self):
        # Ventana Principal
        self.ventana_principal = ventana_principal = tk.Tk()
        self.ventana_principal.title("♡ Calculadora Financiera ♡")

        # Icono ventana principal
        ventana_principal.iconbitmap("fresa.ico")
        # Icono de https://www.flaticon.es/iconos-gratis/fresa

        # Personalizar tamaño de la ventana principal (descomentar ya que este terminado)
        # ventana_principal.resizable(False,False)

        # Forma del cursor ventana principal
        ventana_principal.config(cursor="heart")

        # Fondo ventana principal
        ventana_principal.config(bg="pink")

        # Titulo ventana principal
        titulo_ventana_principal = Label(ventana_principal,
                                         text="♡ Calculadora Financiera ♡")

        titulo_ventana_principal.grid(row=0,
                                      column=0,
                                      padx=20,
                                      pady=20)

        # Boton seleccion tema/formula (Aun no es un boton pero despues quiero cambiarlo)
        boton_seleccion_formula = Button(ventana_principal,
                                         text="Interes Simple")

        boton_seleccion_formula.grid(row=0,
                                     column=1,
                                     padx=20,
                                     pady=20)
        # Labels para las variables
        variable_capital = Label(ventana_principal,
                                 text="Capital")
        variable_capital.grid(row=1,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky="ew")

        variable_tasa_interes = Label(ventana_principal,
                                      text="Tasa de interes en %")
        variable_tasa_interes.grid(row=2,
                                   column=0,
                                   padx=5,
                                   pady=5,
                                   sticky="ew")

        variable_plazo = Label(ventana_principal,
                               text="Plazo en años")
        variable_plazo.grid(row=3,
                            column=0,
                            padx=5,
                            pady=5,
                            sticky="ew")

        variable_interes = Label(ventana_principal,
                                 text="Interes")
        variable_interes.grid(row=1,
                              column=3,
                              padx=5,
                              pady=5,
                              sticky="ew")

        variable_monto = Label(ventana_principal,
                               text="Monto")
        variable_monto.grid(row=2,
                            column=3,
                            padx=5,
                            pady=5,
                            sticky="ew")

        # Input de variables
        input_capital = Entry(ventana_principal,
                              highlightthickness=4,
                              highlightcolor="pink")
        input_capital.grid(row=1,
                           column=1,
                           padx=5,
                           pady=5,
                           sticky="ew")

        input_tasa_interes = Entry(ventana_principal,
                                   highlightthickness=4,
                                   highlightcolor="pink")
        input_tasa_interes.grid(row=2,
                                column=1,
                                padx=5,
                                pady=5,
                                sticky="ew")

        input_plazo = Entry(ventana_principal,
                            highlightthickness=4,
                            highlightcolor="pink")
        input_plazo.grid(row=3,
                         column=1,
                         padx=5,
                         pady=5,
                         sticky="ew")

        input_interes = Entry(ventana_principal,
                              highlightthickness=4,
                              highlightcolor="pink")
        input_interes.grid(row=1,
                           column=4,
                           padx=5,
                           pady=5,
                           sticky="ew")

        input_monto = Entry(ventana_principal,
                            highlightthickness=4,
                            highlightcolor="pink")
        input_monto.grid(row=2,
                         column=4,
                         padx=5,
                         pady=5,
                         sticky="ew")
        # Botbon calcular
        boton_calcular = Button(ventana_principal, text="Calcular", command=InteresSimple.calcular_interes(self))
        boton_calcular.grid(row=5,
                            column=1,
                            padx=5,
                            pady=5)

        # Ejecutar ventana principal
        ventana_principal.mainloop()


# Backend
class InteresSimple:
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        self.capital = capital
        self.tasa_interes = tasa_interes
        self.plazo = plazo
        self.tipo_plazo = tipo_plazo
        self.interes = interes
        self.monto = monto

    @staticmethod
    def clasemadre():
        print(f"\n~Clase Madre Creada~")

    def calcular_interes(self):
        print("Se calculo el interes")
        pass


class Interes(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


class Monto(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


class Capital(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


class TasaInteres(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


class Plazo(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


class EquivalerPlazo(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
        pass


# main
if __name__ == "__main__":
    app = VentanaPrincipal

VentanaPrincipal()
