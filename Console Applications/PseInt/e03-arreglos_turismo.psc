Proceso Ejercicio3
	
	//Se declaran las variables a utilizar.
	Definir SEC, i, j, k Como Entero;
	Definir arregloA, arregloC Como Entero;
	Definir resultadoB1, resultadoB2, resultadoC1, resultadoC2 Como Entero;
	Dimension SEC[10,12,5];
	Dimension arregloA[10];
	Dimension arregloC[12];
	
	//Se generan los registros con visitas automáticas.
	Escribir "Generando registros...";
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				SEC[i,j,k] <- azar(50)+1;
			FinPara
		FinPara
	FinPara
	Escribir "Registros generados.";
	
	//Se inicializan los valores de los arreglos auxiliares.
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		arregloA[i] <- 0;
	FinPara
	
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		arregloC[i] <- 0;
	FinPara
	
	//Se asignan los valores a los arreglos auxiliares para su posterior comparaci�n.
	Escribir "";
	Escribir "";
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir "";
		Escribir "Centro tur�stico ", i+1;
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				Escribir "El mes ", j+1, " en el año ", k+1, " se registraron ", SEC[i,j,k], " visitas.";
				arregloA[i] <- arregloA[i] + SEC[i,j,k];
				Si k = 4 Entonces
					arregloC[j] <- arregloC[j] + SEC[i,j,k];
				FinSi
			FinPara
		FinPara
	FinPara
	
	//Se comparan los valores de los arreglos y se selecciona el m�s apto.
	resultadoB1 <- 0;
	resultadoB2 <- 0;
	Para i <- 0 Hasta 9 Con Paso 1 Hacer
		Si arregloA[resultadoB1] > arregloA[i] Entonces
			resultadoB1 <- i;
		FinSi
		Si arregloA[resultadoB2] < arregloA[i] Entonces
			resultadoB2 <- i;
		FinSi
	FinPara
	resultadoC1 <- 0;
	resultadoC2 <- 0;
	Para i <- 0 Hasta 11 Con Paso 1 Hacer
		Si arregloC[resultadoC1] > arregloC[i] Entonces
			resultadoC1 <- i;
		FinSi
		Si arregloC[resultadoC2] < arregloC[i] Entonces
			resultadoC2 <- i;
		FinSi
	FinPara
	
	//Se muestran los resultados en pantalla.
	Escribir "";
	Escribir "";
	Para i <- 0 Hasta 9 Con Paso 1 Hacer
		Escribir "Visitas al centro turistico ", i+1, ": ", arregloA[i];
	FinPara
	Escribir "";
	Escribir "El centro turistico menos visitado en los ultimos cinco años es: Centro tur�stico ", resultadoB1+1, " con ", arregloA[resultadoB1], " visitas.";
	Escribir "El centro turistico mas visitado en los ultimos cinco años es: Centro tur�stico ", resultadoB2+1, " con ", arregloA[resultadoB2], " visitas.";
	Escribir "";
	Escribir "El mes del ultimo año con menor afluencia turistica es el mes ", resultadoC1+1, " con ", arregloC[resultadoC1], " visitantes.";
	Escribir "El mes del ultimo año con mayor afluencia turistica es el mes ", resultadoC2+1, " con ", arregloC[resultadoC2], " visitantes.";
FinProceso
