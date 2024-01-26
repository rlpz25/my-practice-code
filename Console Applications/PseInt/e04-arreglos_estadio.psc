Proceso Ejercicio4
	
	//Se declaran las variables que se van a utilizar.
	Definir FUT, i, j, k, pos_menor, aux, aux2 Como Entero;
	Definir arregloA, arregloA2, arregloB, arregloC, arregloC2 como entero;
	Definir resultadoA, resultadoB1, resultadoB2 Como Entero;
	Dimension FUT[10,12,5];
	Dimension arregloA[10];
	Dimension arregloA2[10];
	Dimension arregloB[10];
	Dimension arregloC[10];
	Dimension arregloC2[10];
	
	//Se rellena el arreglo principal con datos al azar, los cuales representan el numero de asistentes al estadio en cada casilla.
	Escribir "Generando registros...";
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				FUT[i,j,k] <- azar(1000000)+1;
			FinPara
		FinPara
	FinPara
	Escribir "Registros generados.";
	
	//Se inicializan los arreglos auxiliares.
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		arregloA[i] <- 0;
		arregloA2[i] <- i+1;
		arregloB[i] <- 0;
		arregloC[i] <- 0;
		arregloC2[i] <- 0;
	FinPara
	
	Escribir "";
	Escribir "";
	//Se realiza el primer recorrido del arreglo principal con el objetivo de extraer datos manejables y
	//almacenarlos en arreglos auxiliares.
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir "";
		Escribir "Estadio ", i+1;
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				Escribir "El mes ", j+1, " en el a�o ", k+1, " se registraron ", FUT[i,j,k], " visitas.";
				//Extrae datos del ultimo a�o
				Si k = 4 Entonces
					//Almacena el numero de asistentes a cada estadio
					arregloA[i] <- arregloA[i] + FUT[i,j, k];
					//Selecciona el mejor mes de cada estadio
					Si arregloC[i] < FUT[i,j,k] Entonces
						arregloC[i] <- FUT[i,j,k];
						arregloC2[i] <- j;
					FinSi
				FinSi
				//Almacena el numero de visitantes para cada estadio en los ultimos 5 a�os
				arregloB[i] <- arregloB[i] + FUT[i,j,k];
			FinPara
		FinPara
	FinPara
	
	//Se ordena el arreglo de las visitas del estadio
	//Posteriormente se definira el orden de impresion de los datos.
	//arregloA2 y aux2 unicamente almacenan la referencia para especificar de que estadio se habla.
	Para i <- 0 hasta 8 hacer
		pos_menor <- i;
		Para j <- i+1 Hasta 9 Hacer
			Si arregloA[j] < arregloA[pos_menor] Entonces
				pos_menor <- j;
			FinSi
		FinPara
		aux <- arregloA[i];
		aux2 <- arregloA2[i];
		arregloA[i] <- arregloA[pos_menor];
		arregloA2[i] <- arregloA2[pos_menor];
		arregloA[pos_menor] <- aux;
		arregloA2[pos_menor] <- aux2;
	FinPara
	
	//Se selecciona el mayor y menor numero de asistentes.
	resultadoB1 <- 0;
	resultadoB2 <- 0;
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Si arregloB[resultadoB1] > arregloB[i] Entonces
			resultadoB1 <- i;
		FinSi
		Si arregloB[resultadoB2] < arregloB[i] Entonces
			resultadoB2 <- i;
		FinSi
	FinPara
	
	//Se muestran los resultados al usuario.
	Escribir "";
	Escribir "";
	//Inciso A
	Escribir "El numero de asistentes del ultimo año en cada estadio, ordenados de mayor a menor son los siguientes:";
	//Imprime una lista ordenada de mayor a menor
	Para i <- 9 hasta 0 Con Paso -1 hacer
		Escribir "El estadio ", arregloA2[i], " tuvo ",arregloA[i], " asistentes.";
	FinPara
	Escribir "";
	//Inciso B
	Escribir "El estadio que tuvo la menor afluencia en los ultimos cinco años fue el estadio ", resultadoB1+1, " con ", arregloB[resultadoB1], " asistentes.";
	Escribir "El estadio que tuvo la mayor afluencia en los ultimos cinco años fue el estadio ", resultadoB2+1, " con ", arregloB[resultadoB2], " asistentes.";
	Escribir "";
	//Inciso C
	Escribir "El mejor mes del ultimo año para cada estadio es el siguiente:";
	//Imprime una lista que describe el mejor mes para cada estadio.
	Para i <- 0 hasta 9 hacer
		Escribir "Para el estadio ", i+1, " fue el mes ", arregloC2[i]+1, " con ",arregloC[i], " asistentes.";
	FinPara
	
FinProceso
