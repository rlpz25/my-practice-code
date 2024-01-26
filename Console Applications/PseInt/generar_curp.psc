//PERFILES COMPATIBLES
//UJAT-DAIA
//VicenteFierro
//UABC-II

Algoritmo GenerarCURP
	Definir prueba Como Caracter;
	Definir genero, nombre_completo, fecha_de_nacimiento, estado_de_nacimiento, resultado Como Caracter;
	Escribir "Ingresa tu nombre completo";
	Leer nombre_completo;
	nombre_completo <- eliminaAcentos(nombre_completo);
	Escribir "Ingresa tu fecha de nacimiento separada por guiones ( DD-MM-AAAA )";
	Leer fecha_de_nacimiento;
	Escribir "¿Eres hombre o mujer?";
	Leer genero;
	Escribir "¿En qué estado de la república naciste?";
	Leer estado_de_nacimiento;
	resultado <- Mayusculas(devolverCURP(nombre_completo, fecha_de_nacimiento, estado_de_nacimiento, genero));
	Escribir resultado;	
FinAlgoritmo

Funcion resultado <- devolverCURP ( nombre_completo, fecha_de_nacimiento, estado_de_nacimiento, genero )
	Definir parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10, parte11, resultado Como caracter;
	parte1 <- funcionParte1(nombre_completo);
	parte2 <- funcionParte2(nombre_completo);
	parte3 <- funcionParte3(nombre_completo);
	parte4 <- funcionParte4(fecha_de_nacimiento);
	parte5 <- funcionParte5(genero);
	parte6 <- funcionParte6(estado_de_nacimiento);
	parte7 <- funcionParte7(nombre_completo);
	parte8 <- funcionParte8(nombre_completo);
	parte9 <- funcionParte9(nombre_completo);
	parte10 <- funcionParte10(fecha_de_nacimiento);
	parte11 <- funcionParte11(azar(9));
	resultado <- parte1 + parte2 + parte3 + parte4 + parte5 + parte6 + parte7 + parte8 + parte9 + parte10 + parte11;
FinFuncion

Funcion parte1 <- funcionParte1 ( nombre_completo )
	Definir parte1, primer_apellido, apellido_vector Como caracter;
	Definir numero_palabras, tamanyo, i Como Entero;
	numero_palabras <- contarPalabras(nombre_completo);
	Si numero_palabras = 3 Entonces
		primer_apellido <- obtenerPalabra(2, nombre_completo);
	SiNo
		primer_apellido <- obtenerPalabra(3, nombre_completo);
	FinSi
	tamanyo <- Longitud(primer_apellido);
	Dimension apellido_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		apellido_vector[i]<-Subcadena(primer_apellido,i,i);
	Fin Para
	parte1 <- apellido_vector[1]+apellido_vector[2];
FinFuncion

Funcion parte2 <- funcionParte2 ( nombre_completo )
	Definir parte2, segundo_apellido, apellido_vector Como caracter;
	Definir numero_palabras, tamanyo, i Como Entero;
	numero_palabras <- contarPalabras(nombre_completo);
	Si numero_palabras = 3 Entonces
		segundo_apellido <- obtenerPalabra(3, nombre_completo);
	SiNo
		segundo_apellido <- obtenerPalabra(4, nombre_completo);
	FinSi
	tamanyo <- Longitud(segundo_apellido);
	Dimension apellido_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		apellido_vector[i]<-Subcadena(segundo_apellido,i,i);
	FINPARA
	parte2 <- apellido_vector[1];
FinFuncion

Funcion parte3 <- funcionParte3 ( nombre_completo )
	Definir parte3, primer_nombre, segundo_nombre, nombre, nombre_vector Como caracter;
	Definir numero_palabras, tamanyo, i Como Entero;
	numero_palabras <- contarPalabras(nombre_completo);
	primer_nombre <- Mayusculas(obtenerPalabra(1, nombre_completo));
	segundo_nombre <- Mayusculas(obtenerPalabra(2, nombre_completo));
	Si numero_palabras = 3 ENTONCES
		nombre <- primer_nombre;
	SiNo
		Segun primer_nombre Hacer
			"JOSE": nombre <- segundo_nombre;
			"JOSÉ": nombre <- segundo_nombre;
			"MARIA": nombre <- segundo_nombre;
			"MARÍA": nombre <- segundo_nombre;
			De Otro Modo:
				nombre <- primer_nombre;
		FinSegun
	FinSi
	tamanyo <- Longitud(nombre);
	Dimension nombre_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		nombre_vector[i]<-Subcadena(nombre,i,i);
	FinPara
	parte3 <- nombre_vector[1];
