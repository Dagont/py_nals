import xlrd
import xlwt
 
#----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
 

 
    # get the first worksheet
    first_sheet = book.sheet_by_index(0)
 
    libro = xlwt.Workbook()
    hoja = libro.add_sheet('Documentación SSIS recuento')


    for a in range(1,160):
        celda3 = first_sheet.cell(a,2).value  #Celda de tabla origen
        print(celda3)
        celda3 = celda3.upper().split('_')
        if (len(celda3)>1):
            #print(len(celda3))
            celda5 = first_sheet.cell(a,4).value.upper()
            sub1 = celda3[len(celda3)-2]
            sub2 = celda3[len(celda3)-1]
            print("=> ("+sub1+") , ("+sub2+")") 
           # print(len(celda5))
           # print(celda5)
            if ((celda5.find(sub1)!=-1) or (celda5.find(sub2)!=-1)):
                hoja.write(a,0,"Si")
                print("=> Si\n")
                
            else:
                hoja.write(a,0,"No")
                print("=> No\n")
    libro.save("Test1.xls")
        
        
    

 
#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "test.xls"
    open_file(path)
