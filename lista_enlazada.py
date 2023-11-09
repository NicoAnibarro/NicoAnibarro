def leer_arch_client():
    try: 
        # Esta funcion convierte el archivo de Clientes.tx y lo convierte en un diccionario a modo de comprar despues con el codigo cliente ingresado.
        cr=0
        diccionario={}
        clientes=open('Clientes.dat' , 'r', encoding='utf-8')
        linea=clientes.readline()
        while linea!="":
            lista=linea.split(",")
            cr=cr+1
            cod_client=lista[0].strip(" ")
            nya=lista[1].strip(" ")
            posi=lista[2].strip(" ")
            posf=lista[3].strip(" ")
            diccionario[cod_client]={'NyA':nya,'posi':posi, 'posf':posf}
            linea=clientes.readline()
    except FileNotFoundError:
        print("no existe el archivo especificado")
        #Si no existe el archivo impeimira este error
    return diccionario        
def encabezado_impresion():
    print(long_lineas)
    print("| Nombre Cliente |"+str(NyA).center(22)+"| Codigo |"+str(cod_cliente).center(6)+"|")
    print(long_lineas)
    print("|"+"Factura".center(13)+"|"+"Fecha".center(25)+"|"+"importe".center(15)+"|")
    print(long_lineas)
def cuerpo_impresion():
    print("|"+f"{str(nro_factura).center(13)}"+"|"+f"{str(fecha).center(25)}"+"|"+f"{str(importe).center(15)}"+"|")

def pie_impresion():
    print(long_lineas)

def listado_orden_descendente():
    global fecha, nro_factura, importe
    with open('Novedad.dat', 'r', encoding='utf-8') as archnov:
        calc_pos=(long_carac_nov*int(PI))-long_carac_nov
        #print("cal_pos: ", calc_pos)
        archnov.seek(calc_pos)
        lista=archnov.readline().split(",")
        #print("FACTURA POS I :", lista)
        fecha=lista[1].strip(" ")
        nro_factura=int(lista[2])
        importe=int(lista[3])
        reg_sig=int(lista[4])
        #print("registro siguiente: ", reg_sig)
        encabezado_impresion()
        cuerpo_impresion()

    while reg_sig != 0:
        with open('Novedad.dat', 'r', encoding='utf-8') as archnov:
            
            calc_pos=(long_carac_nov*int(reg_sig))-long_carac_nov
            #print("calculo de posicion: ", calc_pos)
           
            archnov.seek(calc_pos)
            lista_orden=archnov.readline().split(",")
            #print("Factura registro siguiente :", lista_orden)
            fecha=lista_orden[1].strip(" ")
            nro_factura=int(lista_orden[2])
            importe=int(lista_orden[3])
            reg_sig=int(lista_orden[4])
            #print("registro siguiente: ", reg_sig)
            cuerpo_impresion()
    pie_impresion()

def listado_orden_ascendente():
    global fecha, nro_factura, importe
    with open('Novedad.dat', 'r', encoding='utf-8') as archnov:
        calc_pos=(long_carac_nov*int(PF))-long_carac_nov
        print("cal_pos: ", calc_pos)
        archnov.seek(calc_pos)
        lista=archnov.readline().split(",")
        #print("FACTURA POS I :", lista)
        fecha=lista[1].strip(" ")
        nro_factura=int(lista[2])
        importe=int(lista[3])
        reg_ant=int(lista[5])
        #print("registro siguiente: ", reg_ant)
        encabezado_impresion()
        cuerpo_impresion()

    
    while reg_ant != 0:
        with open('Novedad.dat', 'r', encoding='utf-8') as archnov:
            calc_pos=(long_carac_nov*int(reg_ant))-long_carac_nov
            #print("calculo de posicion: ", calc_pos)
            archnov.seek(calc_pos)
            lista_orden=archnov.readline().split(",")
            #print("Factura registro siguiente :", lista_orden)
            reg_ant=int(lista_orden[5])
            fecha=lista_orden[1].strip(" ")
            nro_factura=int(lista_orden[2])
            importe=int(lista_orden[3])
            #print("registro siguiente: ", reg_ant)
            cuerpo_impresion()
    pie_impresion()

while True:
    """----- VARIABLES GLOBALES ----"""
    long_carac_nov=73 # Es la cantidad de caracteres que posee el archivo novedad incluido \n sin contar el salto de linea
    long_carac_client= 53 # Es la cantidad de caracteres que posee el archivo cliente incluido \n sin contar el salto de linea
    cod_cliente=""
    PI=0
    PF=0
    NyA=""
    calc_pos=0
    nro_factura=0
    fecha=''
    importe=0
    reg_sig=0
    long_lineas='-'*57


    Clientes=leer_arch_client()
    print("LISTADO COMPRAS POR CLIENTE")
    # Proceso de ejecucion del programa
    #Se ingresa el codigo cliente, los clientes se cargaran en un diccionario a modo de verificar el codigo cliente si existe
    # una vez verificado procedera a leer la linea del codigo cliente y guardara en variables la posicion inicial y la posicion final
    #se dara a elejir si se quiere de manera desc o asc en el primer caso toma el valor de la posicion incial
    # abrira el archivo novedad y leera la linea correspondiente a la factura figurada en la posicion inicial
    #una vez leido tomara los valores de reg sig y se dirigira nuevamente a la nueva direccion hasta que el reg_sig = 0
    cod_cliente=input('ingrese el codigo cliente ')
    if int(cod_cliente) != 0:
        if cod_cliente in Clientes:
            #Compara si el cliente existe. si el cliente existe vamos a traer los siguientes campos
            NyA= Clientes[cod_cliente]["NyA"]
            PI=Clientes[cod_cliente]['posi']
            PF=Clientes[cod_cliente]['posf']
        else:
            print("El cliente que quiere buscar no existe en la lista")
            break
        opcion=input('Orden descentente presione: 1, Orden ascendente: 2 :')
        if int(opcion) == 1:
            #se llama a la funcion de ordenar en forma descendente
            listado_orden_descendente()
            
        if int(opcion) == 2:
            listado_orden_ascendente()

    else:
        print("A salido del programa")
        break