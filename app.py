from flask import Flask, render_template, request
import os

import boto3
from botocore.exceptions import ClientError

import factura_v1
import factura_datalab_v1
import filesController
from flask import send_file #by download

app = Flask(__name__)
UPLOAD_PATH = 'static/uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_PATH)


# @app.route('/')
# def index():
#     all_image_files = []
#     all_mp3_files = []
#     all_files_xml = []
#     all_files_csv = []
#     for filename in os.listdir(UPLOAD_FOLDER):       
#         ##files xml
#         if (filename.find('.xml') > -1):
#             all_files_xml.append(filename)
#         ## f .csv        
#         if (filename.find('.csv') > -1):
#             all_files_xml.append(filename)
#     return render_template('index.html', **locals());
##---------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('crearSesionIndex.html')    
##---------------------------------------------------
def index2():
    ##pagina .html ??
    # return '''<hr> <h3> <a href="/crearSesion">Crear sesion</a> </h3>
    # <hr>'''
    return render_template('crearSesionIndex.html')
##---------------------------------------------------------------------------
@app.route('/cerrarSesion', methods=[ 'POST' ])
def cerrarSesion():    
    #-------------------------------------------------------
    if request.method == 'POST':        
        sesion1=request.form.get("sesion")        
    #     return index(sesion)
    #-------------------------------------------------------
    return render_template('cerrarSesion.html', sesion=sesion1)
##---------------------------------------------------------------------------

def index(rutaDir):
    rutaDir = rutaDir.replace('.', '') #se elimina

    all_image_files = []
    all_mp3_files = []
    all_files_xml = []
    all_files_csv = []
    for filename in os.listdir(UPLOAD_FOLDER+rutaDir):        

        ##files xml
        if (filename.find('.xml') > -1):
            all_files_xml.append(filename)
        ## f .csv        
        if (filename.find('.csv') > -1):
            all_files_xml.append(filename)
        ## f .csv        
        if (filename.find('.xlsx') > -1):
            all_files_xml.append(filename)

    sesion1=rutaDir

    return render_template('index.html', **locals(), sesion=sesion1);
##---------------------------------------------------------------------------

#
def isImageFormat(link):
    if (link.find('.jpg') > -1 or link.find('.png') > -1 or link.find('.gif') > -1 or link.find('.jpeg') > -1):
        return True;
    return False;


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_path = '{}/{}'.format(UPLOAD_FOLDER, file.filename)
        file.save(upload_path)
        return 'ok'
##--------------------------------------------------------------------------
##----------------------------------------------------------------------------
# @app.route('/convertirCSV', methods=['GET', 'POST'])
# def convertirCSV():
# @app.route('/convertirCSV/<nombre>', methods=['GET', 'POST'])
# ##@app.route('/convertirCSV', methods=['GET', 'POST'])
# def convertirCSV (nombre):

@app.route('/convertirCSV/<nombre>')
##@app.route('/convertirCSV', methods=['GET', 'POST'])
def convertirCSV (nombre):

    # if request.method == 'GET':
    import factura_v1
        
    directorio="static/uploads/"

    nombreArchivo=nombre
        
    # return factura_v1.convertirCSV_v0( nombreArchivo, directorio )
    return factura_v1.convertirCSV_v2( nombreArchivo, directorio )    
    
##----------------------------------------------------------------------------
@app.route('/download/<nombre>')
def downloadFile_nombre (nombre):
    
    path = "static/uploads/"+nombre
    return send_file(path, as_attachment=True)

# @app.route('/download/<nombre>')
# def downloadFile_nombre (nombre):   
#     return nombre
# @app.route('/download')
# def downloadFile_nombre ():   
#     return "ok"
##---------------------------------------------------------------------------------
@app.route('/eliminar/<nombre>')
def deleteFile_nombre (nombre):
    from os import remove

    name=nombre
    path = "static/uploads/"+nombre
    remove(path)    

    return '<h3>Archivo eliminado</h3> '+nombre+'      <a href="/"> [ Inicio / Volver ]</a>'
