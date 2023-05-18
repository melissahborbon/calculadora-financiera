# Calculadora Financiera
import tkinter as tk

from tkinter import *

import tkinter.messagebox as messagebox


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

    import tkinter.messagebox as messagebox

    def calcular(self):
        # Obteniendo los valores de los Entry
        try:
            self.capital = float(self.input_capital.get())
            self.tasa_interes = float(self.input_tasa_interes.get())
            self.plazo = float(self.input_plazo.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrate de que todas las entradas son números.")
            return

        # Verificando que las variables necesarias existen y son mayores a cero
        if self.capital > 0 and self.tasa_interes > 0 and self.plazo > 0:
            # Calculando Interes
            self.interes = Interes(self.capital, self.tasa_interes, self.plazo, '', 0, 0)
            self.input_interes.delete(0, 'end')
            self.input_interes.insert(0, str(self.interes.calcular_interes()))

            # Calculando Monto
            self.monto = Monto(self.capital, self.tasa_interes, self.plazo, '', self.interes.interes, 0)
            self.input_monto.delete(0, 'end')
            self.input_monto.insert(0, str(self.monto.calcular_monto()))
        else:
            messagebox.showerror("Error", "Por favor, asegúrate de que todas las entradas son números positivos.")


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