FinFuncion

Funcion parte4 <- funcionParte4 ( fecha_de_nacimiento )
	Definir parte4, anyo Como caracter;
	Definir tamanyo, i Como Entero;
	tamanyo <- Longitud(fecha_de_nacimiento);
	Dimension anyo(tamanyo);
	Para i  <- 1 Hasta tamanyo Con Paso 1 Hacer
		anyo[i] = Subcadena(fecha_de_nacimiento,i,i);
	FinPara
	parte4 <- anyo[9]+anyo[10]+obtenerMes(fecha_de_nacimiento)+obtenerDia(fecha_de_nacimiento);
FinFuncion

Funcion parte5 <- funcionParte5 ( genero )
	Definir parte5 Como caracter;
	Si Mayusculas(genero) == "HOMBRE" Entonces
		parte5 <- "H";
	SiNo
		parte5 <- "M";
	FinSi
FinFuncion

Funcion parte6 <- funcionParte6 ( palabra )
	Definir parte6 Como caracter;
	Segun Mayusculas(palabra) Hacer
		"AGUASCALIENTES": parte6 <- "AS";
		"DISTRITO FEDERAL": parte6 <- "DF";
		"NAYARIT": parte6 <- "NT";
		"SONORA": parte6 <- "SR";
		"BAJA CALIFORNIA": parte6 <- "BC";
		"DURANGO": parte6 <- "DG";
		"NUEVO LEON": parte6 <- "NL";
		"TABASCO": parte6 <- "TC";
		"BAJA CALIFORNIA SUR": parte6 <- "BS";
		"GUERRERO": parte6 <- "GR";
		"OAXACA": parte6 <- "OC";
		"TAMAULIPAS": parte6 <- "TS";
		"CAMPECHE": parte6 <- "CC";
		"HIDALGO": parte6 <- "HG";
		"PUEBLA": parte6 <- "PL";
		"TLAXCALA": parte6 <- "TL";
		"COAHUILA": parte6 <- "CL";
		"JALISCO": parte6 <- "JC";
		"QUERÉTARO": parte6 <- "QT";
		"QUERETARO": parte6 <- "QT";
		"VERACRUZ": parte6 <- "VZ";
		"COLIMA": parte6 <- "CM";
		"MEXICO": parte6 <- "MC";
		"MÉXICO": parte6 <- "MC";
		"QUINTANAROO": parte6 <- "QR";
		"YUCATAN": parte6 <- "YN";
		"CHIAPAS": parte6 <- "CS";
		"MICHOACÁN": parte6 <- "MN";
		"MICHOACAN": parte6 <- "MN";
		"SAN LUIS POTOSI": parte6 <- "SP";
		"SAN LUIS POTOSÍ": parte6 <- "SP";
		"ZACATECAS": parte6 <- "ZS";
		"CHIHUAHUA": parte6 <- "CH";
		"MORELOS": parte6 <- "MS";
		"SINALOA": parte6 <- "SL";
		De Otro Modo:
			parte6 <- "NE";
	FinSegun
FinFuncion

Funcion parte7 <- funcionParte7 ( nombre_completo )
	Definir parte7, primer_apellido, apellido_vector Como caracter;
	Definir numero_palabras, tamanyo, i, contador Como Entero;
	Definir detector Como Logico;
	detector <- Falso;
	numero_palabras <- contarPalabras(nombre_completo);
	Si numero_palabras = 3 Entonces
		primer_apellido <- Mayusculas(obtenerPalabra(2, nombre_completo));
	SiNo
		primer_apellido <- Mayusculas(obtenerPalabra(3, nombre_completo));
	FinSi
	tamanyo <- Longitud(primer_apellido);
	Dimension apellido_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		apellido_vector[i]<-Subcadena(primer_apellido,i,i);
	FinPara
	contador <- 2;
	Repetir
		si apellido_vector[contador] <> "A" Y apellido_vector[contador] <> "E" Y apellido_vector[contador] <> "I" Y apellido_vector[contador] <> "O" Y apellido_vector[contador] <> "U" Entonces
			parte7 <- apellido_vector[contador];
			detector <- Verdadero;
		FinSi
		contador <- contador + 1;
	Hasta Que detector
FinFuncion