##---------------------------------------------------------------------------------
@app.route('/addTOall/<nombref>')
def addTOall (nombref):

    ##return "agregado a Propiedades_Concentrado ok"
    nombre = nombref
    ruta= "static/uploads/"
    path = ruta + nombre
    f = open (path,'r')
    parrafo_f = f.read()
    ##print(parrafo_f)
    f.close()

    ##abrir f, estraer text, // crear new file o abrir file, abrir el file y agregar al final, cerrar f
    ##+ condiciones de cumplimiento
    ##-------------------------------------
    # ##f2 = open ("propiedadesConcentrado.csv", "a")##carpeta_Archivos
    # f2 = open ("carpeta_Archivos/Propiedades_Concentrado.csv", "a")
    # ##string2= nombref + " --- tras tres tris\n"
    # string2 = parrafo_f + "\n"
    # f2.write(string2)
    # f2.close()       
    # myJson= 'Agregado al final <hr> <a href="/list"> [ Volver a Archivos ]</a> '

    ##----------------------------------------    

    
    ##f2 = open ("carpeta_Archivos/Propiedades_Concentrado.csv", "a")

    f2 = open ( ruta + "FACTURAS_CONCENTRADO.csv", "a")    
    string2 = parrafo_f
    f2.write(string2)
    f2.close()       
    myJson= 'Agregado al final <hr> <a href="/"> [ Volver / Inicio ]</a> '
    return myJson
##----------------------------------------------------------------------------------------------
## crear directorio
@app.route('/createDirUser', methods=['POST'])
def createDirUser():
    nombreDir="nulo"
    if request.method == 'POST':
        nombreSesion=request.form.get("namedir")

    ##---------------------------------------------
    if nombreSesion== "":
        return index2()
    ## caracteres indeseados
    #array1[] -> for
    ##-------------------------------------------------------------
    caracteres=["ñ",",","[","]",".","\n","'","/","\\"," ","  ","ó","é"]
    ##-------------------------------------------------------------
    string0=""
    for i in range(0,len(nombreSesion) ):
        #----------------------------------------------
        for j in range(0,len(caracteres) ):
            if nombreSesion[i].lower() ==caracteres[j]:
                return index2()
    ##-------------------------------------------------

    ## nombre ya existente ??
    # comprobacion de nombres existentes
    # try:
    #     if os.exists(nombreSesion):
    #         return "<hr>La sesion ya existe.<hr>" + '<a href="/"> [ Inicio / Volver ]</a>'
    #         # return index2()
    # except:
    #     aux="nada"
    #     # return "<hr>La sesion ya existe.<hr>" + '<a href="/"> [ Inicio / Volver ]</a>'

    ##---------------------------------------------
    # import os
    # if os.path.exists(nombreSesion):
    #     return "<hr>La sesion ya existe.<hr>" + '<a href="/"> [ Inicio / Volver ]</a>'

    ##---------------------------------------------
    nombreDir=nombreSesion

    import os
    name=nombreDir
    # directorio = "./mdr_dir_test/"
    directorio = "./directorios/"+name
    crearDirectorio="./"+UPLOAD_PATH+"/directorios/"+name
    try:
        ##os.stat(crearDirectorio)
        if os.stat(crearDirectorio):
            # return "<hr>La sesion ya existe.<hr>" + '<a href="/"> [ Inicio / Volver ]</a>'
            if name != "Admin_123": # Mod datalab2022
                return "<hr>La sesion ya existe.<hr>" + '<a href="/"> [ Inicio / Volver ]</a>'
    except:
        os.mkdir(crearDirectorio)


    ### import json
    ##return "ruta-> "+directorio
    rutaDir=directorio
    ## return render_template('index.html', sesion=json.dumps(rutaDir))
    ##return render_template('index.html',**locals(), sesion=rutaDir)
    return index(rutaDir)
