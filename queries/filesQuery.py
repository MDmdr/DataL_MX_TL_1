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

engineDB = "mysql" 
user = "root"
password = "54321bd"
host = "localhost"
port = "3306"
nameDB = "datalab2"


def conection():
    engine = create_engine(
        # 'mysql+pymysql://root:54321bd@localhost:3306/datalab2',
        'mysql+pymysql://root:54321bd@localhost:3306/'+nameDB,
        echo=True
    )
    return engine.connect()

def getTest():
    return "funtions test OK"
# test conection ?

def addFileTable_0( name ):
    print("\n add file table:")
    print(name)
    status = 1   # ----------       
    conn = conection()    
    text1 = """insert into files (
    name,
    status,
    datetime 
    ) VALUES (""" +" '"+name+"', "+str(status)+", NOW() ) "    
    # sql_text = text( text1 )
    # result = conn.execute(sql_text)
    try:
        sql_text = text( text1 )
        result = conn.execute(sql_text)        
    except ValueError:        
        # result = "El archivo no se pudo agregar a la BD. (Error)."
        print("Error add to BD. ")
        return ""
    conn.close()
    return ""
# ------------------------------------------------------------------------------------------
def addFileTable( name ):
    print("\n add file table:")
    print(name)
    status = 1   # ----------       
    conn = conection()    
    text1 = """insert into files (
    name,
    status,
    datetime 
    ) VALUES (""" +" '"+name+"', "+str(status)+", NOW() ) "    
    # sql_text = text( text1 )
    # result = conn.execute(sql_text)
    try:
        sql_text = text( text1 )
        result = conn.execute(sql_text)        
    except ValueError:        
        # result = "El archivo no se pudo agregar a la BD. (Error)."
        print("Error add to BD. ")
        return ""
    conn.close()

    array1 = []
    array1 = checkFileBD( name )
    return array1

def checkFileBD( nameFile ):
    conn = conection()    
    result = ""    
    sql_text = text("select id,name from files where name LIKE '%"+nameFile+"%' LIMIT 1")
    result = conn.execute(sql_text)
    conn.close()
    
    array1=[]    
    for row in result:
        print(row)  
        for item in row:
            array1.append(item)
    
    for x in array1:
        print( x )
    if len(array1) == 0:
        print("THE FILE NO EXISTS IN THE BD")
        return array1
    if len(array1)> 0:
        print("THE FILE EXISTS IN THE BD")
        return array1
    return array1
    # ##return""
