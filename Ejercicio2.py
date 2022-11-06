class alumno:
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print("El alumno se ha creado con éxito\n")
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)


    def califiacion(self):
        if self.nota>=5:
           print(self.nombre, "ha aprobado")
        else:
           print(self.nombre, "ha suspendido")
    
    def __str__(self):
        return "{}, ha sacado un: {}".format(self.nombre, self.nota)

alumno1=Alumno("Jaime", 5)
alumno1.califiacion()

print("\n\n")

alumno2=Alumno("Alberto", 3)
alumno2.califiacion()

print("\n\n")


       