Funcion parte8 <- funcionParte8 ( nombre_completo )
	Definir parte8, segundo_apellido, apellido_vector Como caracter;
	Definir numero_palabras, tamanyo, i, contador Como Entero;
	Definir detector Como Logico;
	detector <- Falso;
	numero_palabras <- contarPalabras(nombre_completo);
	Si numero_palabras = 3 Entonces
		segundo_apellido <- Mayusculas(obtenerPalabra(3, nombre_completo));
	SiNo
		segundo_apellido <- Mayusculas(obtenerPalabra(4, nombre_completo));
	FinSi
	tamanyo <- Longitud(segundo_apellido);
	Dimension apellido_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		apellido_vector[i]<-Subcadena(segundo_apellido,i,i);
	FinPara
	contador <- 2;
	Repetir
		si apellido_vector[contador] <> "A" Y apellido_vector[contador] <> "E" Y apellido_vector[contador] <> "I" Y apellido_vector[contador] <> "O" Y apellido_vector[contador] <> "U" Entonces
			parte8 <- apellido_vector[contador];
			detector <- Verdadero;
		FinSi
		contador <- contador + 1;
	Hasta Que detector
FinFuncion

Funcion parte9 <- funcionParte9 ( nombre_completo )
	Definir parte9, nombre, nombre_vector Como caracter;
	Definir numero_palabras, tamanyo, i, contador Como Entero;
	Definir detector Como Logico;
	detector <- Falso;
	numero_palabras <- contarPalabras(nombre_completo);
	nombre <- Mayusculas(obtenerPalabra(1, nombre_completo));
	tamanyo <- Longitud(nombre);
	Dimension nombre_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		nombre_vector[i]<-Subcadena(nombre,i,i);
	FinPara
	contador <- 2;
	Repetir
		si nombre_vector[contador] <> "A" Y nombre_vector[contador] <> "E" Y nombre_vector[contador] <> "I" Y nombre_vector[contador] <> "O" Y nombre_vector[contador] <> "U" Entonces
			parte9 <- nombre_vector[contador];
			detector <- Verdadero;
		FinSi
		contador <- contador + 1;
	Hasta Que detector
FinFuncion

Funcion parte10 <- funcionParte10 ( fecha_de_nacimiento)
	Definir parte10 Como caracter;
	Definir abecedario, anyo, digito, fechavector, abecedariovector Como Caracter;
	Definir tamanyo, i Como Entero;
	abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
	Dimension abecedariovector(27);
	tamanyo <- Longitud(abecedario);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		abecedariovector[i]<-Subcadena(abecedario,i,i);
	FinPara
	anyo <- obtenerAnyo(fecha_de_nacimiento);
	Si anyo < '2000' Entonces
		parte10 <- funcionParte11(azar(9));
	SiNo
		parte10 <- abecedariovector[azar(26)+1];
	FinSi
FinFuncion

Funcion parte11 <- funcionParte11 ( numero_azar )
	Definir parte11 Como caracter;
	Segun numero_azar Hacer
		0: parte11 <- "0";
		1: parte11 <- "1";
		2: parte11 <- "2";
		3: parte11 <- "3";
		4: parte11 <- "4";
		5: parte11 <- "5";
		6: parte11 <- "6";
		7: parte11 <- "7";
		8: parte11 <- "8";
		9: parte11 <- "9";
		De Otro Modo:
			parte11 <- "0";
	FinSegun
FinFuncion

Funcion anyo <- obtenerAnyo ( fecha_de_nacimiento )
	Definir anyo, fechavector Como Caracter;
	Definir tamanyo, i Como Entero;
	Dimension fechavector(10);
	tamanyo <- Longitud(fecha_de_nacimiento);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		fechavector[i]<-Subcadena(fecha_de_nacimiento,i,i);
	FinPara
	anyo <- fechavector[7]+fechavector[8]+fechavector[9]+fechavector[10];
FinFuncion

Funcion mes <- obtenerMes ( fecha_de_nacimiento )
	Definir mes, fechavector Como Caracter;
	Definir tamanyo, i Como Entero;
	Dimension fechavector(10);
	tamanyo <- Longitud(fecha_de_nacimiento);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		fechavector[i]<-Subcadena(fecha_de_nacimiento,i,i);
	FinPara
	mes <- fechavector[4]+fechavector[5];
FinFuncion

