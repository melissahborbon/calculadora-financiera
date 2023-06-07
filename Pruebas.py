# Calculadora Financiera
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Python 3.11.3

# Front End

# Obtener el input numerico
def get_numeric_input(input_entry):
    value = input_entry.get()
    try:
        return float(value)
    except ValueError:
        return None


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

        # Crear un Label en lugar de un botón
        etiqueta_seleccion_formula = Label(ventana_principal,
                                           text="Interes Simple")
        etiqueta_seleccion_formula.grid(row=0,
                                        column=1,
                                        padx=20,
                                        pady=20)

        # Crear Combobox para seleccionar la variable a calcular
        self.seleccion_variable = ttk.Combobox(self.ventana_principal, state="readonly")
        self.seleccion_variable['values'] = ['Capital', 'Tasa de Interes', 'Plazo', 'Interes', 'Monto']
        self.seleccion_variable.current(0)  # Configura 'Capital' como la opción por defecto
        self.seleccion_variable.grid(row=4, column=1, padx=5, pady=5)

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
        self.input_capital = Entry(self.ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_capital.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.input_capital.insert(0, "0")  # Valor por defecto

        self.input_tasa_interes = Entry(self.ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_tasa_interes.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.input_tasa_interes.insert(0, "0")  # Valor por defecto

        self.input_plazo = Entry(self.ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_plazo.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.input_plazo.insert(0, "0")  # Valor por defecto

        self.input_interes = Entry(self.ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_interes.grid(row=1, column=4, padx=5, pady=5, sticky="ew")
        self.input_interes.insert(0, "0")  # Valor por defecto

        self.input_monto = Entry(self.ventana_principal, highlightthickness=4, highlightcolor="pink")
        self.input_monto.grid(row=2, column=4, padx=5, pady=5, sticky="ew")
        self.input_monto.insert(0, "0")  # Valor por defecto

        # Boton de calcular
        boton_calcular = Button(ventana_principal,
                                text="Calcular",
                                command=self.calcular)
        boton_calcular.grid(row=4,
                            column=0,
                            padx=5,
                            pady=5)

        self.img = Image.open("crecimiento.png").resize((100, 100))
        self.img = ImageTk.PhotoImage(self.img)

        label_img = Label(ventana_principal, image=self.img)
        label_img.config(width=100, height=100)
        label_img.grid(row=4, column=4, padx=0, pady=10, sticky="nw")

    def calcular(self):
        # Obtener los valores de entrada
        capital = get_numeric_input(self.input_capital)
        tasa_interes = get_numeric_input(self.input_tasa_interes)
        plazo = get_numeric_input(self.input_plazo)
        interes = get_numeric_input(self.input_interes)
        monto = get_numeric_input(self.input_monto)

        # Verificar si todos los valores son numéricos
        if None in (capital, tasa_interes, plazo, interes, monto):
            messagebox.showerror("Error", "Por favor introduzca solo números.")
            return

        # Compare inflation rate and interest rate
        inflacion = ventana_inflacion.valor_inflacion
        if inflacion > tasa_interes:
            messagebox.showinfo("Comparación", "La tasa de interés es menor a la tasa de inflación. :C")
        elif inflacion == tasa_interes:
            messagebox.showinfo("Comparación", "La tasa de interés es igual a la tasa de inflación. :3")
        elif inflacion < tasa_interes:
            messagebox.showinfo("Comparación", "La tasa de interés es mayor a la tasa de inflación. :D")

        # Crear instancias de las clases con los valores de entrada
        capital_obj = Capital(capital, tasa_interes, plazo, 'Años', interes, monto)
        tasa_interes_obj = TasaInteres(capital, tasa_interes, plazo, 'Años', interes, monto)
        plazo_obj = Plazo(capital, tasa_interes, plazo, 'Años', interes, monto)
        interes_obj = Interes(capital, tasa_interes, plazo, 'Años', interes, monto)
        monto_obj = Monto(capital, tasa_interes, plazo, 'Años', interes, monto)

        # Obtener la selección del botón desplegable
        seleccion = self.seleccion_variable.get()

        # Dependiendo de la selección, llamar al método correspondiente para calcular la variable seleccionada
        if seleccion == 'Capital':
            # Calcular el capital
            result = capital_obj.calcular_capital()
        elif seleccion == 'Tasa de Interes':
            # Calcular la tasa de interes
            result = tasa_interes_obj.calcular_tasainteres()
            result = result * 100
        elif seleccion == 'Plazo':
            # Calcular el plazo
            result = plazo_obj.calcular_plazo()
        elif seleccion == 'Interes':
            # Calcular el interes
            result = interes_obj.calcular_interes()
        elif seleccion == 'Monto':
            # Calcular el monto
            result = monto_obj.calcular_monto()
        else:
            messagebox.showerror("Error", "Selección no válida.")
            return

        # Actualizar la entrada con el resultado
        if seleccion == 'Capital':
            self.input_capital.delete(0, END)
            self.input_capital.insert(0, str(result))
        elif seleccion == 'Tasa de Interes':
            self.input_tasa_interes.delete(0, END)
            self.input_tasa_interes.insert(0, str(result))
        elif seleccion == 'Plazo':
            self.input_plazo.delete(0, END)
            self.input_plazo.insert(0, str(result))
        elif seleccion == 'Interes':
            self.input_interes.delete(0, END)
            self.input_interes.insert(0, str(result))
        elif seleccion == 'Monto':
            self.input_monto.delete(0, END)
            self.input_monto.insert(0, str(result))

    def iniciar(self):
        self.ventana_principal.mainloop()


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


class VentanaInflacion:
    def __init__(self):
        self.valor_inflacion = None

        # Creación de la ventana de inflación
        self.ventana_inflacion = tk.Tk()
        self.ventana_inflacion.title("Inflación")
        self.ventana_inflacion.iconbitmap("fresa.ico")
        self.ventana_inflacion.config(cursor="heart", bg="pink")

        etiqueta_inflacion = Label(self.ventana_inflacion, text="Porcentaje de Inflación:")
        etiqueta_inflacion.grid(row=0, column=0, padx=20, pady=20)

        self.input_inflacion = Entry(self.ventana_inflacion, highlightthickness=4, highlightcolor="pink")
        self.input_inflacion.grid(row=0, column=1, padx=5, pady=5)

        boton_confirmar = Button(self.ventana_inflacion, text="Confirmar", command=self.obtener_inflacion)
        boton_confirmar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def obtener_inflacion(self):
        valor = get_numeric_input(self.input_inflacion)
        if valor is not None:
            self.valor_inflacion = valor
            self.ventana_inflacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico.")

    def iniciar(self):
        self.ventana_inflacion.mainloop()


if __name__ == "__main__":
    ventana_inflacion = VentanaInflacion()
    ventana_inflacion.iniciar()

    # Verificar si se ingresó un valor de inflación válido
    if ventana_inflacion.valor_inflacion is not None:
        ventana_principal = VentanaPrincipal()
        ventana_principal.iniciar()
