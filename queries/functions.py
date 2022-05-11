
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text


from datetime import datetime
import uuid
def getDate():  
    now = datetime.now()
    # now.year  # now.month  # now.day
    return str(now.year)+"/"+str(now.month)+"/"+str(now.day)
def getHour():  
    now = datetime.now()    
    return str(now.hour)+":"+str(now.minute)+":"+str(now.second)
def getUid():    
    return str(uuid.uuid4().hex)



def conection():
    engine = create_engine(
        'mysql+pymysql://root:54321bd@localhost:3306/datalab2',
        echo=True
    )
    return engine.connect()


# cruds

# def getTypesVehicles():
# 	print( "tipos de veiculos, desde functions")
# 	# setTypeVehicle()
# 	return "tipos de veiculos, desde functions"

def getTest():
    return "funtions test OK"

def saveClient(name):
    print("SAVE CLIENT BD")
    # check name not exits in BD, no mames repit
    conn = conection()
    # Check names no repited
    # result = ""
    # sql_text = text("select nombre from cadenas where nombre LIKE '%"+name+"%' LIMIT 1")
    # result = conn.execute(sql_text)
    
    # for row in result:        
    #     for item in row:
    #         print("item-> ", item)
    #         print("name-> ", name)
    #         # name = name+"otro"
    #         if name in item:
    #             print("THE NAME EXISTS IN THE BD")
    #             return ""
    #         else:
    #             print("NAMES NOT EQUALS")


    # return ""
    sql_text = text("INSERT INTO  datalab2.cadenas ( nombre, active, datetime ) VALUES ( '"+name+"', 1, NOW() ) ")    
    result = conn.execute(sql_text)
    conn.close()


    array1 = []
    array1 = checkClientBD(name)
    print("id Client saveClient() -> ", array1[0] )

    # return ""
    return array1

def saveProducts_0(name, num, noId, nameEmit): # num = catidad vendida
    
    print("name insert?->")
    print(name)

    # text1 = "insert into  datalab2.productos ( nombre, active ) VALUES ( ' "+ name +" ', 1 ) "
    # sql_text = text(text1)
    conn = conection()
    # sql_text = text( "INSERT INTO datalab2.productos (insertDate) VALUES (NOW())" )
    # result = conn.execute(sql_text)

    noId=1010

    text1 = "insert into  datalab2.productos ( nombre, active, insertDate, idMySuite, nombreMySuite  ) VALUES ( '"+name+"', 1, NOW(), "+noId+", '"+nameEmit+"' ) "
    sql_text = text(text1)
      
    # conn = conection()
    # result = conn.execute(sql_text, args).first()
    result = conn.execute(sql_text)
    # ultimoIDInsertado=""
    # ultimoIDInsertado = conn.insert_id() ## get id in the end time/moment
    # result_proxy = connection.execute(sql_query, args).first()
    # last_id=result_proxy.inserted_primary_key[0]
    # last_id=result.inserted_primary_key[0]
    sql_text = text( "SELECT LAST_INSERT_ID()" )
    id_result = conn.execute(sql_text)
    print("RESULT QUERY->")
    print(id_result)
    for item in id_result:
        print(item)
        for x in item:
            print(x)
            id_last = x
            break
    ##return ""

    conn.close()
    return id_last # r ""

def saveProducts(name, num, noId, nameEmit): # num = catidad vendida
    
    print("name insert?->")
    print(name)

    # text1 = "insert into  datalab2.productos ( nombre, active ) VALUES ( ' "+ name +" ', 1 ) "
    # sql_text = text(text1)
    conn = conection()
    # sql_text = text( "INSERT INTO datalab2.productos (insertDate) VALUES (NOW())" )
    # result = conn.execute(sql_text)

    # noId=1010
    if noId == "":
        noId = 0

    text1 = "insert into  datalab2.productos ( nombre, active, insertDate, idMySuite, nombreMySuite  ) VALUES ( '"+name+"', 1, NOW(), "+str(noId)+", '"+name+"' ) "
    sql_text = text(text1)    
    result = conn.execute(sql_text)
    conn.close()

    array1 = []
    array1 = checkProductBD(name)
    print("id product saveProducts() -> ", array1[0] )
    
    return array1