Funcion dia <- obtenerDia ( fecha_de_nacimiento )
	Definir dia, fechavector Como Caracter;
	Definir tamanyo, i Como Entero;
	Dimension fechavector(10);
	tamanyo <- Longitud(fecha_de_nacimiento);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		fechavector[i]<-Subcadena(fecha_de_nacimiento,i,i);
	FinPara
	dia <- fechavector[1]+fechavector[2];
FinFuncion

Funcion numero_palabras <- contarPalabras ( palabra )
	Definir letras Como Caracter;
	Definir tamanyo, i, contador, numero_palabras Como Entero;
	contador <- 0;
	tamanyo = Longitud(palabra);
	Dimension letras[tamanyo];
	Para i  <- 1 Hasta tamanyo Con Paso 1 Hacer
		letras[i] = Subcadena(palabra,i,i);
		Si i <> 1 Entonces
			Si letras[i-1] = " " Y letras[i] <> " " Entonces
				contador <- contador+1;
			FinSi
		FinSi
	FinPara
	numero_palabras <- contador+1;
FinFuncion

Funcion palabra <- obtenerPalabra ( numero_palabra, cadena_palabras )
	Definir palabra, palabras_vector Como caracter;
	Definir tamanyo, i, inicio, final, contador, numero_palabras Como Entero;
	numero_palabras <- contarPalabras(cadena_palabras);
	tamanyo <- Longitud(cadena_palabras);
	Dimension palabras_vector(tamanyo);
	contador <- 0;
	Para i  <- 1 Hasta tamanyo Con Paso 1 Hacer
		palabras_vector[i] = Subcadena(cadena_palabras,i,i);
	FinPara
	Para i  <- 1 Hasta tamanyo Con Paso 1 Hacer
		Si i <> 1 Entonces
			Si palabras_vector[i-1] = " " Y palabras_vector[i] <> " " Entonces
				contador <- contador+1;
			FinSi
		FinSi
		Si numero_palabra = 1 y contador = 0 Entonces
			inicio <- 1;
			Si palabras_vector[i+1] = " " Y palabras_vector[i] <> " " Entonces
				final <- i;
			FinSi
		FinSi
		Si numero_palabra = 2 y contador = 1 Entonces
			Si palabras_vector[i-1] = " " Y palabras_vector[i] <> " " Entonces
				inicio <- i;
			FinSi
			Si palabras_vector[i+1] = " " Y palabras_vector[i] <> " " Entonces
				final <- i;
			FinSi
		FinSi
		Si numero_palabra = 3 y contador = 2 Entonces
			Si numero_palabras = 3 Entonces
				Si palabras_vector[i-1] = " " Y palabras_vector[i] <> " " Entonces
					inicio <- i;
				FinSi
				Si i = tamanyo Y palabras_vector[i] <> " " Entonces
					final <- i;
				FinSi
			SiNo
				Si palabras_vector[i-1] = " " Y palabras_vector[i] <> " " Entonces
					inicio <- i;
				FinSi
				Si palabras_vector[i+1] = " " Y palabras_vector[i] <> " " Entonces
					final <- i;
				FinSi
			FinSi
		FinSi
		Si numero_palabra = 4 y contador = 3 Entonces
			Si palabras_vector[i-1] = " " Y palabras_vector[i] <> " " Entonces
				inicio <- i;
			FinSi
			Si i = tamanyo Y palabras_vector[i] <> " " Entonces
				final <- i;
			FinSi
		FinSi
	FinPara
	palabra <- Subcadena(cadena_palabras, inicio, final);
FinFuncion

Funcion sin_acento <- eliminaAcentos ( palabra )
	palabra <- Mayusculas(palabra);
	Definir sin_acento, palabra_vector Como Caracter;
	Definir tamanyo, i Como Entero;
	tamanyo <- Longitud(palabra);
	Dimension palabra_vector(tamanyo);
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		palabra_vector[i]<-Subcadena(palabra,i,i);
	FinPara
	sin_acento <- "";
	Para i<-1 Hasta tamanyo Con Paso 1 Hacer
		Segun palabra_vector[i] Hacer
			"Á": palabra_vector[i] <- "A";
			"É": palabra_vector[i] <- "E";
			"Í": palabra_vector[i] <- "I";
			"Ó": palabra_vector[i] <- "O";
			"Ú": palabra_vector[i] <- "U";
			De Otro Modo:
				palabra_vector[i] <- palabra_vector[i];
		FinSegun
		sin_acento <- sin_acento+palabra_vector[i];
	FinPara
FinFuncion
