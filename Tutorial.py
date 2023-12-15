"""

Calcular el pago de nomina para el Mes de Noviembre

"""

#Sueldo Base
diasTrabajados = 30
horasExtraPrice = 20000
salarioBase = 1300000
valorDia = (salarioBase / diasTrabajados)
seguridad = salarioBase * 0.04
nombre = input("Ingresa el Nombre del Empleado: >")

rangoEmpresarial = input("""
Ingrese el Rango del Empleado
    
    A.Mensajero
    B.Administrado
    C.IT Soluciones
    D.Seguridad

:> """)

if (rangoEmpresarial == "A"):
    bono = (salarioBase * 0.10)
    
elif(rangoEmpresarial == "B"):
    bono = (salarioBase * 0.10)

    
elif(rangoEmpresarial == "C"):
    bono = (salarioBase * 0.10)
    
elif(rangoEmpresarial == "D"):
    bono = 300000
    
else:
    bono = 0
    print("\nERROR No Reconosco esa opcion \n")

llamadosAten = input("Cuenta con Llamados de Atencion s/n :>")
if (llamadosAten == "s"):
    #Optener Nuevo salario y nuevo valor dia
    diasTrabajados = 27
    sueldoBase = (diasTrabajados * valorDia)
    valorDia = (sueldoBase / 30)
elif (llamadosAten == "n"):
    pass
else:
    print("\nERROR No Reconosco esa opcion \n")

horasExtra = input("Cuenta con horas Extra s/n :>")
if (horasExtra == "s"):
    cuantasHoras = int(input("Cuantas horas :>"))
    totalHoras = (horasExtraPrice * cuantasHoras)
elif (horasExtra == "n"):
    pass

else:
    print("\nERROR No Reconosco esa opcion \n")


print(f"""
-Nombre: {nombre}
-Salario Base: ${salarioBase}
-Dias Trabajados:  {diasTrabajados}
-Valor Dia: {valorDia}
-Valor Bono: {bono}
-Valor Pago Seguridad Social: {seguridad} \n

-Valor Total: {(valorDia*diasTrabajados)+ bono + seguridad + totalHoras}
""")



