Proceso Ejercicio2
	
//Se declaran las variables que se van a utilizar.
	Definir LLU, i, j, k Como Entero;
	Definir arregloA, arregloB, arregloC Como Entero;
	Definir resultadoA, resultadoB, resultadoC Como Entero;
	Dimension LLU[24,12,10];
	Dimension arregloA[24];
	Dimension arregloB[24];
	Dimension arregloC[12];
	
//Se generan los registros con numeros al azar.
	Escribir "Generando registros...";
	Para i<-0 Hasta 23 Con Paso 1 Hacer
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 9 Con Paso 1 Hacer
				LLU[i,j,k] <- azar(30)+1;
			FinPara
		FinPara
	FinPara
	Escribir "Registros generados.";
	
//Se inicializan los valores de los arreglos auxiliares.
	Para i<-0 Hasta 23 Con Paso 1 Hacer
		arregloA[i] <- 0;
		arregloB[i] <- 0;
	FinPara
	
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		arregloC[i] <- 0;
	FinPara
	
//Se rellenan los arreglos auxiliares con los datos a comparar.
	Escribir "";
	Escribir "";
	Para i<-0 Hasta 23 Con Paso 1 Hacer
		Escribir "";
		Escribir "Provincia ", i+1;
		Para j<-0 Hasta 11 Con Paso 1 Hacer
			Para k<-0 Hasta 9 Con Paso 1 Hacer
				Escribir "El mes ", j+1, " del año ", k+1, " hubieron ", LLU[i,j,k], " precipitaciones registradas.";
				arregloA[i] <- arregloA[i] + LLU[i,j,k];
				Si k = 9 Entonces
					arregloB[i] <- arregloB[i] + LLU[i,j,k];
				FinSi
				Si k = 4 Y i = 17 Entonces
					arregloC[j] <- arregloC[j] + LLU[i,j,k];
				FinSi
			FinPara
		FinPara
	FinPara
	
//Se comparan los datos para seleccionar el más apto.
	resultadoA <- 0;
	resultadoB <- 0;
	resultadoC <- 0;
	Para i<-0 Hasta 23 Con Paso 1 Hacer
		Si arregloA[resultadoA] < arregloA[i] Entonces
			resultadoA <- i;
		FinSi
		Si arregloB[resultadoB] > arregloB[i] Entonces
			resultadoB <- i;
		FinSi
	FinPara
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		Si arregloC[resultadoC] < arregloC[i] Entonces
			resultadoC <- i;
		FinSi
	FinPara
	
//Se muestran los resultados al usuario
	Escribir "";
	Escribir "";
	Escribir "";
	Escribir "La provincia que tuvo el mayor registro de precipitaciones pluviales en los ultimos 10 años es la provincia ", resultadoA+1, " con ", arregloA[resultadoA], " registros.";
	Escribir "La provincia que tuvo el menor registro de precipitaciones pluviales en el ultimo año es la provincia ", resultadoB+1, " con ", arregloB[resultadoB], " registros.";
	Escribir "El mes que tuvo mayor registro de lluvias en la provincia 18 el 5to año es el mes ", resultadoC+1, " con ", arregloC[resultadoC], " registros.";
FinProceso