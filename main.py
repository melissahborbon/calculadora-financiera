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


class Interes(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_interes(self):
        self.tasa_interes = self.tasa_interes / 100
        self.interes = self.capital * self.tasa_interes * self.plazo
        return self.interes


class Monto(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_monto(self):
        self.monto = self.capital + self.interes
        return self.monto

    def calcular_monto_2(self):
        self.monto = self.capital(1 + self.tasa_interes * self.plazo)
        return self.monto


class Capital(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_capital(self):
        self.capital = self.interes / (self.tasa_interes * self.plazo)


class TasaInteres(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_tasainteres(self):
        self.tasa_interes = (self.interes / self.capital) / self.plazo
        return self.tasa_interes


class Plazo(InteresSimple):
    def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
        super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)

    def calcular_plazo(self):
        self.plazo = self.interes / (self.capital * self.tasa_interes)
        return self.plazo


# class EquivalerPlazo(InteresSimple):
#     def __init__(self, capital, tasa_interes, plazo, tipo_plazo, interes, monto):
#         super().__init__(capital, tasa_interes, plazo, tipo_plazo, interes, monto)
#         pass

interes_calculado = Interes(10000, 11, 5, "año", 0, 0)  # Creando una instancia
print(interes_calculado.calcular_interes())  # Llamando al método
