Proceso Ejercicio5
	
	//Se definen las variables que se usaran.
	Definir PRO, i, j, k Como Entero;
	Definir arregloA, arregloB Como Entero;
	Definir resultadoA, resultadoB, resultadoC Como Entero;
	Dimension  PRO[12,3,8];
	Dimension arregloA[12];
	Dimension arregloB[3];
	resultadoA <- 0;
	resultadoC <- 0;
	
	//Se generan los registros con numeros de venta al azar
	Escribir "Generando registros...";
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		Para j<-0 Hasta 2 Con Paso 1 Hacer
			Para k<-0 Hasta 7 Con Paso 1 Hacer
				PRO[i,j,k] <- azar(1000)+1;
			FinPara
		FinPara
	FinPara
	Escribir "Registros generados.";
	
	
	//Se inicializan los arreglos auxiliares.
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		arregloA[i] <- 0;
	FinPara
	
	arregloB[0] <- 0;
	arregloB[1] <- 0;
	arregloB[2] <- 0;
	
	//Se rellenan los arreglos auxiliares con los datos de las ventas.
	Escribir "";
	Escribir "";
	Para i<-0 Hasta 11 Con Paso 1 Hacer
		Escribir "";
		Escribir "Mes ", i+1;
		Para j<-0 Hasta 2 Con Paso 1 Hacer
			Para k<-0 Hasta 7 Con Paso 1 Hacer
				Escribir "El departamento ", j+1, " en el año ", k+1, " realizo ", PRO[i,j,k], " en ventas.";
				Si k = 1 Entonces
					resultadoA <- resultadoA + PRO[i,j,k];
				FinSi
				Si k = 7 Entonces
					arregloA[j] <- arregloA[j] + PRO[i,j,k];
				FinSi
				Si resultadoC < PRO[i,j,k] Entonces
					resultadoC <- PRO[i,j,k];
					arregloB[0] <- i;
					arregloB[1] <- j;
					arregloB[2] <- k;
				FinSi
			FinPara
		FinPara
	FinPara
	
	
	//Se comparan los datos de los arreglos auxiliares.
	resultadoB <- 0;
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Si arregloA[resultadoB] < arregloA[i] Entonces
			resultadoB <- i;
		FinSi
	FinPara
	
	//Se muestran los resultados al usuario.
	Escribir "";
	Escribir "";
	Escribir "";
	Escribir "Las ventas totales de la empresa en el segundo año fueron de ", resultadoA;
	Escribir "El departamento que tuvo mayores ventas en el ultimo año es el departamento ", resultadoB+1, " con ", arregloA[resultadoB], " en ventas.";
	Escribir "El departamento con mayor venta fue el departamento ", arregloB[1]+1, " en el mes ", arregloB[0]+1, " del a�o ", arregloB[2]+1, " con ", resultadoC, " en ventas.";
FinProceso