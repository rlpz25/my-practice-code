#####P = -γ*z+P₀ Sin calcular el peso especifico
#Ingrese el peso especifico (N/m³).
peso_especifico <- 12.0290
#Ingrese la altitud (m).
altitud <- 500
#Ingrese la presion inicial (atm).
presion_inicial <- 1
#Calculo automatico
presion_inicial_pascales <- presion_inicial*101325 
presion <- (-peso_especifico) * altitud + presion_inicial_pascales
cat(paste0("La presion es:\n", presion/101325, " atm.\n", presion, " Pa."))

#####P = -γ*z+P₀ Calculando el peso especifico
#Ingrese la densidad del aire a cierta temperatura (ρ).
densidad <- 1.269
#Ingrese la altitud (m).
altitud <- 500
#Ingrese la presion inicial (atm).
presion_inicial <- 1
#Calculo automatico
gravedad <- 9.807
peso_especifico <- densidad * gravedad
presion_inicial_pascales <- presion_inicial*101325 
presion <- (-peso_especifico) * altitud + presion_inicial_pascales
cat(paste0("La presion es:\n", presion/101325, " atm.\n", presion, " Pa."))



#####P₂ = P₁-γ(z₂-z₁) Sin calcular el peso especifico
#Ingrese el peso especifico (N/m³).
peso_especifico <- 12.01
#Ingrese la presion 1 (atm).
presion1 <- 0.98
#Ingrese la altitud 1 (m).
altitud1 <- 150
#Ingrese la altitud 2 (m).
altitud2 <- 500
#Calculo automatico
presion1_pascales <- presion1*101325
presion2 <- presion1_pascales - peso_especifico * (altitud2 - altitud1)
cat(paste0("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n"))

#####P₂ = P₁-γ(z₂-z₁) Calculando el peso especifico
#Ingrese la densidad del aire a cierta temperatura (ρ).
densidad <- 1.269
#Ingrese la presion 1 (atm).
presion1 <- 0.98
#Ingrese la altitud 1 (m).
altitud1 <- 150
#Ingrese la altitud 2 (m).
altitud2 <- 500
#Calculo automatico
gravedad <- 9.807
presion1_pascales <- presion1*101325
peso_especifico <- densidad * gravedad
presion2 <- presion1_pascales - peso_especifico * (altitud2 - altitud1)
cat(paste0("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n"))



#####Modelo exponencial
#Ingrese la presion 1 (atm).
presion1 <- 1
#Ingrese la altitud 1 (m).
altitud1 <- 0
#Ingrese la altitud 2 (m).
altitud2 <- 2250
#Ingrese la temperatura (C).
temperatura <- 15
#Calculo automatico
euler <- 2.718281828
Rg <- 287.0
gravedad <- 9.807
temperatura_k <- temperatura + 273.15
presion1_pascales <- presion1*101325
presion2 <- presion1_pascales * euler ^ - ((gravedad / (Rg * temperatura_k)) * (altitud2 - altitud1))
cat(paste0("La presion 2 es:\n", presion2/101325, " atm.\n", presion2, " Pa.\n"))