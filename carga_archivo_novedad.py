#archivo de carga 
import time

def fecha_actual():
    from datetime import datetime
    formato= "%d-%m-%Y %H:%M:%S"
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime(formato)
    return fecha_formateada
    #Esta funcion nos guarda la fecha actual de manera automatica en la factura.

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
def abrir_arc_nov():
    estoy=0
    try:
        with open('Novedad.dat', 'r' , encoding='utf-8') as archivo:
            estoy=1
    except FileNotFoundError:
        with open('Novedad.dat', 'a+', encoding='utf-8') as archivo:
            estoy=2
    archivo.close()
    if estoy==1:
        archivo=open('Novedad.dat', 'a', encoding='utf-8')
    if estoy==2:
        archivo=open('Novedad.dat', 'w', encoding='utf-8')
    return archivo
def calc_long_client():
    with open('Clientes.dat' , 'r', encoding='utf-8') as archivo:
        linea=archivo.readline()
        cant_carac_linea_client=len(linea)
    return cant_carac_linea_client

def cal_long_nov():
    cant_carac_linea_nov=0
    try:
         with open('Novedad.dat' , 'r', encoding='utf-8') as archivo:
            linea=archivo.readline()
            cant_carac_linea_nov=len(linea)
    except FileNotFoundError:
        print("El 'archivo no existe cree el registro y vuelva a intenarlo")
        cant_carac_linea_nov=0
        pass
    return cant_carac_linea_nov

def numero_factura_aut():
    try:
        with open('Novedad.dat', 'r') as archivo:
            lineas = archivo.readlines()
            numero_de_lineas = len(lineas)
            if numero_de_lineas > 0:
                ultima_linea = lineas[-1]
                lista_ultima_lin=ultima_linea.strip(" ").split(",")
                num_factura=int(lista_ultima_lin[2])+1
                return num_factura
                
            else:
                print("El archivo está vacío.")
    except FileNotFoundError:
        print("El archivo no se encontró.")
        num_factura=1
        return num_factura
print("bienvenido al programa carga del archivo novedad \n si desea cancelar ingrese 0 en el codigo cliente y saldra del programa")