##------------------------------------------------------
## Crear sesion, de directorio
@app.route('/crearSesion')
def crearSesion():
    return render_template('crearSesion.html');
##----------------------------------------------------------------------------------------------
## control de folder para usuarios x
##----------------------------------------------------------------------------------------------
@app.route('/upload2', methods=['GET', 'POST'])
def upload2():
    if request.method == 'POST':
        file = request.files['file']
        sesion=request.form.get("sesion")
        upload_path = '{}/{}'.format(UPLOAD_FOLDER+"/"+sesion, file.filename)
        file.save(upload_path)
        ##return 'ok'
        return index(sesion)
##--------------------------------------------------------------------------
# @app.route('/download/<nombre>')
@app.route('/download2', methods=['GET', 'POST'])
def downloadFile_nombre2():

     #-------------------------------------------------------
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        nombre=request.form.get("nombre")
        
        # return "static/uploads"+sesion+"/"+nombre

        path = "static/uploads"+sesion+"/"+nombre
        return send_file(path, as_attachment=True)
        
                
    #------------------------------------------------------- 

# @app.route('/download/<nombre>')
# def downloadFile_nombre (nombre):   
#     return nombre
# @app.route('/download')
# def downloadFile_nombre ():   
#     return "ok"
##---------------------------------------------------------------------------------
# @app.route('/eliminar/<nombre>')
@app.route('/eliminar2', methods=['GET', 'POST'])
def deleteFile_nombre2():
    # return "Eliminar 2"
    from os import remove
    sesion=""
    nombre=""
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        nombre=request.form.get("nombre")

    #### ? name=nombre
    ##path = "static/uploads/"+nombre
    path = "static/uploads"+sesion+"/"+nombre
    remove(path)

    # REDIRECCIONAR AL INDEX DE LA SESION ACTUAL, TE REGRESA A G  

    ##return '<h3>Archivo eliminado</h3> '+nombre+'      <a href="/"> [ Inicio / Volver ]</a>'

    return  '<h3>Archivo eliminado</h3> ' + nombre +'<hr>'+ '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Sesion / Ver Archivos ]" >
        </form>
        '''
##---------------------------------------------------------------------------------
##---------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def sesionFolder():
    #-------------------------------------------------------
    if request.method == 'POST':     
        sesion=request.form.get("sesion")
        # return UPLOAD_FOLDER+"/"+sesion
        # return UPLOAD_FOLDER+sesion
        return index(sesion)        
    #-------------------------------------------------------    
##---------------------------------------------------------------------------
# @app.route('/convertirCSV2/<nombre>')
@app.route('/convertirCSV2', methods=['GET', 'POST'])
def convertirCSV2():

    # if request.method == 'GET':
    import factura_v1
        
    # directorio="static/uploads/"
    # nombreArchivo=nombre
    #-----------------------------------------------
    sesion=""
    nombre=""
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        nombre=request.form.get("nombre")

    ##path = "static/uploads"+sesion+"/"+nombre
    directorio="static/uploads"+sesion+"/"
    nombreArchivo=nombre
    #-----------------------------------------------
        
    # return factura_v1.convertirCSV_v0( nombreArchivo, directorio )
    # return factura_v1.convertirCSV_v2( nombreArchivo, directorio )
    return factura_v1.convertirCSV_v3_1( nombreArchivo, directorio ) + '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Inicio / Ver Archivos ]" >
        </form>
        '''
