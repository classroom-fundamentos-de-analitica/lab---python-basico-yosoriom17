"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------
Este archivo contiene las preguntas que se van a realizar en el laboratorio.
No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.
Utilice el archivo `data.csv` para resolver las preguntas.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    secColum = [int(linea.split("\t")[1]) for linea in text if linea != '']
    return sum(secColum)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    dic = {}
    for linea in text:
        if(linea != ''):
            le = linea.split("\t")[0]
            dic[le] = dic.get(le, 0) + 1
    lista = (list(dic.items()))
    return sorted(lista)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    dic = {}
    for linea in text:
        if(linea != ''):
            lineSplit = linea.split("\t")
            le = lineSplit[0]
            dic[le] = dic.get(le, 0) + int(lineSplit[1])
    lista = (list(dic.items()))
    return sorted(lista)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        le = linea.split("\t")[2].split("-")[1]
        dic[le] = dic.get(le, 0) + 1
    lista = (list(dic.items()))
    return sorted(lista)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        lineSplit = linea.split("\t")
        num = int(lineSplit[1])
        val = dic.get(lineSplit[0], (num, num))
        dic[lineSplit[0]] = (max(val[0], num), min(val[1], num))
    lista = [(key, dic[key][0], dic[key][1]) for key in dic]
    return sorted(lista)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")[4].split(",")
        for l in li:
            cla,val = l.split(":")
            val = int(val)
            tupl = dic.get(cla, (val, val))
            dic[cla] = (min(tupl[0], val), max(tupl[1], val))
    lista = [(key, dic[key][0], dic[key][1]) for key in dic]
    return sorted(lista)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")
        num = int(li[1])
        val = dic.get(num, [])
        dic[num] = val + [li[0]]
    return sorted(dic.items())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")
        num = int(li[1])
        val = dic.get(num, [])
        if(li[0] not in val):
            dic[num] = val + [li[0]]
    lista = [(key, sorted(dic[key])) for key in dic]
    return sorted(lista)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")[4].split(",")
        for l in li:
            cla,_ = l.split(":")
            val = dic.get(cla, 0)
            dic[cla] = val + 1
    return dict(sorted(dic.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    lista = []
    for linea in text:
        li = linea.split("\t")
        lista.append((li[0], len(li[3].split(",")), len(li[4].split(","))))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")
        num = int(li[1])
        for letra in li[3].split(","):
            val = dic.get(letra, 0)
            dic[letra]  = val + num
    return dict(sorted(dic.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    archivo = open("data.csv")
    text = archivo.read().split("\n")
    archivo.close()
    text.pop()
    dic = {}
    for linea in text:
        li = linea.split("\t")
        suma = sum([int(num) for num in [a for l in li[4].split(",") for a in l.split(":")][1::2]])
        val = dic.get(li[0], 0)
        dic[li[0]] = val + suma
    return dict(sorted(dic.items()))