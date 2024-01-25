# El programa recibe dos listas
# La primera lista es el diccionario
# La segunda lista es el query
# Crear una funcion que devuelva las coincidencias

dic = ["abd", "hola", "diccionario", "loha", "halo", "bda"]
que = ["bad", "aloh", "dab", "dicnariocio"]

def searchCo(dictionary, query):

    result = []

    # wq: palabra actual de query
    for wq in query:

        # print("Query: " + wq)

        qlaux = []
        counter = 0

        for ch in wq:
            qlaux.append(ch)

        # qlaux almacena los caracteres de la palabra actual de query
        qlaux.sort()
        # print(qlaux)
        
        # wd: palabra actual de dictionary
        for wd in dictionary:

            dlaux = []

            if (len(wd) == len(wq)):

                # print("Dictionary: " + wd)
                for ch in wd:
                    dlaux.append(ch)
                
                # dlaux almacena los caracteres de la palabra actual de dictionary
                dlaux.sort()

                if (qlaux == dlaux):
                    # print("Son iguales, counter: " + str(counter))
                    counter = counter + 1
        
        # print("Counter tras recorrido: "+ str(counter))
        result.append(counter)

    print(result)

searchCo(dic, que)

        

