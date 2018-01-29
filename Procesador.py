from xml.dom import minidom #Libreria para leer XML
import xlwt                 #Libreria par escritura en Excel
import os                   #No me acuerdo pa que era pero dejalo ahí jaja



listadoArchivos = os.listdir('.') #Obtiene el listado de archivos en un directorio, no lo necesitas creo
listadoArchivos = ["ExtraccionDimCliente.dtsx"] #Pone el nombre de un archivo para procesar, modifica este y pon el sln
listadoLimpio=[]

#Selecciona solo los archivos presentes en el directorio que terminan en .dtsx
for each in listadoArchivos: #Para todos los archivos en el directorio 
    if ".dtsx" in each:     #Si contienen .dtsx en algun lado
        listadoLimpio.append(each)  #Agregar a la lista de archivos a procesar nueva


print(listadoArchivos)

libro = xlwt.Workbook() #Crear un libro de excel
cursor=0;
hoja = libro.add_sheet('Documentación SSIS') #Agregar una hoja al libro
print("-- INICIALIZANDO COMPILADOR SSIS --")

for element in listadoLimpio: #Para cada archivo en la lista de archivos
    t=0#Persistencia del cursor a través de archivos
    y=0#Persistencia del cursor a través de archivos
    xmldoc = minidom.parse(element) #Abrir el archivo documento XML
    print("##Procesando: "+element)
    temp=0;
    coldfix=[]

    #def ObtenerNombreArchivo():
    print("Leyendo Nombre del archivo...")
    cont = 0;#Cursor para definir en que fila del excel estoy escribiendo
    
    listaConexiones = xmldoc.getElementsByTagName('DTS:Executable') #Encontrar el tag DTS:Excecutable
    conexion = listaConexiones[0].attributes['DTS:ObjectName'].value # Obtener el atributo DTS:ObjectName del tag previo
    nombreArchivo=conexion
    hoja.write(cursor+cont,0,nombreArchivo) #Escribir en el archivo hoja.write(fila,columna,valor)
    print(nombreArchivo)

    #def ObtenerNombreCajaPrincipal():
    print("Leyendo Nombre de Caja Principal...")
    cont = 0;
    listaConsultas = xmldoc.getElementsByTagName('DTS:Executable')#Encontrar el tag DTS:Excecutable
    for item in listaConsultas:
        if item.hasAttribute("DTS:ObjectName"):# Si el tag posee el atributo DTS:ObjectName
            if "dft" in item.attributes['DTS:ObjectName'].value.lower() and "archivos" not in item.attributes['DTS:ObjectName'].value.lower():
                #Si DTS:ObjectName al ponerlo en minusculas contiene dft y no contiene archivos
                nombreCajas2=item.attributes['DTS:ObjectName'].value #tomar el valor del atributo
                hoja.write(cursor+cont,1,nombreCajas2)#escribir en el excel
                print(nombreCajas2)
                coldfix.append(nombreCajas2)#ignora esto
                cont+=1
    y=cont

    #def ObtenerNombreCaja():
    print("Leyendo Nombre SubCaja...")
    cont = 0;
    listaConsultas = xmldoc.getElementsByTagName('component') #Obtener todos los elementos que tengan este tag
    for item in listaConsultas:
        if item.hasAttribute("name"): #Si los elementos tienen el atributo name
            if "origen" in item.attributes['name'].value.lower() and "excel" not in item.attributes['name'].value.lower():
                #Si el valor del atributo contiene "origen" y no tiene "excel"
                nombreCajas=item.attributes['name'].value#tomar el valor del atributo
                hoja.write(cursor+cont,2,nombreCajas)#escribirlo en el excel
                print(nombreCajas)
                cont+=1
    t=cont
                
                
    #def ObtenerConexiones():
    print("Leyendo Conexiones...")
    cont = 0;
    listaConexiones = xmldoc.getElementsByTagName('connection')
    for item in listaConexiones:
        conexion = item.attributes['connectionManagerRefId'].value
        if "STA" not in conexion.upper() and "EXCEL" not in conexion.upper() and "AX" in conexion.upper():
            conexion = conexion.split('[')[1][:-1] #Esto es un split porque el valor venia asi "[Valor]" para que quede "Valor"
            nombreConexiones=conexion
            hoja.write(cursor+cont,3,nombreConexiones)
            cont+=1


    #def ObtenerConsultas():
    print("Leyendo Consultas...")
    cont = 0;
    contA=0;
    ##Obtener las consultas
    listaConsultas = xmldoc.getElementsByTagName('property') #Lo mismo de arriba
    for item in listaConsultas:
        if item.hasAttribute("UITypeEditor"):
            temp = item.toxml().split(">") #Esto trae el valor del campo ej: <tag>Hola<\tag> entonces la funcion hallando la etiqueta tag, retorna Hola
            temp = temp[len(temp)-2]
            temp=temp.split("<")[0]
            nombreConsultas=temp
           # print(temp)
            if ("select" in temp.lower()):
                hoja.write(cursor+contA,4,nombreConsultas)
                #print(nombreConsultas)
                contA+=1
            cont+=1    
    print("Procesamiento Finalizado")

    cursor+=12

print("-- FINALIZANDO COMPILADOR SSIS --")
print("-- GUARDANDO ARCHIVO --")
libro.save("Test1.xls")#Guardar el excel


    










        


        
        
        
