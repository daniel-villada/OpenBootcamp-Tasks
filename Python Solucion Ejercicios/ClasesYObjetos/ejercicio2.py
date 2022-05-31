class Alumno:
    def data(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def showData(self):
        print(f"Nombre del alumno: {self.nombre}\nNota: {self.nota}")

    def results(self):
        if self.nota < 5:
            print("El alumno no ha aprobado")
        else:
            print("El alumno ha aprobado")

alumno1 = Alumno()

alumno1.data("Daniel", 8)
alumno1.showData()
alumno1.results()