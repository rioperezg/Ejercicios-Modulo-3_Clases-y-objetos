print("\n\n")
class product:
    def __init__(self, codigo, nombre, precio, tipo):
     print("El producto se ha creado con éxito\n")
     self.codigo= codigo
     self.nombre= nombre
     self.precio= precio
     self.tipo = tipo

    def __str__(self):
        return "El código de el/la {1} es {0}, su precio es de {2}$ y es {3}".format(self.codigo, self.nombre, self.precio, self.tipo)


producto1=product(71864527, "manzana", 1, "alimento")
print(producto1)

print("\n\n")

producto2=product(7823498, "camiseta", 15, "ropa")
print(producto2)

print("\n\n")

producto3=product(2674612678, "ordenador", 700, "electrónica")
print(producto3) 
    