# def saveSales(noId,cantidad,description,importe,idProduct): #saveSales
def saveSales(cantidad,description,importe,idProduct,fechaFactura, id_client): #saveSales
    # print("ID PRODUCTO->")
    # print(idProduct)
    # print("FECHA FACTURA->")
    # print(fechaFactura)
    FC = fechaFactura.split('T') # 2020-05-15T19:13:58
    date = FC[0]
    print(date)
    # return ""
    print("ID CLIENTE - def saveSales ->")
    print(id_client)
    # return ""

    conn = conection()
    
    text1 = "insert INTO  datalab2.ventas ( idProducto, ventas_mxn, ventas_unidades, active, insertDate, fechaVenta, idCadena ) VALUES ( "+str(idProduct)+", "+importe+" ,"+ cantidad +", 1, NOW(), '"+date+"', "+str(id_client)+" ) "
    # text1 = "insert INTO  datalab2.ventas ( idProducto, ventas_mxn, ventas_unidades, active, insertDate, fechaVenta ) VALUES ( "+str(idProduct)+", "+importe+" ,"+ cantidad +", 1, NOW(), '"+date+"' ) "
    # text1 = "insert INTO  datalab2.ventas ( ventas_mxn, ventas_unidades, active, insertDate ) VALUES ( "+importe+" ,"+ cantidad +", 1, NOW() ) "
    sql_text = text( text1 )
    result = conn.execute(sql_text)

    

    conn.close()
    print("SAVE SALE IN DATA BASE")

    return ""

def checkProductBD(nameProduct): # Check name product exist in BD?    
    conn = conection()    
    result = ""
    # nameProduct = "nombreNombreX"
    sql_text = text("select id,nombre from productos where nombre LIKE '%"+nameProduct+"%' LIMIT 1")
    result = conn.execute(sql_text)
    conn.close()
    # print("RESULT EXP MDR ok->")
    # print("RESULT EXP MDR->")
    # print(result)

    array1=[]
    i=0
    for row in result:
        print(row)  
        for item in row:
            array1.append(item)

    for x in array1:
        print( x )
    if len(array1) == 0:
        print("THE PRODUCT NO EXISTS IN THE BD")
        return array1
    if len(array1)> 0:
        print("THE PRODUCT EXISTS IN THE BD")
        return array1
    return array1

def checkClientBD(nameClient): # Check name Client/cadena exist in BD?    
    conn = conection()    
    result = ""
    # nameClient = "nombreNombreX"
    sql_text = text("select id,nombre from cadenas where nombre LIKE '%"+nameClient+"%' LIMIT 1")
    result = conn.execute(sql_text)
    conn.close()
    
    array1=[]
    i=0
    for row in result:
        print(row)  
        for item in row:
            array1.append(item)

    for x in array1:
        print( x )
    if len(array1) == 0:
        print("THE CLIENT NO EXISTS IN THE BD")
        return array1
    if len(array1)> 0:
        print("THE CLIENT EXISTS IN THE BD")
        return array1
    return array1
