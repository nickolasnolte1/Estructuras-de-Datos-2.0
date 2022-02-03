
# Declarar variables y arreglos
debits_record = 0
credits_record = 0
TotalDebitos = 0
totalCreditos = 0
borrar = 0
debitos = []
creditos = []

#Menú para el usuario
def menu():
    print("\n-------------------------- M E N U ---------------------------")
    print("|   1. Ingresar débitos                                      |")
    print("|   2. Ingresar créditos                                     |")
    print("|   3. Ver el total de débitos ingresados hasta el momento   |")
    print("|   4. Ver el total de créditos ingresados hasta el momento  |")
    print("|   5. Ver saldo actual                                      |")
    print("|   6. Ver el promedio de los débitos ingresados             |")
    print("|   7. Ver el débito con el monto más grande                 |")
    print("|   8. Ver el  registro de operaciones                       |")
    print("|   9. Imrpimir arreglos de créditos y débitos               |")
    print("|   10. Eliminar creditos                                    |")
    print("|   Cualquier otra tecla para cancelar                       |")
    print("--------------------------------------------------------------")

def agregar_debitos():

    global debits_record
    global debitos
    print('Presione 0 para terminar de ingresar datos')
    while True:
        if True:
            numdebits = int(input("Ingrese el monto del débito Q: "))
            if numdebits > 0:
                debits_record += 1
                debitos += [numdebits]
            else:
                if len(debitos) < 10:
                    print('Por favor ingrese más datos, debe ingresar por lo menos 10 débitos para poder continuar')
                else:
                    break
        else:  
            print("Por favor ingrese una opción que se encuentre en el menú")

def agregar_creditos():
    global credits_record
    global creditos
    print('Presione 0 cuando haya terminado de ingresar los datos')
    while True:
        if True:
            numcredits = int(input("Ingrese el monto del crédito Q: "))
            if numcredits > 0:
                credits_record += 1
                creditos += [numcredits]
            else:
                if len(creditos) < 5:
                    print('Por favor ingrese más datos, debe ingresar por lo menos 5 créditos para poder continuar')
                else:
                    break
        else:  
            print("Por favor ingrese una opción que se encuentre en el menú")

def total_debitos():
    global TotalDebitos
    global debitos
    TotalDebitos = 0
    for i in range(0,len(debitos)):
        TotalDebitos += debitos[i]
    print("El total de debitos es: ",TotalDebitos)
    return(TotalDebitos)

def totalCreditosf():
    global creditos
    global totalCreditos
    totalCreditos = 0
    for i in range(0,len(creditos)):
        totalCreditos += creditos[i]
    print("El total de creditos es: ",totalCreditos)
    return(totalCreditos)

def promedioDebitos():
    promedio = 0
    global debitos
    if(total_debitos() > 0):
        promedio = total_debitos()/len(debitos)
    print("El promedio de debitos es: ",promedio)
    return(promedio)

def saldo():
    print("El saldo actual es: ",totalCreditosf() - total_debitos())
    return(saldo)

def debitoGrande():
    global debitos
    gg = 0
    for i in range(0,len(debitos)):
        if(debitos[i]>gg):
            gg = debitos[i]
    print("El debito mas grande es: ",gg)
    return(gg)

def registro():
    print("Se ha agregado ", debits_record, ' veces debitos')
    print("Se ha agregado ", credits_record, ' veces creditos')
    print("Se ha eliminado ", borrar, ' veces creditos')

def prnt():
    global debitos
    global creditos
    print('Debitos: \b')
    print(debitos)
    print('Creditos: \b')
    print(creditos)
