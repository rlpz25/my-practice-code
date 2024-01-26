while (True):

    #Pide la seleccion para el menu principal, y lo almacena en seleccion1
    seleccion1 = int(input("--- MENU ---\n1 Modelo Simple\n2 Modelo Exponencial\n3 Salir\nDigite un numero.\n"))

    #Modelo Simple
    if(seleccion1 == 1):

        #Pide la seleccion para el segundo menu, y lo almacena en seleccion2
        seleccion2 = int(input("--- MENU ---\n1 P = -γ*z+P₀\n2 P₂ = P₁-γ(z₂-z₁)\n3 Salir\nDigite un numero.\n"))

        #1 P = -γ*z+P₀
        if(seleccion2 == 1):

            #Pide la seleccion para el tercer menu, y lo almacena en seleccion3
            seleccion3 = int(input("¿Necesita calcular el peso especifico?\n1 Si\n2 No\n3 Salir\n"))

            #Si
            if(seleccion3 == 1):

                densidad = float(input("Ingrese la densidad del aire a cierta temperatura (ρ).\n"))
                gravedad = 9.807
                peso_especifico = densidad * gravedad
                z = float(input("Ingrese la altitud (m).\n"))
                presion_inicial = (float(input("Ingrese la presion inicial (atm).\n")))*101325
                presion = (-peso_especifico) * z + presion_inicial
                print("La presion es:\n", presion/101325, " atm.\n", presion, " Pa.\n")

            #No
            elif(seleccion3 == 2):

                peso_especifico = float(input("Ingrese el peso especifico (N/m³).\n"))
                z = float(input("Ingrese la altitud (m).\n"))
                presion_inicial = (float(input("Ingrese la presion inicial (atm).\n")))*101325
                resultado = (-peso_especifico) * z + presion_inicial
                print("La presion es:\n", resultado/101325, " atm.\n", resultado, " Pa.\n")

            #Salir
            elif(seleccion3 == 3):
                break

        #2 P₂ = P₁-γ(z₂-z₁)
        elif(seleccion2 == 2):

            seleccion3 = int(input("¿Necesita calcular el peso especifico?\n1 Si\n2 No\n3 Salir\n"))

            #Si
            if(seleccion3 == 1):
                
                densidad = float(input("Ingrese la densidad del aire a cierta temperatura (ρ).\n"))
                gravedad = 9.807
                peso_especifico = densidad * gravedad
                presion1 = float(input("Ingrese la presion 1 (atm).\n"))*101325
                altitud1 = float(input("Ingrese la altitud 1 (m).\n"))
                altitud2 = float(input("Ingrese la altitud 2 (m).\n"))
                presion2 = presion1 - peso_especifico * (altitud2 - altitud1)
                print("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n")

            #No
            elif(seleccion3 == 2):
                
                peso_especifico = float(input("Ingrese el peso especifico (N/m³).\n"))
                presion1 = float(input("Ingrese la presion 1 (atm).\n"))*101325
                altitud1 = float(input("Ingrese la altitud 1 (m).\n"))
                altitud2 = float(input("Ingrese la altitud 2 (m).\n"))
                presion2 = presion1 - peso_especifico * (altitud2 - altitud1)
                print("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n")

            #Salir
            elif(seleccion3 == 3):
                break
            
        #3 Salir
        elif(seleccion2 == 3):
            break


    #--------------------------------------------------------------------------------------
    #Modelo Exponencial
    elif(seleccion1 == 2):

        euler = 2.718281828
        Rg = 287.0
        gravedad = 9.807
        temperatura = float(input("Ingrese la temperatura (C).\n"))+273.15
        presion1 = float(input("Ingrese la presion 1 (atm).\n"))*101325
        altitud1 = float(input("Ingrese la altitud 1 (m).\n"))
        altitud2 = float(input("Ingrese la altitud 2 (m).\n"))
        presion2 = presion1*euler**-((gravedad/(Rg*temperatura))*(altitud2-altitud1))
        print("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n")


    #---------------------------------------------------------------------------------------
    #Salir
    elif(seleccion1 == 3):
        break
