# queries
from queries import filesQuery

def addFileToDB_test(archivoInput,directorio):
	archivo=directorio+archivoInput
	print("File input ->" + archivoInput )
	if directorio != "":
	    print("File route ->" + archivo)
	return "def addFileToDB test ok"

def addFileToDB(archivoInput,directorio):
	# print( filesQuery.getTest() )
	# filesQuery.addFileTable( archivoInput )

	# verificar si el archivo ya a sido registrado antes
	# print("FUNTIONS ADD ITEM BD")
	rt = ""
	msg = ""
	id_file = ""
	arrayAux = []
	arrayAux = filesQuery.checkFileBD( archivoInput )
	if len(arrayAux) > 0: # arrayAux mayor a 0
		print("THE FILE EXISTS IN THE BD")		
		id_file = arrayAux[0]   # Get id
		msg = "El archivo ya fue \"agregado antes\", con el id: "+str(id_file)
		rt="EXISTS"

	if len(arrayAux) == 0: # arrayAux igual 0
		print("THE FILE NO EXISTS IN THE BD")			
		arrayAux = filesQuery.addFileTable( archivoInput )
		id_file = arrayAux[0]
		msg = "El archivo ha sido \"registrado con exito\", con el id: "+str(id_file)
	# print("id_file: ", id_file)
	# return msg
	return rt

# MDR: fal agregar control por user sesion