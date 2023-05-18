# Calculadora Financiera
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *


# Python 3.11.3

# Front End
class VentanaPrincipal:
    def __init__(self):
        self.capital = None
        self.tasa_interes = None
        self.plazo = None
        self.interes = None
        self.monto = None

        # Creacion de ventana principal
        self.ventana_principal = ventana_principal = tk.Tk()
        self.ventana_principal.title(" ♡ Calculadora Financiera ♡ ")
        self.ventana_principal.iconbitmap("fresa.ico")
        self.ventana_principal.config(cursor="heart", bg="pink")

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
        self.input_capital = Entry(ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_capital.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.input_tasa_interes = Entry(ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_tasa_interes.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.input_plazo = Entry(ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_plazo.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.input_interes = Entry(ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_interes.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

        self.input_monto = Entry(ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_monto.grid(row=2, column=4, padx=5, pady=5, sticky="ew")

        # Botbon calcular
        boton_calcular = Button(ventana_principal, text="Calcular", command=self.calcular)
        boton_calcular.grid(row=5, column=1, padx=5, pady=5)

        # Ejecutar ventana principal
        ventana_principal.mainloop()

    def calcular(self):
        # Obteniendo los valores de los Entry
        try:
            self.capital = float(self.input_capital.get()) if self.input_capital.get() != "" else None
            self.tasa_interes = float(self.input_tasa_interes.get()) if self.input_tasa_interes.get() != "" else None
            self.plazo = float(self.input_plazo.get()) if self.input_plazo.get() != "" else None
            self.interes = float(self.input_interes.get()) if self.input_interes.get() != "" else None
            self.monto = float(self.input_monto.get()) if self.input_monto.get() != "" else None
        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrate de que todas las entradas son números.")
            return

        if self.capital is None and self.tasa_interes and self.plazo and self.interes:
            self.capital = Capital(self.interes / (self.plazo * self.tasa_interes), self.tasa_interes, self.plazo, '',
                                   self.interes, 0).calcular_capital()
            self.input_capital.delete(0, 'end')
            self.input_capital.insert(0, str(self.capital))

        elif self.tasa_interes is None and self.capital and self.plazo and self.interes:
            self.tasa_interes = TasaInteres(self.capital, self.interes / (self.capital * self.plazo), self.plazo, '',
                                            self.interes, 0).calcular_tasainteres()
            self.input_tasa_interes.delete(0, 'end')
            self.input_tasa_interes.insert(0, str(self.tasa_interes))

        elif self.plazo is None and self.capital and self.tasa_interes and self.interes:
            self.plazo = Plazo(self.capital, self.tasa_interes, self.interes / (self.capital * self.tasa_interes), '',
                               self.interes, 0).calcular_plazo()
            self.input_plazo.delete(0, 'end')
            self.input_plazo.insert(0, str(self.plazo))

        elif self.interes is None and self.capital and self.tasa_interes and self.plazo:
            self.interes = Interes(self.capital, self.tasa_interes, self.plazo, '', 0, 0).calcular_interes()
            self.input_interes.delete(0, 'end')
            self.input_interes.insert(0, str(self.interes))

        elif self.monto is None and self.capital and self.interes:
            self.monto = Monto(self.capital, self.tasa_interes, self.plazo, '', self.interes, 0).calcular_monto()
            self.input_monto.delete(0, 'end')
            self.input_monto.insert(0, str(self.monto))

        else:
            messagebox.showerror("Error", "Por favor, asegúrate de que todas las entradas cumplen los requerimientos.")


# Backend

# Variables


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

    def conversion_a_porcentaje(self):
        self.tasa_interes = self.tasa_interes / 100
        return self.tasa_interes

    # def equivaler_plazo(self):
    #     def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
    #         super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
    #         pass


class Interes(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_interes(self):
        self.conversion_a_porcentaje()
        self.interes = self.capital * self.tasa_interes * self.plazo
        return self.interes


class Monto(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_monto(self):
        self.monto = self.capital + self.interes
        return self.monto


class Capital(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_capital(self):
        self.conversion_a_porcentaje()
        self.capital = self.interes / (self.tasa_interes * self.plazo)
        return self.capital


class TasaInteres(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_tasainteres(self):
        self.tasa_interes = (self.interes / self.capital) / self.plazo
        self.tasa_interes = round(self.tasa_interes, 3)  # Redondear a 2 decimales
        return self.tasa_interes


class Plazo(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_plazo(self):
        self.conversion_a_porcentaje()
        self.plazo = self.interes / (self.capital * self.tasa_interes)
        return self.plazo


if __name__ == "__main__":
    ventana = VentanaPrincipal()
