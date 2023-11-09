#carga cliente
#el while True lo que hace es repetirse hasta que una condicion se cumpla y accione un break
while True: 
    try:
        with open('Clientes.dat', 'r') as archivo:
            lineas = archivo.readlines()
        numero_de_lineas = len(lineas)

        if numero_de_lineas > 0:
            ultima_linea = lineas[-1]
            lista_ultima_lin=ultima_linea.strip(" ").split(",")
            codigo_cliente=int(lista_ultima_lin[0])+1
        else:
            print("El archivo está vacío.")
    except FileNotFoundError:
        print("El archivo no se encontró.")
    
    print("Bienvenido! Si usted ingresa 0.")
    exit_program=input("Para continuar presiones enter de lo contrario 0: ")
        
    if exit_program=='0':
        print("saldra del programa")
        break
    #Break su funcion es romper el bucle en el momento de ser leida
    else:
        
        NyA=input("ingrese el nombre y apellido: ")
        #NyA:significa nombre y apellido
        PI=0
        PF=0

 
        """Las siguientes lineas cumplen la funcion de leer el archivo y en caso de que este contenga lineas dentro
        abrira el archivo con el caracter que le corresponde 'a' de append debido a que cada ver que habra con el caracter
        'W' este sobre escribe el archivo en vez de agregar un nueva linea"""
        try:
            archivo=open("Clientes.dat", "r")
            lineas=archivo.readlines()
            len(lineas)
            archivo.close
            if len(lineas)>0:
                archivo=open("Clientes.dat","a")   
        except FileNotFoundError:
            archivo=open("Clientes.dat","w") 
        
        archivo.write(f"{str(codigo_cliente).ljust(4)},{NyA.ljust(31)},{str(PI).ljust(6)},{str(PF).ljust(6)},\n")

       
        print(f"Cliente cargado con exito:\n codigo: {codigo_cliente} Nombre y apellido: {NyA}")