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

                    if (type(notas) == pd.DataFrame):
                        # Comprobar si las llaves son objetos Asignatura y los valores son enteros o decimales, y validos.
                        # TODO: Comprobar si no tiene la llave notas para tirar un error de tipo KeyError custom.
                        if (not notas.empty):
                            if ("Asignaturas" in notas.keys() and "Notas" in notas.keys()):
                                for asignatura in notas["Asignaturas"]:
                                    if (not isinstance(asignatura, Asignatura)):
                                        raise TypeError("La columna 'Asignaturas' solo puede contener objetos de tipo Asignatura.")
                                    if (asignatura not in asignaturas):
                                            raise RuntimeError(f"El alumno {nombre} no tiene la asignatura {asignatura.nombre} matriculada, y por lo tanto no puede recibir una nota en ella.")

                                for nota in notas["Notas"]:
                                    if (type(nota) not in [int, float]):
                                        raise TypeError("La columana 'Notas' solo puede tener notas con valores de tipo int o float.")
                                    if (nota < 0 or nota > 10):
                                        raise ValueError("Las notas solo pueden estar entre 0 y 10.")

                            else:
                                raise KeyError('El DataFrame notas tiene que tener las llaves "Asignatura" y "Notas".')
                            # El diccionario esta correcto o es vacio
                            self.nombre = nombre
                            self.asignaturas = asignaturas
                            self.notas = notas
                    else:
                        raise TypeError("La variable notas tiene que ser de tipo DataFrame de Pandas, con llave 'Asignaturas' conteniendo objetos Asignatura, y la llave 'Notas' conteniendo notas entre 0 a 10.")
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

    def poner_nota(self, asignaturaInput, nota):
        if (isinstance(asignaturaInput, Asignatura)):
            # TODO: Detectar si la asignatura ya esta con una nota, y si lo esta cambiar la nota en vez de concatenar.
            # Busqueda lineal
            i = 0

            while (i < len(self.asignaturas) - 1 and self.asignaturas[i] != asignaturaInput):
                i += 1
            
            if (self.asignaturas[i] == asignaturaInput):
                if (type(nota) in [int, float]):
                    if (0 <= nota <= 10):
                        self.notas = pd.concat([self.notas, pd.DataFrame({"Asignaturas": [asignaturaInput], "Notas": [nota]})])
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
            # Comprobar si la lista alumnos solo contiene objetos Alumno
            for alumno in alumnos:
                if (not isinstance(alumno, Alumno)):
                    raise TypeError("La lista alumnos solo puede contener objetos de tipo Alumno.")

            # La lista solo tiene objetos Alumno
            self.alumnos = alumnos
        else:
            raise TypeError("La variable alumnos tiene que ser una lista de objetos tipo Alumno.")

    def aniadir_alumno(self, alumno):
        if (isinstance(alumno, Alumno)):
            self.alumnos.append(alumno)
        else:
            print("La variable alumno tiene que ser un objeto de tipo Alumno.")

    def mostrar_expediente(self, nombre_alumno):
        if (type(nombre_alumno) == str):
            if (nombre_alumno != ""):
                # Busqueda lineal
                i = 0
                while (i < len(self.alumnos) - 1 and self.alumnos[i].nombre != nombre_alumno):
                    i += 1

                if (self.alumnos[i].nombre == nombre_alumno):
                    # Alumno encontrado
                    alumno_buscado = self.alumnos[i]

                    # Preparar y mostrar el mensaje de las asignaturas matriculadas.
                    if (len(alumno_buscado.asignaturas) != 0):
                        mensaje_asignaturas = f"El alumno {nombre_alumno} tiene las siguientes asignaturas matriculadas: "
                        asignaturas = alumno_buscado.asignaturas
                        if (len(asignaturas) > 1):
                            for indice in range(0, len(asignaturas) - 1):
                                asignaturaMatriculada = asignaturas[indice]
                                mensaje_asignaturas += f"{asignaturaMatriculada.nombre} con {asignaturaMatriculada.creditos} de creditos universitarios, "

                            asignaturaMatriculada = asignaturas[len(asignaturas) - 1]
                            mensaje_asignaturas += f"y {asignaturaMatriculada.nombre} con {asignaturaMatriculada.creditos} de creditos universitarios."
                            print(mensaje_asignaturas)
                        else:
                            print(mensaje_asignaturas + f"{alumno_buscado.asignaturas[0].nombre} con {alumno_buscado.asignaturas[0].creditos} de creditos universitarios.")

                        # Preparar y mostrar el mensaje de las notas.
                        if (len(alumno_buscado.notas) != 0): 
                            mensaje_notas = "Tiene las siguientes notas por asignatura: "

                            if (len(alumno_buscado.notas) > 1):
                                notas = alumno_buscado.notas
                                for indice in range(0, len(notas) - 1):
                                    asignaturaConNota = list(notas.keys())[indice]
                                    nota = notas[asignaturaConNota]
                                    mensaje_notas += f"{nota} en la asignatura {asignaturaConNota.nombre}, "

                                asignaturaConNota = list(notas.keys())[len(notas) - 1]
                                nota = notas[asignaturaConNota]
                                mensaje_notas += f"y {nota} en la asignatura {asignaturaConNota.nombre}."
                                print(mensaje_notas)
                            else:
                                asignaturaConNota = list(alumno_buscado.notas.keys())[0]
                                nota = alumno_buscado.notas[asignaturaConNota]
                                print(mensaje_notas + f"{nota} en la asignatura {asignaturaConNota.nombre}.")
                                

                            alumno_buscado.media()
                        else:
                            print("Todavia no tiene notas en sus asignaturas.")
                    else:
                        print(f"El alumno {nombre_alumno} no tiene asignaturas matriculadas.")
                else:
                    print(f"El alumno con el nombre {nombre_alumno} no ha sido encontrado.")
            else:
                print("El nombre del alumno a buscar no puede estar vacio.")
        else:
            print("La variable nombre_alumno tiene que ser de tipo string.")

