Proceso Ejercicio7
	
//Se declaran las variables a utilizar.
	Definir UNI, i, j, k Como Entero;
	Definir alumnosAnyo, alumnosCarrUltAnyo, alumnosCA como entero;
	Definir resultadoA, resultadoB, resultadoC Como Entero;
	Definir carreras Como Caracter;
	Dimension UNI[8,2,5];
	Dimension alumnosAnyo[5];
	Dimension alumnosCarrUltAnyo[8];
	Dimension alumnosCA[5];
	Dimension carreras[8];
	
//Se rellena el arreglo auxiliar que corresponde a las carreras.
	carreras[0] <- "Contabilidad";
	carreras[1] <- "Administracion";
	carreras[2] <- "Economia";
	carreras[3] <- "Relaciones Internacionales";
	carreras[4] <- "Matematicas";
	carreras[5] <- "Ingenieria en Computacion";
	carreras[6] <- "Ingenieria Industrial";
	carreras[7] <- "Ingenieria en Telematica";
	
//Se rellena el arreglo tridimensional con valores al azar.
	Escribir "Generando registros...";
	Para i<-0 Hasta 7 Con Paso 1 Hacer
		Para j<-0 Hasta 1 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				UNI[i,j,k] <- azar(100)+1;
			FinPara
		FinPara
	FinPara
	Escribir "Registros generados.";
	
//Se inicializan los arreglos auxiliares.
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		alumnosAnyo[i] <- 0;
		alumnosCA[i] <- 0;
	FinPara
	
	Para i<-0 Hasta 7 Con Paso 1 Hacer
		alumnosCarrUltAnyo[i] <- 0;
	FinPara
	
//Se asignan los valores a arreglos auxiliares, los cuales serviran para comparar posteriormente.
	Escribir "";
	Escribir "";
	Para i<-0 Hasta 7 Con Paso 1 Hacer
		Escribir "";
		Escribir "Carrera ", i+1, " (", carreras[i], ").";
		Para j<-0 Hasta 1 Con Paso 1 Hacer
			Para k<-0 Hasta 4 Con Paso 1 Hacer
				Escribir "El semestre ", j+1, " el año ", k+1, " se inscribieron ", UNI[i,j,k], " alumnos";
				alumnosAnyo[k] <- alumnosAnyo[k] + UNI[i,j,k];
				Si k = 4 Entonces
					alumnosCarrUltAnyo[i] <- alumnosCarrUltAnyo[i] + UNI[i,j,k];
				FinSi
				Si i = 5 Entonces
					alumnosCA[k] <- alumnosCA[k] + UNI[i,j,k];
				FinSi
			FinPara
		FinPara
	FinPara
	
//Se comparan los valores de cada arreglo para seleccionar el valor m�s apto
	resultadoA <- 0;
	resultadoC <- 0;
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Si alumnosAnyo[resultadoA] < alumnosAnyo[i] Entonces
			resultadoA <- i;
		FinSi
		Si alumnosCA[resultadoC] < alumnosCA[i] Entonces
			resultadoC <- i;
		FinSi
	FinPara
	
	resultadoB <- 0;
	Para i<-0 Hasta 7 Con Paso 1 Hacer
		Si alumnosCarrUltAnyo[resultadoB] < alumnosCarrUltAnyo[i] Entonces
			resultadoB <- i;
		FinSi
	FinPara
	
//Se muestran los resultados al usuario.
	Escribir "";
	Escribir "";
	Escribir "";
	Escribir "El año en el que ingreso el mayor n�mero de alumnos es el año ", resultadoA+1, " con ", alumnosAnyo[resultadoA], " alumnos";
	Escribir "La carrera que recibio mayor número de alumnos el último año es la carrera ", carreras[resultadoB], " con ", alumnosCarrUltAnyo[resultadoB], " alumnos";
	Escribir "El año en el que la carrera Ingeniería en Computacion recibio mas alumnos es el año ", resultadoC+1, " con ", alumnosCA[resultadoC], " alumnos";
	
FinProceso