#----------------------------------------------------------------------------------------------------------
def addTablePrincipal( comprobante, receptor, conceptos, fechaTimbrado, TipoDeComprobante ):
    print("\n add table principal")
    print(comprobante["CondicionesDePago"])    
    print(comprobante["MetodoPago"])
    print(comprobante["Moneda"])
    print(comprobante["Folio"])
    print(comprobante["TipoDeComprobante"])
    print(receptor["Rfc"] )
    print(receptor["Nombre"])
    print(receptor["UsoCFDI"])
    print(conceptos)
    print(fechaTimbrado)
    print(TipoDeComprobante)
    TipoDeComprobante = ""

    #fx:TextosDeCabecera
    #fx:TextosDePie

    # conceptos = ""
    conn = conection()

    ### error test  MDR  
    # text1 = """insert into tequilalocosellinoriginal (
    # fecha_timbrado,
    # condicionesPago,
    # metodoPago,
    # moneda,
    # folio,
    # receptor_rfc,
    # receptor_nombre,
    # receptor_usocfdi,
    # conceptos,
    # tipodeComprobante
    # ) VALUES (""" +"'"+fechaTimbrado +"', '"+str(comprobante["CondicionesDePago"])+"', '"+str(comprobante["MetodoPago"])+"', '"+str(comprobante["Moneda"])+"', "+comprobante["Folio"]+", '"+str(receptor["Rfc"])+"', '"+str(receptor["Nombre"])+"', '"+str(receptor["UsoCFDI"])+"', \""+str(conceptos)+"\", '"+TipoDeComprobante+"' , ) "
    
    ###print(comprobante["TipoDeComprobante"]) ##??
    text1 = """insert into tequilalocosellinoriginal (
    fecha_timbrado,
    condicionesPago,
    metodoPago,
    moneda,
    folio,
    receptor_rfc,
    receptor_nombre,
    receptor_usocfdi,
    conceptos,
    tipodeComprobante
    ) VALUES (""" +"'"+fechaTimbrado +"', '"+str(comprobante["CondicionesDePago"])+"', '"+str(comprobante["MetodoPago"])+"', '"+str(comprobante["Moneda"])+"', "+comprobante["Folio"]+", '"+str(receptor["Rfc"])+"', '"+str(receptor["Nombre"])+"', '"+str(receptor["UsoCFDI"])+"', \""+str(conceptos)+"\", '"+TipoDeComprobante+"' ) "

    
    # sql_text = text( text1 )
    # result = conn.execute(sql_text)
    try:
        sql_text = text( text1 )
        result = conn.execute(sql_text)        
    except ValueError:        
        # result = "El archivo no se pudo agregar a la BD. (Error)."
        print("TABLE ORIGINAL -> El archivo no se pudo agregar a la BD. (Error).")
        return ""
        

    conn.close()

    return ""
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# def setTypeVehicle():

# 	conn = conection()

# 	sql_text = text("INSERT INTO  bd1.t_test (id, text ) VALUES ( 16, 'texto  insert desde t 16' ) ")
# 	result = conn.execute(sql_text)

# 	conn.close()

# 	return ""

def saveRegisterTypeVehicle( TypeVehicle, description ):
    # typeVehicles TABLE
    # id VARCHAR(80), 
    # type_vehicle VARCHAR(150),
    # description VARCHAR(350)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.typeVehicles (id, type_vehicle, description ) VALUES ( ' "+getUid()+" ' , ' "+TypeVehicle+" ' , ' "+description+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print("tipo de vehiculo registrado en bd1")
    return ""


def saveRegisterVehicle( mark, car_plate, proprietor, type_vehicle ):
    # vehicles TABLE
    # id VARCHAR(80), 
    # mark VARCHAR(150),
    # car_plate VARCHAR(100),
    # proprietor VARCHAR(150),
    # type_vehicle VARCHAR(100)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.vehicles (id, mark, car_plate, proprietor, type_vehicle ) VALUES ( ' "+getUid()+" ' , ' "+mark+" ' , ' "+car_plate+" '  , ' "+proprietor+" ' , ' "+type_vehicle+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" vehiculo registrado en base de VEHICULOS bd1")
    return ""


def saveRegisterPayment( car_plate, amount, status ): ## ??? id_de_estancia
    # payments TABLE
    # id VARCHAR(80), 
    # car_plate VARCHAR(100),
    # amount FLOAT(100,3),
    # status VARCHAR(70)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.vehicles (id, car_plate, amount, status ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+amount+" ' , ' "+status+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Pago registrado en la tabla de la base de datos de pagos bd1")
    return ""


