class Pasajero:
    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

 
    def dni(self):
        return self.__dni

    def dni(self, valor):
        if not isinstance(valor, str) or not valor.isdigit() or len(valor) != 8:
            raise ValueError("El DNI debe tener exactamente 8 dígitos numéricos.")
        self.__dni = valor

    def nombre_completo(self):
        return self.__nombre_completo

    def nombre_completo(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena.")
        
        valor = valor.strip()
        if len(valor) < 5:
            raise ValueError("El nombre debe tener al menos 5 caracteres.")
        
        self.__nombre_completo = valor.title()

    def edad(self):
        return self.__edad

    def edad(self, valor):
        if not isinstance(valor, int):
            raise ValueError("La edad debe ser un número entero.")
        if valor < 0 or valor > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        
        self.__edad = valor

    def peso_equipaje(self):
        return self.__peso_equipaje

  
    def peso_equipaje(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El peso debe ser numérico.")
        if valor < 0 or valor > 25:
            raise ValueError("El peso del equipaje debe estar entre 0 y 25 kg.")
        
        self.__peso_equipaje = float(valor)


    def ruta(self):
        return self.__ruta

    def ruta(self, valor):
        rutas_validas = [
            "Iquitos-Nauta",
            "Iquitos-Yurimaguas",
            "Iquitos-Pucallpa",
            "Iquitos-Sta. Rosa"
        ]
        if valor not in rutas_validas:
            raise ValueError(f"Ruta inválida. Opciones válidas: {rutas_validas}")
        
        self.__ruta = valor

    def categoria_edad(self):
        if self.edad < 12:
            return "Niño"
        elif self.edad <= 17:
            return "Adolescente"
        elif self.edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    def tarifa_base(self):
        tarifas = {
            "Iquitos-Nauta": 25,
            "Iquitos-Sta. Rosa": 80,
            "Iquitos-Yurimaguas": 120,
            "Iquitos-Pucallpa": 180
        }
        return tarifas[self.ruta]

    def recargo_equipaje(self):
        if self.peso_equipaje <= 15:
            return 0
        else:
            exceso = self.peso_equipaje - 15
            return exceso * 2

    def tarifa_total(self):
        base = self.tarifa_base()

        if self.categoria_edad() in ["Niño", "Adulto mayor"]:
            base *= 0.5

        return base + self.recargo_equipaje()

    def __str__(self):
        return (
            "----- BOLETA DE PASAJERO -----\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre_completo}\n"
            f"Edad: {self.edad} ({self.categoria_edad()})\n"
            f"Ruta: {self.ruta}\n"
            f"Peso Equipaje: {self.peso_equipaje} kg\n"
            f"Tarifa Base: S/. {self.tarifa_base()}\n"
            f"Recargo Equipaje: S/. {self.recargo_equipaje()}\n"
            f"TOTAL A PAGAR: S/. {self.tarifa_total()}\n"
            "------------------------------"
        )


if __RONALDTORRES__ == "__main__":
    p1 = Pasajero("12345678", "juan perez lopez", 65, 18, "Iquitos-Nauta")
    print(p1)
