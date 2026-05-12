Proceso menu
	definir respuesta Como Entero
	definir num1, num2 Como Real
	definir sum, res, mul, div Como Real
	
	Mientras respuesta <> 5 Hacer // mientras la respuesta no sea 5 se repetira el menu
		
		escribir "Que le gustaria hacer?"
		escribir "Digite 1 para sumar 2 numeros"
		escribir "Digite 2 para restar 2 numeros"
		escribir "Digite 3 para multiplicar 2 numeros"
		escribir "Digite 4 para dividir 2 numeros"
		escribir "Digite 5 para salir del programa"
		
		Leer respuesta
		
		Si respuesta = 1 Entonces
			Escribir "Digite su primer valor"
			Leer num1
			Escribir "Digite el segundo numero"
			Leer num2
			sum <- num1 + num2
			Escribir "Su resultado es: ", sum
		FinSi
		
		Si respuesta = 2 Entonces
			Escribir "Usted eligio Resta"
			Escribir "Digite su primer valor"
			Leer num1
			Escribir "Digite el segundo numero"
			Leer num2
			res <- num1 - num2
			Escribir "Su resultado es: ", res
		FinSi
		
		Si respuesta = 3 Entonces
			Escribir "Usted eligio multiplicar"
			Escribir "Digite su primer valor"
			Leer num1
			Escribir "Digite el segundo numero"
			Leer num2
			mul <- num1 * num2
			Escribir "Su resultado es: ", mul
		FinSi
		
		Si respuesta = 4 Entonces
			Escribir "Usted eligio dividir"
			Escribir "Digite su primer valor"
			Leer num1
			Escribir "Digite el segundo numero"
			Leer num2
			
			Si num2 <> 0 Entonces
				div <- num1 / num2
				Escribir "Su resultado es: ", div
			SiNo
				Escribir "Error: no se puede dividir por 0"
			FinSi
		FinSi
		
	FinMientras
	
	Escribir "Usted eligio salir del programa!"
	Esperar 3 Segundos
	Escribir "Nos vemos"
	
FinProceso