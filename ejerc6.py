cad=raw_input("Ingrese la Frase: ")
con=0
letras=0
digitos=0
for item in cad:
	if cad[con]>='a':
		if cad[con]<='z':
			letras=letras+1
	if cad[con]>='A': 
		if cad[con]<='Z':
			letras=letras+1
	if cad[con]>='0':
		if cad[con]<='9':
			digitos=digitos+1
	con=con+1
else:
	print "Letras : ",letras
	print "digitos : ",digitos
