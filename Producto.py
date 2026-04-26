class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


    def clasificar(self):
        if self.categoria == "tecnología":
            if self.precio > 2000000:
                return "Lujo"
            else:
                return "Básico"
        elif self.categoria == "alimentos":
            if self.precio > 100000:
                return "Lujo"
            else:
                return "Básico"
        elif self.categoria == "ropa":
            if self.precio > 300000:
                return "Lujo"
            else:
                return "Básico"
        else:
            return "Desconocido"