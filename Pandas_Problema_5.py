# Problema 5
# Esta implementacion supone que los creditos academicos son sin decimales.

import pandas as pd

class Asignatura:
    # Metodo constructor
    def __init__(self, nombre, creditos):
        if (type(nombre) == str):
            if (nombre != ""):
                if (type(creditos) == int):
                    if (creditos > 0):
                        self.nombre = nombre
                        self.creditos = creditos
                    else:
                        raise ValueError("Los creditos academicos no pueden ser negativos.")
                else:
                    raise TypeError("La variable creditos tiene que ser de tipo int.")
            else:
                raise ValueError("El nombre de la asignatura no puede estar vacio.")
        else:
            raise TypeError("La variable nombre tiene que ser de tipo string.")

class Alumno:
    # Metodo constructor
    def __init__(self, nombre, asignaturas, notas):
        if (type(nombre) == str):
            if (nombre != ""):
                if (type(asignaturas) == list):
                    # Comprobar si la lista asignaturas solo contiene objetos Asignatura
                    for asignatura in asignaturas:
                        if (not isinstance(asignatura, Asignatura)):
                            raise TypeError("La lista asignaturas solo puede contener objetos de tipo Asignatura.")

                    # La lista solo tiene objetos Asignatura

                    if (type(notas) == dict):
                        # Comprobar si las llaves son objetos Asignatura y los valores son enteros o decimales, y validos.
                        for asignatura, nota in notas.items():
                            if (not isinstance(asignatura, Asignatura)):
                                raise TypeError("Las llaves del diccionario de notas solo pueden ser objetos de tipo Asignatura.")
                            if (asignatura not in asignaturas):
                                raise RuntimeError(f"El alumno {nombre} no tiene la asignatura {asignatura.nombre} matriculada, y por lo tanto no puede recibir una nota en ella.")
                            if (type(nota) not in [int, float]):
                                raise TypeError("Los valores del diccionario de notas solo pueden ser de tipo int o float.")
                            if (nota < 0 or nota > 10):
                                raise ValueError("Las notas dentro del diccionario notas solo pueden estar entre 0 y 10.")

                        # El diccionario esta correcto
                        self.nombre = nombre
                        self.asignaturas = asignaturas
                        self.notas = pd.DataFrame(data = notas.values(), index = notas.keys(), columns = [nombre])
                        # Añadir un titulo a la columna de indices (asignaturas)
                        self.notas.index.name = "Asignaturas"
                    else:
                        raise TypeError("La variable notas tiene que ser de tipo Diccionario, con llaves de tipo Asignatura, y notas entre 0 a 10.")
                else:
                    raise TypeError("La variable asignaturas tiene que ser una lista de objetos tipo Asignatura.")
            else:
                raise ValueError("El nombre del alumno no puede estar vacio.")
        else:
            raise TypeError("La variable nombre tiene que ser de tipo string.")

    def matricular(self, asignatura):
        if (isinstance(asignatura, Asignatura)):
            # Busqueda lineal
            i = 0
            while (i < len(self.asignaturas) - 1 and self.asignaturas[i].nombre != asignatura.nombre):
                i += 1

            if (len(self.asignaturas) == 0 or self.asignaturas[i].nombre != asignatura.nombre):
                self.asignaturas.append(asignatura)
            else:
                print("El alumno ya estaba matriculado en esta asignatura.")
        else:
            print("La variable asignatura tiene que ser un objeto de tipo Asignatura.")

    def poner_nota(self, asignatura, nota):
        if (isinstance(asignatura, Asignatura)):
            # Busqueda lineal
            i = 0
            while (i < len(self.asignaturas) - 1 and self.asignaturas[i] != asignatura):
                i += 1

            if (self.asignaturas[i] == asignatura):
                if (type(nota) in [int, float]):
                    if (0 <= nota <= 10):
                        if (asignatura in self.notas.index):
                            # La asignatura ya esta en el DataFrame, actualizar la nota.
                            self.notas.loc[asignatura, self.nombre] = nota
                        else:
                            # La asignatura no esta en el DataFrame, concatenarla junto a la nota.
                            self.notas = pd.concat([self.notas, pd.DataFrame(data = [nota], index = [asignatura], columns = [self.nombre])])
                            
                            # Escribir de nuevo el nombre del la columna de los indices (Es sobreescrito por la operación anterior)
                            self.notas.index.name = "Asignaturas"
                    else:
                        print("La nota tiene que estar entre 0 y 10.")
                else:
                    print("La variable nota tiene que ser de tipo int o float.")
            else:
                print("El alumno no esta matriculado en esta asignatura.")
        else:
            print("La variable asignatura tiene que ser un objeto de tipo Asignatura.")

    def media(self):
        print(f"El alumno {self.nombre} tiene una media de {round(sum(self.notas.values()) / len(self.notas.values()), 2)}.")

class Instituto:
    # Metodo constructor
    def __init__(self, alumnos):
        if (type(alumnos) == list):
            if (len(alumnos) != 0):
                # Comprobar si la lista alumnos solo contiene objetos Alumno
                for alumno in alumnos:
                    if (not isinstance(alumno, Alumno)):
                        raise TypeError("La lista alumnos solo puede contener objetos de tipo Alumno.")

                # La lista solo tiene objetos Alumno
                self.alumnos = alumnos
            else:
                raise ValueError("La lista alumnos no puede estar vacia.")
        else:
            raise TypeError("La variable alumnos tiene que ser una lista de objetos tipo Alumno.")

    def aniadir_alumno(self, alumno):
        if (isinstance(alumno, Alumno)):
            self.alumnos.append(alumno)
        else:
            print("La variable alumno tiene que ser un objeto de tipo Alumno.")

    def mostrar_expediente(self):
        # TODO: Hacer que los objetos Asignatura en la tabla muestren su nombre
        # TODO: Asignar "Sin nota" en las notas cuando haya una asignatura matriculada, pero no tenga nota
        # TODO: Asignar "No matriculada" en las notas cuando no este matriculada en una asignatura.
        expediente = pd.DataFrame()

        for alumno in self.alumnos:
            expediente = pd.concat([expediente, alumno.notas], axis=1)

        print(expediente)


pro = Asignatura("Programación", 312)
djk = Asignatura("Digitalización", 104)
itk = Asignatura("Itinerancia", 156)
ssf = Asignatura("Sistemas", 260)
bae = Asignatura("Bases de Datos", 260)
lnd = Asignatura("Lenguajes de Marca", 208)
ets = Asignatura("Entornos de Desarollo", 156)

aromgon = Alumno("Alejandro", [pro, djk, ets], {pro: 7, djk: 6, ets: 9})
agongon = Alumno("Andrea", [pro, djk, itk, ssf, bae, lnd, ets], {djk: 7, itk: 6.3, ssf: 10, bae: 4, lnd: 5, ets: 8.5})
fromgom = Alumno("Fernando", [pro], {pro: 7.8})
aromchi = Alumno("Alonso", [], {})

cifpcm_daw = Instituto([aromgon, agongon, fromgom])

agongon.poner_nota(pro, 7.4)

fromgom.matricular(ets)
fromgom.poner_nota(ets, 6.2)

cifpcm_daw.aniadir_alumno(aromchi)
aromchi.matricular(bae)

cifpcm_daw.mostrar_expediente()