def saveRegisterParking( car_plate, hour_entry, hour_exit, proprietor, amount_acc ): ## ??? 
    # register_parking TABLE
    # id VARCHAR(80), 
    # car_plate VARCHAR(100),
    # hour_entry VARCHAR(60),
    # hour_exit VARCHAR(60),
    # proprietor VARCHAR(150),
    # amount_acc FLOAT(100,3)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, hour_entry, hour_exit, proprietor, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+hour_entry+" ' , ' "+hour_exit+" ' , ' "+proprietor+" ' , ' "+amount_acc+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Registro de Estancia almacenado en la tabla de la base de datos")
    return ""

# get registers tables ----------------------------------------------------------

def getRegisterTypeVehicle( TypeVehicle, description ):
    # typeVehicles TABLE
    # id VARCHAR(80), 
    # type_vehicle VARCHAR(150),
    # description VARCHAR(350)
    conn = conection()
    # SELECT * FROM bd1.typeVehicles;
    sql_text = text(" SELECT * FROM bd1.typeVehicles ")
    result = conn.execute(sql_text)

    conn.close()
    # print("Todos los Tipos de vehiculos obtenidos")
    # return ""
    array1=[]
    i=0

    # Number of rows
    for row in result:
        print(row)        
        for col in row:
            array1.append(col)
            print(col)
        array1.append("/")
        i=i+1
    # return result
    return array1

def getRegisterTypeVehicleAll():
    
    conn = conection()
    
    sql_text = text(" SELECT * FROM bd1.typeVehicles ")
    result = conn.execute(sql_text)

    conn.close()
    
    array1=[]
    i=0

    # Number of rows
    for row in result:
        print(row)        
        for col in row:
            array1.append(col)
            print(col)
        array1.append("/")
        i=i+1
    # return result
    return array1

def getRegisterVehicle( mark, car_plate, proprietor, type_vehicle ):
    # vehicles TABLE
    # id VARCHAR(80), 
    # mark VARCHAR(150),
    # car_plate VARCHAR(100),
    # proprietor VARCHAR(150),
    # type_vehicle VARCHAR(100)
    conn = conection()

    sql_text = text("SELECT * FROM  bd1.vehicles ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Todos los vehiculos obtenidos de la base de datos")
    return ""

# buscar matricula
def searchCarPlate(car_plate):
    result="No hay matricula"
    conn = conection()

    sql_text = text("SELECT * FROM bd1.vehicles WHERE car_plate='"+car_plate+"' ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Matricula buscada: "+ str(result) )
    return ""

# ------------------------------------------------------------------------------------
# create data in BD
def saveEntryCarParking( car_plate, date_entry, hour_entry, type_vehicle):
    # conn = conection()
    # sql_text = text("INSERT INTO  bd1.vehicles (id, car_plate, amount, status ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+amount+" ' , ' "+status+" ' ) ")
    # result = conn.execute(sql_text)
    # conn.close()
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_entry, hour_entry ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date_entry+" ' , ' "+hour_entry+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    return ""

# updates data in the bd, of register in BD
# def saveExitCarParking( car_plate, date, hour, type_vehicle):

#     # se busca id ? y car_plate
#     # id, car_plate
#     # (UPDATE bd1.t_test SET id=8, text='texto update a 8' WHERE id=9)

#     "UPDATE bd1.register_parking date_exit=date,hour_exit=hour WHERE id=id AND car_plate=car_plate"
    
#     text("UPDATE bd1.register_parking date_exit=date,hour_exit=hour WHERE id=id AND car_plate=car_plate")
    


#     conn = conection()

#     text=text(UPDATE bd1.register_parking SET phone_no='Phone No',cust_city='Kolkata',grade=1 WHERE id='id' AND car_plate='car_plate')

#     sql_text = text("INSERT INTO  bd1.register_parking (date_exit, hour_exit, proprietor, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+hour_entry+" ' , ' "+hour_exit+" ' , ' "+proprietor+" ' , ' "+amount_acc+" ' ) ")
#     result = conn.execute(sql_text)

#     conn.close()
#     return ""

