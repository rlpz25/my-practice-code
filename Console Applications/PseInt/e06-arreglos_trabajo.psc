Proceso Ejercicio6
	
	//Se definen las variables que se usaran.
	Definir TRA, i, j, sueldo Como Entero;
	Definir arregloA, arregloB Como Entero;
	Definir resultadoC, resultadoD como entero;
	Definir nombre Como Caracter;
	
	///Para este ejercicio no es necesario utilizar un arreglo Tridimensional,
	///ya que no se cuenta con una tercera dimensión que requiera su consideración a la
	///hora de recorrer el arreglo.
	Dimension TRA[5,6];
	Dimension nombre[5];
	Dimension sueldo[5];
	Dimension arregloA[5];
	Dimension arregloB[5];
	
	//Se inicializan los arreglos auxiliares
	Para i <- 0 Hasta 4 Hacer
		arregloA[i] <- 0;
		arregloB[i] <- 0;
	FinPara
	
	//Se asigna el nombre de cada chofer
	nombre[0] <- "Gabriela";
	nombre[1] <- "Fernanda";
	nombre[2] <- "Ricardo";
	nombre[3] <- "Roberto";
	nombre[4] <- "Daniela";
	
	//Se asignan sueldo por hora a cada chofer
	sueldo[0] <- 35;
	sueldo[1] <- 27;
	sueldo[2] <- 36;
	sueldo[3] <- 29;
	sueldo[4] <- 31;
	
	///Se rellena el arreglo principal con valores al azar, estos datos representan la cantidad de horas trabajadas en cada casilla del arreglo..
	Para i <- 0 Hasta 4 Hacer
		Para j <- 0 hasta 5 Hacer
			TRA[i,j] <- azar(3)+5;
		FinPara
	FinPara
	
	//Se realiza el primer recorrido del arreglo principal con el objetivo de extraer datos manejables, los cuales
	//se almacenan en los arreglos auxiliares.
	Para i <- 0 Hasta 4 Hacer
		para j <- 0 Hasta 5 Hacer
			//Extrae la suma de todas las horas trabajadas para cada chofer.
			arregloA[i] <- arregloA[i] + TRA[i,j];
			//Extrae las horas trabajadas el Lunes para cada chofer
			Si j = 0 Entonces
				arregloB[i] <- arregloB[i] + TRA[i,j];
			FinSi
		FinPara
	FinPara
	
	//Se realiza un recorrido al arreglo auxiliar para seleccionar el resultado m�s apto.
	resultadoD <- 0;
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		//Selecciona el mayor de 2 valores
		Si arregloB[resultadoD] < arregloB[i] Entonces
			resultadoD <- i;
		FinSi
	FinPara
	
	resultadoC <- 0;
	//Resultado del Inciso A
	Escribir "El total de horas trabajadas a la semana para cada trabajador son:";
	//Imprime una lista con los nombres y las horas trabajadas de cada chofer.
	Para i <- 0 Hasta 4 Hacer
		Escribir nombre[i], " trabajo ", arregloA[i], " horas.";
	FinPara
	Escribir "";
	//Resultado del Inciso B
	Escribir "El sueldo semanal para cada trabajador es:";
	//Imprime una lista con el sueldo semanal de cada chofer.
	Para i <- 0 Hasta 4 Hacer
		resultadoC <- resultadoC+arregloA[i]*sueldo[i];
		Escribir "El sueldo semanal de ", nombre[i], " es de ", arregloA[i]*sueldo[i], " pesos.";
	FinPara
	Escribir "";
	//Resultado del Inciso C
	Escribir "El total que pagara la empresa es de: ", resultadoC;
	Escribir "";
	//Resultado del Inciso D
	Escribir "El trabajador que laboro mas horas el dia Lunes fue ", nombre[resultadoD], " con ", arregloB[resultadoD], " horas trabajadas.";
	
FinProceso