##---------------------------------------------------------------------------
##---------------------------------------------------------------------------
@app.route('/addDB', methods=['GET', 'POST'])
def addDB():

    # return "Agregar(do) ha Base de Datos"
    
    import factura_datalab_v1
    #-----------------------------------------------
    sesion=""
    nombre=""
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        nombre=request.form.get("nombre")
    ##path = "static/uploads"+sesion+"/"+nombre
    directorio="static/uploads"+sesion+"/"
    nombreArchivo=nombre
    #-----------------------------------------------
    # return "NUEVA CONEXION A SCRIPT1"  
    # ----------------------------------------------
    result=""
    arrayAux = []
    rt=""

    rt = filesController.addFileToDB( nombreArchivo, directorio )
    if rt == "EXISTS":
        result = "El archivo ya fue \"agregado antes\". "
        return result + '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Inicio / Ver Archivos ]" >
        </form>
        '''
    
    try:
        result = factura_datalab_v1.addToDataBase1( nombreArchivo, directorio )    
    except ValueError:        
        result = "El archivo no se pudo agregar a la BD. (Error)."
        return result + '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Inicio / Ver Archivos ]" >
        </form>
        '''
    
    # result = factura_datalab_v1.addToDataBase1( nombreArchivo, directorio )
    return result + '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Inicio / Ver Archivos ]" >
        </form>
        '''
##---------------------------------------------------------------------------------
@app.route('/addTOall2', methods=['GET', 'POST'])
def addTOall2():
    ##---------------------------------------------------------------
    sesion=""
    nombre=""
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        nombre=request.form.get("nombre")

    ##path = "static/uploads"+sesion+"/"+nombre
    directorio="static/uploads"+sesion+"/"    
    ##---------------------------------------------------------------
    ##return "agregado a Propiedades_Concentrado ok"
    # nombre = nombref
    ##ruta= "static/uploads/"
    ruta= "static/uploads"+sesion+"/"
    path = ruta + nombre
    f = open (path,'r')
    parrafo_f = f.read()
    ##print(parrafo_f)
    f.close()
    
    ##f2 = open ("carpeta_Archivos/Propiedades_Concentrado.csv", "a")

    f2 = open ( ruta + "FACTURAS_CONCENTRADO.csv", "a")    
    string2 = parrafo_f
    f2.write(string2)
    f2.close()       
    myJson= ' <h3> Agregado al final </h3> <hr> (Agregado a concentrado)<hr> '+ '''<form action="/regresar" method="post" class="">            
            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
            <input type="submit" value="[ Inicio / Ver Archivos ]" >
        </form>
        '''
    return myJson
##----------------------------------------------------------------------------------------------
@app.route('/refrescar', methods=['POST'])
def refrescar():
    sesion=""    
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        return index(sesion)    
    return render_template('crearSesionIndex.html')    
##----------------------------------------------------------
@app.route('/regresar', methods=['POST'])
def regresar():
    sesion=""    
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        return index(sesion)    
    return render_template('crearSesionIndex.html')    
##---------------------------------------------------------- 

@app.route('/eliminarSesion', methods=[ 'POST' ])
def eliminarSesion():
    #-------------------------------------------------------
    if request.method == 'POST':        
        sesion=request.form.get("sesion")
        # return UPLOAD_PATH+sesion

        ## FALTA COMPROBAR SI EL DIRECTORIO INDICADO EXISTE

        #eliminar directorio con files
        try:            
            from os import rmdir
            rmdir(UPLOAD_PATH+sesion)

            ##return "sesion eliminada a"
            return "<hr>La sesion se a eliminado.<hr>" + '<a href="/"> [ Inicio / Ir a inicio ]</a>'
        except:
            from shutil import rmtree
            rmtree(UPLOAD_PATH+sesion)

            ##return "sesion eliminada b"
            return "<hr>La sesion se a eliminado.<hr>" + '<a href="/"> [ Inicio / Ir a inicio ]</a>'
    #-------------------------------------------------------
    ##redireccionar a inicio
    ##return index2()
    return render_template('crearSesionIndex.html')
##---------------------------------------------------------------------------
# rutas post para acciones
#----------------------------------------
# agregar formularios con botones en fronted post


if __name__ == '__main__':
    app.run(debug=True)
