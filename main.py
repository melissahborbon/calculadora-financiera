# Calculadora Financiera

# Python 3.11.3

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


# Introduccion de datos

C = float(input("Introduce el capital inicial"))
i = float(input("Introduce la tasa de interes"))
n = float(input("Introduce la cantidad de plazos"))
tipodeplazo = str(input("Introduce tipo de plazo"))
I = float(input("Introduce el interes"))
M = float(input("Introduce el monto"))

# Calcular Interes
print(f"Calcular interes")
interes_calculado = Interes(C, i, n, tipodeplazo, I, M)  # Creando una instancia
print(interes_calculado.calcular_interes())  # Llamando al método
print()

# Calcular Monto
print(f"Calcular monto")
monto_calculado = Monto(C, i, n, tipodeplazo, I, M)  # Creando una instancia
print(monto_calculado.calcular_monto())  # Llamando al método
print()

# Calcular Capital
print(f"Calcular capital")
capital_calculado = Capital(C, i, n, tipodeplazo, I, M)
print(capital_calculado.calcular_capital())
print()

# Calcular Tasa de interes
print(f"Calcular tasa de interes")
tasa_interes_calculada = TasaInteres(C, i, n, tipodeplazo, I, M)
print(tasa_interes_calculada.calcular_tasainteres())
print()

# Calcular Plazo
print(f"Calcular plazo")
plazo_calculado = Plazo(C, i, n, tipodeplazo, I, M)
print(plazo_calculado.calcular_plazo())
print()