# def saveExitCarParking( car_plate, date, hour, type_vehicle): # ???
#     if type_vehicle == "oficial":        
#         saveRegister_Oficia()
#         return ""
#     if type_vehicle == "residente":        
#         saveRegister_Residente()
#         return ""
#     if type_vehicle == "no_residente":
#         saveRegister_No_residente()
#         return ""
#     else:
#         return "false"
#     return "false"

def saveRegister_Oficial(car_plate, date, hour):
    # aux=searchCarPlate(car_plate)
    aux1="NULL"
    aux2="NULL"
    conn = conection()

    # sql_text = text("SELECT id FROM bd1.register_parking WHERE car_plate='"+car_plate+"' AND date_exit='"+aux1+"' AND hour_exit='"+aux2+"'  ")
    sql_text = text("SELECT id FROM bd1.register_parking WHERE car_plate='"+car_plate+"' ")
    result = conn.execute(sql_text)

    conn.close()
    print("result: ")
    print(f"Numero de filas = {result.rowcount}.")
    # Number of rows
    for row in result:
        print(row)
    # -----------------------------------------------------
    id=getUid()
    amount_acc="0" #str()
    conn = conection()

    # "INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '  , ' "+amount_acc+" '  ) "

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '  , 0.0  ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""
def exit_saveRegister_Oficial(car_plate, date, hour, identifier):     
    # -----------------------------------------------------    
    amount_acc="0"
    conn = conection()

    text1="update bd1.register_parking SET hour_exit='"+hour+"',date_exit='"+date+"',amount_acc='"+amount_acc+"' WHERE id LIKE '%"+identifier+"%'"

    sql_text = text(text1)
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""

def saveRegister_Residente(car_plate, date, hour):
    # -----------------------------------------------------
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""
def exit_saveRegister_Residente(car_plate, date, hour, identifier):     
    # -----------------------------------------------------    
    amount_acc="0"
    conn = conection()
    text1="update bd1.register_parking SET hour_exit='"+hour+"',date_exit='"+date+"',amount_acc='"+amount_acc+"' WHERE id LIKE '%"+identifier+"%'"
    sql_text = text(text1)
    result = conn.execute(sql_text)
    conn.close()
    # -----------------------------------------------------
    return ""

def saveRegister_No_residente(car_plate, date, hour):
    # -----------------------------------------------------
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""
def exit_saveRegister_No_residente(car_plate, date, hour, identifier):     
    # -----------------------------------------------------    
    amount_acc="0"
    conn = conection()
    text1="update bd1.register_parking SET hour_exit='"+hour+"',date_exit='"+date+"',amount_acc='"+amount_acc+"' WHERE id LIKE '%"+identifier+"%'"
    sql_text = text(text1)
    result = conn.execute(sql_text)
    conn.close()
    # -----------------------------------------------------
    return ""

# -------------------------------------------------------------------------------
def getAllRegisters():
    conn = conection()
    
    sql_text = text(" SELECT * FROM register_parking ")
    result = conn.execute(sql_text)

    conn.close()

    # ??array1[][]=""
    # dim_row = 2
    # dim_columns = 2
    # output = [[0 for x in range(dim_columns)] for i in range(dim_row)]

    array1=[]
    i=0

    # Number of rows
    for row in result:
        print(row)
        # array1[i].append()
        # array1.append("/")
        for col in row:
            array1.append(col)
            print(col)
        array1.append("/")
        i=i+1
    # return result
    return array1

def checkCarPlateRegister(car_plate):
    conn = conection()

    # "select id,car_plate from register_parking where car_plate LIKE '%"+car_plate+"%' AND hour_exit IS NULL AND date_exit IS NULL LIMIT 1"

    sql_text = text("select id from register_parking where car_plate LIKE '%"+car_plate+"%' AND hour_exit IS NULL AND date_exit IS NULL LIMIT 1")
    result = conn.execute(sql_text)

    conn.close()
    print("functions result->")
    print(result)
    print("functions result row->")
    aux=""
    for row in result:
        print(row)
        aux=row
        for col in row:
            aux=col
    if aux=="":
        print("vacio")
    else:
        print("aux->")
        print(aux)


    return aux





