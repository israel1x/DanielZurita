# DANIEL ZURITA
primer = input("Introduce el Primer Numero: ")
segun = input("Introduce el Segundo Numero: ")
tercer = input("Introduce el Tercer Numero: ")
pi = 3.14
print "Los numeros que ingreso son: ",primer,segun,tercer
print "Resultado suma = ",primer+segun+tercer
print "Resultado resta = ",primer-(segun)-(tercer)
print "Resultado promedio = ",(primer+segun+tercer)/3

if ((segun<primer and segun>tercer) or (segun>primer and tercer>segun)):
    print "Se Encuentra el segundo numero ", segun, " entre el primero ", primer, " y el tercero ", tercer, ":", True
else:
    print "Se Encuentra el segundo numero ", segun, " entre el primero ", primer, " y el tercero ", tercer, ":", False

if primer>segun and segun>tercer:
    print primer,"-",segun,"-",tercer,":",True
else:
    print primer,"-",segun,"-",tercer,":",False

print "Altura h = ",abs(primer)
print "Radio R = ",abs(segun)
print "Generatriz g = ",abs(tercer)
print "Area A =",((pi*abs(segun))*(abs(tercer)+abs(segun)))
print "Volumen V = ",(0.33*pi*pow(segun,2))*abs(primer)