long_carac_nov=73 # Es la cantidad de caracteres que posee el archivo novedad incluido \n
long_carac_client= 53 # Es la cantidad de caracteres que posee el archivo cliente incluido \n
nro_factura_ant=0
calc_pos_nov_reg_sig=0
while True:
    Clientes=leer_arch_client() #Se llama la funcion para que genere el diccionario en la variable Clientes
    
     
    cod_cliente=input("ingrese el codigo cliente: ")
    if cod_cliente!="0":
        if cod_cliente in Clientes:
            #Compara si el cliente existe. si el cliente existe vamos a traer los siguientes campos
            NyA= Clientes[cod_cliente]["NyA"]
            PI=Clientes[cod_cliente]['posi']
            PF=Clientes[cod_cliente]['posf']
        
             
        else:
            print("el cliente no puede comprar" )
            #Si el cliente no existe mostrara el mensaje
            break

        fecha=fecha_actual() # Se llama a la funcion fecha para obtener la fecha y hora actual de generacion de factura.
        nro_factura=numero_factura_aut() #Se llama a la funcion para obtener el ultimo nro de factura y sumarle 1 para la generacion de factura automatica
        if nro_factura==None: #Si el archivo novedad se encuentra vacio este automaticamente pondra 1 al nro de factura
            nro_factura=1
        importe=int(input("ingrese el importe de la compra: $"))
        #print("posicion inicial: ",PI) 
        print(f"codigo_cliente: {cod_cliente}, fecha: {fecha}, Nro de factura: {nro_factura}, nombre y apellido: {NyA}, \n posicion inicial: {PI}, posicion final: {PF}")
        opcion_guardado=input("Guardar si/no: ") 
        if opcion_guardado.lower()=="si": #si se escribe si, el programa pasara a escribir al archivo novedad

            if PI !='0': #si la posiscion incical
                #Se debe de guaradar el valor de de PI para asi dirigirse al archivo novedad y verificar si la columna reg_sig es = 0
                #Si el reg_siguiente es 0 vamos a dirigirnos a esa posicion y sobrescribiremos con el nro de factura actual pero el reg_ant seguira siendo 0
                #En caso de que el reg_sig sea distinto de cero nos hiremos desplazando hasta que sea igual a 0
                #Luego en nuestro registro nuevo del arch nov en reg_anterior ponderemos el nro de reg_anterior (es decir el nro de factura anterior) 
                
                #print("long_caracteres_novedad: ", long_carac_nov)
                cal_prim_pos_nov=(int(long_carac_nov)*int(PI))-int(long_carac_nov)
                #print("calc_prim_pos_nov: ", cal_prim_pos_nov)
                
                # Se usara mucho el with open ya que al ejecutar las funciones cierra el archivo automaticamente.
                with open('Novedad.dat', 'r', encoding='utf-8') as archnov:
                    #En este modulo se dirige a la linea del nro de factura descrito como posicion inicial en el archivo cliente
                    archnov.seek(cal_prim_pos_nov) # se dirige a la posicion calculada
                    linea_nov_PI=archnov.readline()# lee la linea
                    lista_nov_PI=linea_nov_PI.split(',') #convierte en lista
                    #print(f"se creo una lista en el if PI!=0. \n archivo novedad posicion inicial cliente, linea {PI}: {lista_nov_PI}")
                    reg_sig=int(lista_nov_PI[4].strip(" ")) # aqui se hace un strip a modo de eiminar los espacios en las varaibles especificadas
                    #print("reg_siguiente: ", reg_sig)
                    reg_ant=int(lista_nov_PI[5].strip(" ")) # aqui se hace un strip a modo de eiminar los espacios en las varaibles especificada
                    #print("reg_ant: ", reg_ant)
                    if reg_sig == 0:
                        nro_factura_ant=int(lista_nov_PI[2].strip(" "))
                        #Nosostros al querer agregar un registro nuevo y al leer la linea de la PI el reg_sig = 0 entonces nuestro nro de factura anteior
                        # o reg_anterior va a ser el nro de factrua de la PI
                if reg_sig !=0:
                    #Si el registro siguiente es distinto de cero entrara en un bucle el cual ira salteando de linea en linea hasta que el reg_sig=0
                    #print("se ingreso a la condicional reg_sig!='0'")
                    while reg_sig!=0:
                        #print("ingresa al loop while hasta que el registro sig sea = 0")
                        with open ('Novedad.dat', 'r+') as archnov:
                            cal_pos_reg_sig=(int(long_carac_nov)*int(reg_sig))-int(long_carac_nov) # se traduce a (73*n)-73 
                            #print("calculo de la posicion del registro siguiente: ", cal_pos_reg_sig)
                            archnov.seek(cal_pos_reg_sig)
                            lista_arch_nov=archnov.readline().split(',')
                            #print(lista_arch_nov)
                            reg_sig=int(lista_arch_nov[4].strip(" "))
                            #print("reg_sig: ", reg_sig)
                            reg_ant=int(lista_arch_nov[5].strip(" "))
                            #print("reg_ant: ", reg_ant)
                            nro_factura_ant=int(lista_arch_nov[2].strip(" "))
                            #print("nro_factura_ant: ", nro_factura_ant)
                # Si el registro anterior es distinto de         
                
                if reg_sig ==0:
                    with open ('Novedad.dat', 'a+', encoding='utf-8') as archnov: #aqui se escribe en el archivo novedad agregando la linea nueva
                        #print("ingreso a la condicional reg_sig == 0")
                        archnov.write(f"{str(cod_cliente).ljust(10)},{fecha.ljust(23)},{str(nro_factura).ljust(10)},{str(importe).ljust(10)},{str(0).ljust(6)},{str(nro_factura_ant).ljust(6)},\n")
                    
                    with open ('Novedad.dat', 'r+', encoding='utf-8') as archnov: 
                        # Aqui se modifica la factura anterior rescribiendo el reg_sig con el nro de factua actual
                        calc_pos_nov_reg_sig=int(long_carac_nov*nro_factura_ant)-17 #esto se traduce a  (73*n)-17
                        #print("calculo posicion registro sig: ", calc_pos_nov_reg_sig)
                        archnov.seek(calc_pos_nov_reg_sig)
                        archnov.write(f",{str(nro_factura).ljust(6)},{str(reg_ant).ljust(6)},")
                        time.sleep(0.5)
                        #print('se inserto en el archivo novedad')
                
                #En esta parte del codigo se modifica la posicion final del archvio cliente.
                #modficar el calculo de la posiscion final
                long_linea_Client=long_carac_client
                #print("longitud de caracteres linea clientes: ", long_linea_Client)
                caracteres_hasta_pos_f=9
                calc_pos=(int(long_linea_Client)*int(cod_cliente))-caracteres_hasta_pos_f
                #print("calculo posicion registro sig: ", calc_pos_nov_reg_sig)

                with open('Clientes.dat', 'r+', encoding='utf-8') as client:
                    client_pos_seek=client.seek(calc_pos)
                    linea_cli_pos=client.readline()
                    #print("linea Cliente posicion final", linea_cli_pos)
                    client_pos_seek=client.seek(calc_pos)
                    client.write(f"{str(nro_factura).ljust(6)},")
                    time.sleep(0.5)


            if PI == '0':
                # Si la posicion inicial es igual a 0 entonces se escribira en el archivo novedad la nueva factura
                with open ('Novedad.dat', 'a+', encoding='utf-8') as archnov:
                    reg_ant=0
                    reg_sig=0
                    archnov.write(f"{str(cod_cliente).ljust(10)},{fecha.ljust(23)},{str(nro_factura).ljust(10)},{str(importe).ljust(10)},{str(reg_ant).ljust(6)},{str(reg_sig).ljust(6)},\n")
                    archnov.close()
                    PI= nro_factura
                    #print("Nro de factura: ", PI)
                
                # Se calcula la posicion inicial para poder reescribir PI con el nro de factura actual.
                long_linea_Client=long_carac_client
                caracteres_hasta_posi=17 # son 15 caracteres contando el salto de linea
                calc_pos=(int(long_linea_Client)*int(cod_cliente))-int(caracteres_hasta_posi)
                with open('Clientes.dat', 'r+', encoding='utf-8') as Client:
                    Client.seek(calc_pos)
                    linea_cli_pos=Client.readline()
                    #print("lista pos inicial pos final cliente",linea_cli_pos)
                    Client.seek(0)
                    client_pos_seek=Client.seek(calc_pos)
                    Client.write(f",{str(PI).ljust(6)},"+f"{str(PF).ljust(6)},")
                    time.sleep(0.5)
            
    else: 
        print("Salio del programa")
        break