from xml.dom.minidom import parse, parseString
# from lxml import etree as ET

# queries
from queries import functions

# def convertirCSV(archivoInput,archivoOuput):
# 	return 'archivo convertido test ->'+archivoInput

def test():
	return 'test function ok'


##----------------------------------------------------------------------
def addToDataBase1(archivoInput,directorio):

	print( functions.getTest() ) # TSest

	addTablePrincipal_DB(archivoInput,directorio)
	# return "" ### comentar para permitir la siguiente operacion

	archivo=directorio+archivoInput
	print("File input ->" + archivoInput )
	if directorio != "":
	    print("File route ->" + archivo)
	

	# def obtenerFactura(archivo):-----------------------------------
	string1=""
	string1="Comprobante,Emisor,Receptor,Conceptos,Impuestos"+'\n'
	# f3 = open (archivo+".csv",'wb')

	#----- Datalab 2022 -----------------------------------------------
	nombreEmisor=""
	fechaFactura=""
	id_last_product=0
	id_client=0 # id_last_client in BD with the name equal
	#------------------------------------------------------------------
	
	array=archivoInput.split('.')
	# print( "Only name-> " + array[0] )
	##f3 = open (archivo+".csv",'w')
	## f3 = open (directorio+array[0]+".csv",'w')
	
	# dom = parse(archivo)
	dom = parse(directorio+archivoInput)

	print("--------------------------------------------------------")	

	print("Comprobante: \n")

	for node in dom.getElementsByTagName("cfdi:Comprobante"):	
		print("Version ->"+node.getAttribute("Version"))
		print("Serie ->"+node.getAttribute("Serie"))
		print("Folio ->"+node.getAttribute("Folio"))
		print("Fecha ->"+node.getAttribute("Fecha")) ## datalab bd
		# print(node.getAttribute("Sello"))
		print("FormaPago ->"+node.getAttribute("FormaPago"))
		print("NoCertificado ->"+node.getAttribute("NoCertificado"))
		# print(node.getAttribute("Certificado"))
		print("CondicionesDePago ->"+node.getAttribute("CondicionesDePago"))
		print("SubTotal ->"+node.getAttribute("SubTotal")) ## datalab bd
		print("Moneda ->"+node.getAttribute("Moneda"))
		print("Total ->"+node.getAttribute("Total"))
		print("TipoDeComprobante ->"+node.getAttribute("TipoDeComprobante"))
		print("MetodoPago ->"+node.getAttribute("MetodoPago"))
		print("LugarExpedicion ->"+node.getAttribute("LugarExpedicion"))

		fechaFactura = node.getAttribute("Fecha") # Fecha de venta

		



	print("#-------------------------------------------------------------")
	print("Emisor: \n")
	for node in dom.getElementsByTagName("cfdi:Emisor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		# print("Nombre: "+ str( node.getAttribute("Nombre")) )
		print("Nombre ->"+ node.getAttribute("Nombre") )
		print("RegimenFiscal ->"+node.getAttribute("RegimenFiscal"))
		
		nombreEmisor = str( node.getAttribute("Nombre") )

	print("#-------------------------------------------------------------")
	print("Receptor: \n")
	for node in dom.getElementsByTagName("cfdi:Receptor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		print("Nombre ->"+node.getAttribute("Nombre")) ## datalab bd
		print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		print("FUNTIONS ADD ITEM BD")
		arrayAux=[]
		arrayAux = functions.checkClientBD( str( node.getAttribute("Nombre") ) )
		if len(arrayAux) == 0:
			print("THE CLIENT NO EXISTS IN THE BD")			
			arrayAux = functions.saveClient( str( node.getAttribute("Nombre") ) ) # CLIENT
			id_client = arrayAux[0]
		if len(arrayAux) > 0:
			print("THE CLIENT EXISTS IN THE BD")
			# obtengo id
			id_client = arrayAux[0]
		### functions.saveClient( str( node.getAttribute("Nombre") ) ) # CLIENT

		print("ID CLIENT ->", id_client)

		

	print("#-------------------------------------------------------------")
	print("Conceptos: \n")

	for node in dom.getElementsByTagName("cfdi:Conceptos"):
		for node1 in node.getElementsByTagName("cfdi:Concepto"):
			print("Datalab 2022")
			print("Cantidad-> "+ str( node1.getAttribute("Cantidad") ) )  ## datalab bd
			print("Descripcion-> "+ str( node1.getAttribute("Descripcion") ) )  ##datalab bd

			arrayAux=[]
			print("FUNTIONS ADD ITEM BD") # SAVE PRODUCT TO BD						
			arrayAux = functions.checkProductBD( str( node1.getAttribute("Descripcion") ) ) # ¿Product exist in th BD?			
			if len(arrayAux) == 0:
				print("THE PRODUCT NO EXISTS IN THE BD")
				# registro el producto y obtengo su id
				arrayAux = functions.saveProducts( str(node1.getAttribute("Descripcion")), str(node1.getAttribute("Cantidad")), str(node1.getAttribute("NoIdentificacion")), nombreEmisor )
				id_last_product = arrayAux[0]
			if len(arrayAux) > 0:
				print("THE PRODUCT EXISTS IN THE BD")
				# obtengo id
				id_last_product = arrayAux[0]

			print("ID LAST PRODUCT-> ", id_last_product)
            
			# id_last_product = functions.saveProducts( str(node1.getAttribute("Descripcion")), str(node1.getAttribute("Cantidad")), str(node1.getAttribute("NoIdentificacion")), nombreEmisor )
            
			# NoIdentificacion
			# Cantidad
			# Descripcion
			# Importe
			# ##saveSales(cantidad,description,importe,idProduct): #saveSales
			functions.saveSales( str(node1.getAttribute("Cantidad")),str(node1.getAttribute("Descripcion")), str(node1.getAttribute("Importe")), int(id_last_product), fechaFactura, id_client )
			
			print("ClaveUnidad ->"+ str( node1.getAttribute("ClaveUnidad") ) )			

			string1=string1 + " ClaveUnidad: "+ str( node1.getAttribute("ClaveUnidad") )

			for node2 in node1.getElementsByTagName("cfdi:Impuestos"):
				for node3 in node2.getElementsByTagName("cfdi:Traslados"):
					for node4 in node3.getElementsByTagName("cfdi:Traslado"):
						print( "Base -> " + node4.getAttribute("Base"))
						print( "Impuestos -> " + node4.getAttribute("Impuestos"))
						print( "TipoFactor -> " + node4.getAttribute("TipoFactor"))
						print( "TasaOCuota -> " + node4.getAttribute("TasaOCuota"))
						print( "Importe -> " + node4.getAttribute("Importe"))

						

			print("#...............................")
			# <cfdi:Impuestos>
		
		# print(node.getAttribute("Rfc"))
		

	print("#--------------------------------------------------------")
	print("Impuestos: \n")
	# i5=0

	for node in dom.getElementsByTagName("cfdi:Impuestos"):	
		print("TotalImpuestosTrasladados -> "+ node.getAttribute("TotalImpuestosTrasladados"))

		string1=string1 + " TotalImpuestosTrasladados: "+ node.getAttribute("TotalImpuestosTrasladados")

		for node1 in node.getElementsByTagName("cfdi:Traslados"):
			for node2 in node1.getElementsByTagName("cfdi:Traslado"):
				print( "Impuesto ->"+ node2.getAttribute("Impuesto"))
				print("TipoFactor ->"+ node2.getAttribute("TipoFactor"))
				print("TasaOCuota ->"+ node2.getAttribute("TasaOCuota"))
				print("Importe ->"+ node2.getAttribute("Importe"))

				
			#
	print("#-------------------------------------------------------------")
	print("fx:nameNode: \n")

	# fx:Calle
	print( dom.getElementsByTagName("fx:CdgPaisEmisor") ) 
	print( dom.getElementById("fx:CdgPaisEmisor") )

	# for node in dom.getElementsByTagName("fx:FactDocMX"):	
	# 	# print("TotalImpuestosTrasladados -> "+ node.getAttribute("TotalImpuestosTrasladados"))
	# 	# string1=string1 + " TotalImpuestosTrasladados: "+ node.getAttribute("TotalImpuestosTrasladados")
	# 	for node1 in node.getElementsByTagName("fx:Identificacion"):
	# 		# print( node1.getElementsByTagName("fx:CdgPaisEmisor") )
	# 		# print( node1.childNodes )
	# 		# print( node1.getAttribute("fx:TipoDeComprobante") )
	# 		for node2 in node1.getElementsByTagName("fx:CdgPaisEmisor"):
	# 			# print( "Impuesto ->"+ node2.getAttribute("Impuesto"))
	# 			print(node2.getAttribute() )
	
	print("#-------------------------------------------------------------")

	addTablePrincipal_DB(archivoInput,directorio)
	# try:
 	#        result = factura_datalab_v1.addToDataBase1( nombreArchivo, directorio )    
 	#	   except ValueError:        
 	#        result = "El archivo no se pudo agregar a la BD. (Error)."
 	#        return result + '''<form action="/regresar" method="post" class="">            
 	#            <input id="sesion" name="sesion" type="hidden" value="'''+sesion+'''">
 	#            <input type="submit" value="[ Inicio / Ver Archivos ]" >
 	#        </form>
 	#        '''
	
	
	return '<h3>Archivo agregado ha base de datos</h3> '+archivoInput
##----------------------------------------------------------------------
##----------------------------------------------------------------------

def addTablePrincipal_DB(archivoInput,directorio):
	
	#----- Datalab 2022 -----------------------------------------------
	nombreEmisor=""
	fechaFactura=""
	id_last_product=0
	id_client=0 # id_last_client in BD with the name equal
	#------------------------------------------------------------------
	# ##factura_json
		
	# dom = parse(archivo)
	dom = parse(directorio+archivoInput)

	print("--------------------------------------------------------")	

	print("Comprobante: \n")

	for node in dom.getElementsByTagName("cfdi:Comprobante"):	
		print("Version ->"+node.getAttribute("Version"))
		print("Serie ->"+node.getAttribute("Serie"))
		print("Folio ->"+node.getAttribute("Folio"))
		print("Fecha ->"+node.getAttribute("Fecha")) ## datalab bd
		# print(node.getAttribute("Sello"))
		print("FormaPago ->"+node.getAttribute("FormaPago"))
		print("NoCertificado ->"+node.getAttribute("NoCertificado"))
		# print(node.getAttribute("Certificado"))
		print("CondicionesDePago ->"+node.getAttribute("CondicionesDePago"))
		print("SubTotal ->"+node.getAttribute("SubTotal")) ## datalab bd
		print("Moneda ->"+node.getAttribute("Moneda"))
		print("Total ->"+node.getAttribute("Total"))
		print("TipoDeComprobante ->"+node.getAttribute("TipoDeComprobante"))
		print("MetodoPago ->"+node.getAttribute("MetodoPago"))
		print("LugarExpedicion ->"+node.getAttribute("LugarExpedicion"))
		fechaFactura = node.getAttribute("Fecha") # Fecha de venta

		comprobante = {}
		# comprobante[""] = node.getAttribute("")	
		comprobante["CondicionesDePago"] = node.getAttribute("CondicionesDePago")
		comprobante["Moneda"] = node.getAttribute("Moneda")
		comprobante["MetodoPago"] = node.getAttribute("MetodoPago")
		comprobante["Folio"] = node.getAttribute("Folio")
		comprobante["TipoDeComprobante"] = node.getAttribute("TipoDeComprobante")

	print("#-------------------------------------------------------------")
	print("Emisor: \n")
	for node in dom.getElementsByTagName("cfdi:Emisor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		# print("Nombre: "+ str( node.getAttribute("Nombre")) )
		print("Nombre ->"+ node.getAttribute("Nombre") )
		print("RegimenFiscal ->"+node.getAttribute("RegimenFiscal"))		
		nombreEmisor = str( node.getAttribute("Nombre") )

	print("#-------------------------------------------------------------")
	print("Receptor: \n")
	for node in dom.getElementsByTagName("cfdi:Receptor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		print("Nombre ->"+node.getAttribute("Nombre")) ## datalab bd
		print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		receptor = {}
		receptor["Rfc"] = node.getAttribute("Rfc")
		receptor["Nombre"] = node.getAttribute("Nombre")
		receptor["UsoCFDI"] = node.getAttribute("UsoCFDI")	

	print("#-------------------------------------------------------------")
	print("Conceptos: \n")
	conceptos = []	
	for node in dom.getElementsByTagName("cfdi:Conceptos"):
		for node1 in node.getElementsByTagName("cfdi:Concepto"):			
			# print("Cantidad-> "+ str( node1.getAttribute("Cantidad") ) )  ## datalab bd
			# print("Descripcion-> "+ str( node1.getAttribute("Descripcion") ) )  ##datalab bd			
			# print("ClaveUnidad ->"+ str( node1.getAttribute("ClaveUnidad") ) )
			# # string1=string1 + " ClaveUnidad: "+ str( node1.getAttribute("ClaveUnidad") )
			print("Datalab 2022")
			concepto = {}			
			concepto["NoIdentificacion"] = str(node1.getAttribute("NoIdentificacion") )
			concepto["Cantidad"] = str(node1.getAttribute("Cantidad") )
			concepto["ClaveUnidad"] = str(node1.getAttribute("ClaveUnidad") )
			concepto["Descripcion"] = str(node1.getAttribute("Descripcion") )
			concepto["ValorUnitario"] = str(node1.getAttribute("ValorUnitario") )
			concepto["Importe"] = str(node1.getAttribute("Importe") )
			conceptos.append( concepto )
			# break
			
			# for node2 in node1.getElementsByTagName("cfdi:Impuestos"):
			# 	for node3 in node2.getElementsByTagName("cfdi:Traslados"):
			# 		for node4 in node3.getElementsByTagName("cfdi:Traslado"):
			# 			print( "Base -> " + node4.getAttribute("Base"))
			# 			print( "Impuestos -> " + node4.getAttribute("Impuestos"))
			# 			print( "TipoFactor -> " + node4.getAttribute("TipoFactor"))
			# 			print( "TasaOCuota -> " + node4.getAttribute("TasaOCuota"))
			# 			print( "Importe -> " + node4.getAttribute("Importe"))

						

			print("#...............................")
			# <cfdi:Impuestos>		
		# print(node.getAttribute("Rfc"))
	print("Imprimir Conceptos:")
	print(conceptos)
	# print(conceptos[0])
	# print(conceptos[1])
		

	print("#--------------------------------------------------------")
	print("Impuestos: \n")
	# i5=0

	for node in dom.getElementsByTagName("cfdi:Impuestos"):	
		print("TotalImpuestosTrasladados -> "+ node.getAttribute("TotalImpuestosTrasladados"))
		# string1=string1 + " TotalImpuestosTrasladados: "+ node.getAttribute("TotalImpuestosTrasladados")
		for node1 in node.getElementsByTagName("cfdi:Traslados"):
			for node2 in node1.getElementsByTagName("cfdi:Traslado"):
				print( "Impuesto ->"+ node2.getAttribute("Impuesto"))
				print("TipoFactor ->"+ node2.getAttribute("TipoFactor"))
				print("TasaOCuota ->"+ node2.getAttribute("TasaOCuota"))
				print("Importe ->"+ node2.getAttribute("Importe"))

	print("--------------------------------------------------------------------")
	# <cfdi:Complemento>
	# <tfd:TimbreFiscalDigital
	fechaTimbrado = ""
	for node in dom.getElementsByTagName("cfdi:Complemento"):		
		for node1 in node.getElementsByTagName("tfd:TimbreFiscalDigital"):
			# print("FechaTimbrado -> "+ node1.getAttribute("FechaTimbrado"))
			fechaTimbrado = str( node1.getAttribute("FechaTimbrado") )
			print("fechaTimbrado: ", fechaTimbrado)
	TipoDeComprobante = ""
	for node1 in dom.getElementsByTagName("cfdi:Addenda"):
		print("cfdi:Addenda")
		for node2 in node1.getElementsByTagName("fx:FactDocMX"): # fx:FactDocMX
			print("fx:FactDocMX")
			for node3 in node2.getElementsByTagName("fx:Identificacion"): #fx:Identificacion
				print("fx:Identificacion")
				##print( str(node2.get("fx:TipoDeComprobante")) )		
				# for node4 in node3.getElementsByTagName("fx:TipoDeComprobante"): #fx:Identificacion
				# 	print("fx:TipoDeComprobante")
				# 	print("¿TipoDeComprobante?")
				# 	TipoDeComprobante = str( node4.getAttribute("TipoDeComprobante") )
				# 	print("TipoDeComprobante: ", TipoDeComprobante)
	# print("#-------------------------------------------------------------")
	# print("fx:nameNode: \n")
	# # fx:Calle
	# print( dom.getElementsByTagName("fx:CdgPaisEmisor") ) 
	# print( dom.getElementById("fx:CdgPaisEmisor") )	
	# print("#-------------------------------------------------------------")	
	try:
 	    result = functions.addTablePrincipal( comprobante, receptor, conceptos, fechaTimbrado, TipoDeComprobante )    
	except ValueError:        
	    result = "No se pudo agregar el contenido a la tabla principal (Error). <br> "
	    return result
	# text message exit
	return " function addToTablePrincipal_BD ok"

#---------------------------------------------------------------------------------------

def addTablePrincipal_DB_0(archivoInput,directorio):
	print(" function addToTablePrincipal_BD ok")
	archivo=directorio+archivoInput
	print("File input ->" + archivoInput )
	if directorio != "":
	    print("File route ->" + archivo)
	return " function addToTablePrincipal_BD ok"








##----------------------------------------------------------------------
def addToDataBase(archivoInput,directorio):

	print( functions.getTest() )

	archivo=directorio+archivoInput
	print("File input ->" + archivoInput )
	if directorio != "":
	    print("File route ->" + archivo)
	

	# def obtenerFactura(archivo):-----------------------------------
	string1=""
	string1="Comprobante,Emisor,Receptor,Conceptos,Impuestos"+'\n'
	# f3 = open (archivo+".csv",'wb')
	
	array=archivoInput.split('.')
	# print( "Only name-> " + array[0] )
	##f3 = open (archivo+".csv",'w')
	f3 = open (directorio+array[0]+".csv",'w')
	
	# dom = parse(archivo)
	dom = parse(directorio+archivoInput)

	print("--------------------------------------------------------")	

	print("Comprobante: \n")

	for node in dom.getElementsByTagName("cfdi:Comprobante"):	
		print("Version ->"+node.getAttribute("Version"))
		print("Serie ->"+node.getAttribute("Serie"))
		print("Folio ->"+node.getAttribute("Folio"))
		print("Fecha ->"+node.getAttribute("Fecha")) ## datalab bd
		# print(node.getAttribute("Sello"))
		print("FormaPago ->"+node.getAttribute("FormaPago"))
		print("NoCertificado ->"+node.getAttribute("NoCertificado"))
		# print(node.getAttribute("Certificado"))
		print("CondicionesDePago ->"+node.getAttribute("CondicionesDePago"))
		print("SubTotal ->"+node.getAttribute("SubTotal")) ## datalab bd
		print("Moneda ->"+node.getAttribute("Moneda"))
		print("Total ->"+node.getAttribute("Total"))
		print("TipoDeComprobante ->"+node.getAttribute("TipoDeComprobante"))
		print("MetodoPago ->"+node.getAttribute("MetodoPago"))
		print("LugarExpedicion ->"+node.getAttribute("LugarExpedicion"))

		



	print("#-------------------------------------------------------------")
	print("Emisor: \n")
	for node in dom.getElementsByTagName("cfdi:Emisor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		# print("Nombre: "+ str( node.getAttribute("Nombre")) )
		print("Nombre ->"+ node.getAttribute("Nombre") )
		print("RegimenFiscal ->"+node.getAttribute("RegimenFiscal"))
		

	print("#-------------------------------------------------------------")
	print("Receptor: \n")
	for node in dom.getElementsByTagName("cfdi:Receptor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		print("Nombre ->"+node.getAttribute("Nombre")) ## datalab bd
		print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		

	print("#-------------------------------------------------------------")
	print("Conceptos: \n")

	for node in dom.getElementsByTagName("cfdi:Conceptos"):
		for node1 in node.getElementsByTagName("cfdi:Concepto"):
			print("Datalab 2022")
			print("Cantidad-> "+ str( node1.getAttribute("Cantidad") ) )  ## datalab bd
			print("Descripcion-> "+ str( node1.getAttribute("Descripcion") ) )  ##datalab bd

			print("ClaveUnidad ->"+ str( node1.getAttribute("ClaveUnidad") ) )			

			string1=string1 + " ClaveUnidad: "+ str( node1.getAttribute("ClaveUnidad") )

			for node2 in node1.getElementsByTagName("cfdi:Impuestos"):
				for node3 in node2.getElementsByTagName("cfdi:Traslados"):
					for node4 in node3.getElementsByTagName("cfdi:Traslado"):
						print( "Base -> " + node4.getAttribute("Base"))
						print( "Impuestos -> " + node4.getAttribute("Impuestos"))
						print( "TipoFactor -> " + node4.getAttribute("TipoFactor"))
						print( "TasaOCuota -> " + node4.getAttribute("TasaOCuota"))
						print( "Importe -> " + node4.getAttribute("Importe"))

						# string1=string1 + " Base: " + node4.getAttribute("Base")
						# string1=string1 + "Impuestos: " + node4.getAttribute("Impuestos")
						# string1=string1 + "TipoFactor: " + node4.getAttribute("TipoFactor")
						# string1=string1 + "TasaOCuota: " + node4.getAttribute("TasaOCuota")
						# string1=string1 + "Importe: " + node4.getAttribute("Importe")

			print("#...............................")
			# <cfdi:Impuestos>
			# 		<cfdi:Traslados>
			# 			<cfdi:Traslado
		# print(node.getAttribute("Rfc"))
		# print(node.getAttribute("Nombre"))
		# print(node.getAttribute("UsoCFDI"))
		# #mdr 2022 datalab
		# f3.write( string1 )
		# f3.write( ',' )
		# string1=""

	print("#--------------------------------------------------------")
	print("Impuestos: \n")
	# i5=0

	for node in dom.getElementsByTagName("cfdi:Impuestos"):	
		print("TotalImpuestosTrasladados -> "+ node.getAttribute("TotalImpuestosTrasladados"))

		string1=string1 + " TotalImpuestosTrasladados: "+ node.getAttribute("TotalImpuestosTrasladados")

		for node1 in node.getElementsByTagName("cfdi:Traslados"):
			for node2 in node1.getElementsByTagName("cfdi:Traslado"):
				print( "Impuesto ->"+ node2.getAttribute("Impuesto"))
				print("TipoFactor ->"+ node2.getAttribute("TipoFactor"))
				print("TasaOCuota ->"+ node2.getAttribute("TasaOCuota"))
				print("Importe ->"+ node2.getAttribute("Importe"))

				# string1=string1 + " Impuesto: "+ node2.getAttribute("Impuesto")
				# string1=string1 + " TipoFactor: "+ node2.getAttribute("TipoFactor")
				# string1=string1 + " TasaOCuota: "+ node2.getAttribute("TasaOCuota")
				# string1=string1 + " Importe: "+ node2.getAttribute("Importe")

				# # if(i5==0):
				# # 	print("Importe ->"+ node2.getAttribute("Importe"))
				# # 	i5=i5+1
			#
	print("#-------------------------------------------------------------")
	print("fx:nameNode: \n")

	# fx:Calle
	print( dom.getElementsByTagName("fx:CdgPaisEmisor") ) 
	print( dom.getElementById("fx:CdgPaisEmisor") )

	for node in dom.getElementsByTagName("fx:FactDocMX"):	
		# print("TotalImpuestosTrasladados -> "+ node.getAttribute("TotalImpuestosTrasladados"))
		# string1=string1 + " TotalImpuestosTrasladados: "+ node.getAttribute("TotalImpuestosTrasladados")
		for node1 in node.getElementsByTagName("fx:Identificacion"):
			# print( node1.getElementsByTagName("fx:CdgPaisEmisor") )
			# print( node1.childNodes )
			# print( node1.getAttribute("fx:TipoDeComprobante") )
			for node2 in node1.getElementsByTagName("fx:CdgPaisEmisor"):
				# print( "Impuesto ->"+ node2.getAttribute("Impuesto"))
				print(node2.getAttribute() )
	# for node in dom.getElementsByTagName("cfdi:Receptor"):
	# 	print("Rfc ->"+node.getAttribute("Rfc"))
	# 	print("Nombre ->"+node.getAttribute("Nombre"))
	# 	print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		# string1=string1 + " Rfc: "+node.getAttribute("Rfc")
		# string1=string1 + " Nombre: "+node.getAttribute("Nombre")
		# string1=string1 + " UsoCFDI: "+node.getAttribute("UsoCFDI")
		# f3.write( string1 + ',' )
		# string1=""

	print("#-------------------------------------------------------------")
	# ## datalab 2022
	# string1=string1.replace(',',' / ')
	# print(string1)
	# print("[---------------------------------------]")
	# print(string1)
	# f3.write( string1 )
	# f3.write( ',' )
	# f3.write( "\n" )
	# string1=""

	## Imprimir los resultados en un archivo
	##string1= """Anyo,Marca,Modelo,Descripcion,Precio """

	##f3 = open (archivo+".csv",'wb')
	##f3.write( string1 + '\n' )
	f3.close()
	# return 'archivo convertido test ->'+archivoInput
	return '<h3>Archivo convertido ha CSV</h3> '+archivoInput
##----------------------------------------------------------------------


