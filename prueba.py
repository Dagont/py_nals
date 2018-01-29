from xml.dom import minidom
import xlwt
import os

listadoArchivos = os.listdir('.')
#listadoArchivos = ["ExtraccionFactGastosImportacion.dtsx"]
libro = xlwt.Workbook()
cursor=0;
hoja = libro.add_sheet('Documentación SSIS')
print("-- INICIALIZANDO COMPILADOR SSIS --")

for element in listadoArchivos:
    t=0
    xmldoc = minidom.parse(element)
    print("Procesando: "+element)
    temp=0;
    coldfix=[]

    #def ObtenerNombreArchivo():
    print("Leyendo Nombre del archivo...")
    cont = 0;
    listaConexiones = xmldoc.getElementsByTagName('DTS:Executable')
    conexion = listaConexiones[0].attributes['DTS:ObjectName'].value
    nombreArchivo=conexion
    hoja.write(cursor+cont,0,nombreArchivo)
    print(nombreArchivo)

    #def ObtenerNombreCajaPrincipal():
    print("Leyendo Nombre de Caja Principal...")
    cont = 0;
    listaConsultas = xmldoc.getElementsByTagName('DTS:Executable')
    for item in listaConsultas:
        if item.hasAttribute("DTS:ObjectName"):
            if "dft" in item.attributes['DTS:ObjectName'].value.lower() and "archivos" not in item.attributes['DTS:ObjectName'].value.lower():
                nombreCajas2=item.attributes['DTS:ObjectName'].value
                hoja.write(cursor+cont,1,nombreCajas2)
                print(nombreCajas2)
                coldfix.append(nombreCajas2)
                #print(coldfix)
                cont+=1

    #def ObtenerNombreCaja():
    print("Leyendo Nombre SubCaja...")
    cont = 0;
    listaConsultas = xmldoc.getElementsByTagName('component')
    for item in listaConsultas:
        if item.hasAttribute("name"):
            if "origen" in item.attributes['name'].value.lower() and "excel" not in item.attributes['name'].value.lower():
                nombreCajas=item.attributes['name'].value
                hoja.write(cursor+cont,2,nombreCajas)
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
            print(conexion)
            conexion = conexion.split('[')[1][:-1]
            nombreConexiones=conexion
           # print(coldfix[cursor+cont].lower())
            print(coldfix)
           # print("hola")
            print(cont)
            ##if ("oasis" not in coldfix[cont].lower()):
            hoja.write(cursor+cont,3,nombreConexiones)
            #else:
            #    hoja.write(cursor+cont,3,"OASIS")
            cont+=1


    #def ObtenerConsultas():
    print("Leyendo Consultas...")
    cont = 0;
    contA=0;
    ##Obtener las consultas
    listaConsultas = xmldoc.getElementsByTagName('property')
    for item in listaConsultas:
        if item.hasAttribute("UITypeEditor"):
            temp = item.toxml().split(">")
            temp = temp[len(temp)-2]
            temp=temp.split("<")[0]
            nombreConsultas=temp
            print(temp)
            if ("select" in temp.lower()):
               # if "oasis" not in coldfix[cont].lower():
                hoja.write(cursor+contA,4,nombreConsultas)
                print(nombreConsultas)
                contA+=1
            cont+=1    
            #else:
             #   if "oasis" in coldfix[cont].lower():
              #      hoja.write(cursor+contA,4,"--")
               #     print("--")
                #    contA+=1
                 #   cont+=1
    print("Procesamiento Finalizado")
    cursor+=t

print("-- FINALIZANDO COMPILADOR SSIS --")
print("-- GUARDANDO ARCHIVO --")
libro.save("Test.xls")


    










        


        
        
        
