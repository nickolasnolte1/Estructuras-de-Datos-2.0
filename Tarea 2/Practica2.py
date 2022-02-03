debitos = []
registroDebito = 0
creditos = []
registrocreditos = 0
totalDebitos = 0
totalCreditos = 0
registroEliminar = 0



def addDebitos():
    global registroDebito
    global debitos
    print('Ingrese un valor menor o igual a 0 para cancelar')
    while True:
        try:
            n = int(input("Ingrese el debito: "))
            if n > 0:
                registroDebito += 1
                debitos += [n]
            else:
                if len(debitos) < 10:
                    print('EL MINIMO DE DEBITOS ES 10, POR FAVOR CONTINUE AGREGANDO DEBITOS')
                else:
                    break
        except ValueError:  
            print("Invalido, por favor ingrese un numero")

def addcreditos():
    global registrocreditos
    global creditos
    print('Ingrese 0 para terminar de ingresar datos')
    while True:
        try:
            n = int(input("Ingrese el credito: "))
            if n > 0:
                registrocreditos += 1
                creditos += [n]
            else:
                if len(creditos) < 5:
                    print('EL MINIMO DE creditos ES 5, POR FAVOR CONTINUE AGREGANDO creditos')
                else:
                    break
        except ValueError:  
            print("Invalido, por favor ingrese un numero")

def totalDebitosf():
    global totalDebitos
    global debitos
    totalDebitos = 0
    for i in range(0,len(debitos)):
        totalDebitos += debitos[i]
    print("El total de debitos es: ",totalDebitos)
    return(totalDebitos)

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
    if(totalDebitosf() > 0):
        promedio = totalDebitosf()/len(debitos)
    print("El promedio de debitos es: ",promedio)
    return(promedio)

def saldo():
    print("El saldo actual es: ",totalCreditosf() - totalDebitosf())
    return(saldo)

def menu():
    print("\n1. Ingresar debito(s)")
    print("2. Ingresar credito(s)")
    print("3. Total de debitos")
    print("4. Total de creditos")
    print("5. Mostrar el saldo")
    print("6. Promedio de debitos")
    print("7. Debito mas grande")
    print("8. Mostrar registro de operaciones de debito y credito")
    print("9. Imprimir creditos y debitos")
    print("10. Eliminar creditos")
    print("Cualquier otra tecla para cancelar")

def debitoGrande():
    global debitos
    gg = 0
    for i in range(0,len(debitos)):
        if(debitos[i]>gg):
            gg = debitos[i]
    print("El debito mas grande es: ",gg)
    return(gg)

def registro():
    print("Se ha agregado ", registroDebito, ' veces debitos')
    print("Se ha agregado ", registrocreditos, ' veces creditos')
    print("Se ha eliminado ", registroEliminar, ' veces creditos')

def prnt():
    global debitos
    global creditos
    print('Debitos: \b')
    print(debitos)
    print('Creditos: \b')
    print(creditos)

def eliminar():
    prnt()
    global creditos 
    mod = int(input('Monto del credito que desea eliminar: '))
    global registroEliminar
    for i in range(0,len(creditos)):
        if(creditos[i] == mod):
            print('')
            registroEliminar += 1
            creditos = creditos[0:i] + creditos[i + 1:] 
            return(creditos)