pro = Asignatura("Programación", 312)
djk = Asignatura("Digitalización", 104)
itk = Asignatura("Itinerancia", 156)
ssf = Asignatura("Sistemas", 260)
bae = Asignatura("Bases de Datos", 260)
lnd = Asignatura("Lenguajes de Marca", 208)
ets = Asignatura("Entornos de Desarollo", 156)

aromgon = Alumno("Alejandro", [pro, djk, ets], pd.DataFrame(
    {
        "Asignaturas": [
            pro,
            djk,
            ets
        ],

        "Notas": [
            7,
            6,
            9
        ]
    }
))
agongon = Alumno("Andrea", [pro, djk, itk, ssf, bae, lnd, ets], pd.DataFrame(
    {
        "Asignaturas": [
            djk,
            itk,
            ssf,
            bae,
            lnd,
            ets
        ],

        "Notas": [
            7,
            6.3,
            10,
            4,
            5,
            8.5
        ]
    }
))
fromgom = Alumno("Fernando", [pro], pd.DataFrame(
    {
        "Asignaturas": [ pro ],
        "Notas": [ 7.8 ]
    }
))

aromchi = Alumno("Alonso", [], pd.DataFrame({}))

# TODO: Descomentar una vez termine refactorizando
"""
cifpcm_daw = Instituto([aromgon, agongon, fromgom])

agongon.poner_nota(pro, 7.4)

fromgom.matricular(ets)
fromgom.poner_nota(ets, 6.2)

cifpcm_daw.aniadir_alumno(aromchi)
aromchi.matricular(bae)

cifpcm_daw.mostrar_expediente("Alejandro")
print()
cifpcm_daw.mostrar_expediente("Andrea")
print()
cifpcm_daw.mostrar_expediente("Fernando")
print()
cifpcm_daw.mostrar_expediente("Alonso")
"""
