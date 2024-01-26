Proceso Ejercicio1
	
	//Se declaran las variables a utilizar.
	Definir FAB, i, j, costos Como Entero;
	Definir arregloA Como Entero;
	Definir resultadoB, resultadoC Como Entero;
	
	///Para este ejercicio no es necesario utilizar un arreglo Tridimensional,
	///ya que no se cuenta con una tercera dimensión que requiera su consideración a la
	///hora de recorrer el arreglo.
	Dimension FAB[12,15];
	Dimension arregloA[15];
	Dimension costos[15];
	
	//Se inicializan las casillas del arreglo auxiliar
	//Se rellena el arreglo de costos con valores al azar.
	Para i <- 0 Hasta 14 Hacer
		arregloA[i] <- 0;
		costos[i] <- azar(500)+1;
	FinPara
	
	///Se rellena el arreglo principal con valores al azar, estos datos representan la cantidad vendida de un producto.
	Para i <- 0 Hasta 11 Hacer
		para j <- 0 hasta 14 Hacer
			FAB[i,j] <- azar(200)+1;
		FinPara
	FinPara
	
	//Se realiza el primer recorrido con el objetivo de extraer los datos y colocarlos en el arreglo auxiliar,
	//esto para facilitar el manejo de los datos.
	Para i <- 0 Hasta 11 Hacer
		para j <- 0 hasta 14 Hacer
			arregloA[j] <- arregloA[j] + FAB[i,j];
		FinPara
	FinPara
	
	//Se utiliza el arreglo auxiliar para calcular el total de las ventas de todos los productos.
	resultadoB <- 0;
	Para i <- 0 Hasta 14 Hacer
		//resultadoB almacena la suma de los totales de cada producto
		resultadoB <- resultadoB + (arregloA[i] * costos[i]);
	FinPara
	
	//Se utiliza el arreglo auxiliar para comparar sus datos y obtener el que cumple con los requisitos aptos.
	resultadoC <- 0;
	Para i <- 0 Hasta 14 Hacer
		Si arregloA[resultadoC] < arregloA[i] Entonces
			resultadoC <- i;
		FinSi
	FinPara
	
	//Se muestran los datos al usuario.
	//Resultado del Inciso A
	Escribir "El monto de venta del año de cada producto es de:";
	//Imprime una lista de la cantidad vendida de cada producto, estos valores estaban almacenados en el arregloA
	Para i <- 0 Hasta 14 Hacer
		Escribir "Del producto ", i+1, " se vendieron ", arregloA[i], " piezas, resultando en un monto total de ", arregloA[i]*costos[i], " pesos.";
	FinPara
	Escribir "";
	//Resultado del Inciso B
	Escribir "El monto total de ventas de la fábrica es de: ", resultadoB;
	Escribir "";
	//Resultado del Inciso C
	Escribir "El producto que más se ha vendido es el producto ", resultadoC+1, " con un monto total de ", arregloA[resultadoC]*costos[resultadoC], " pesos este a�o.";
	
FinProceso