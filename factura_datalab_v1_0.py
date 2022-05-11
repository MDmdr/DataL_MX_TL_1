from xml.dom.minidom import parse, parseString
from lxml import etree as ET

def convertirCSV(archivoInput,archivoOuput):
	return 'archivo convertido test ->'+archivoInput

def test():
	return 'test fun exitoso'

##----------------------------------------------------------------------
def addToDataBase(archivoInput,directorio):

	archivo=directorio+archivoInput
	print(" Archivo input -->" + archivoInput )
	print(archivo)

	# def obtenerFactura(archivo):-----------------------------------
	string1=""
	string1="Comprobante,Emisor,Receptor,Conceptos,Impuestos"+'\n'
	# f3 = open (archivo+".csv",'wb')
	
	array=archivoInput.split('.')
	print( "solo name --> " + array[0] )
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
		print("Fecha ->"+node.getAttribute("Fecha"))
		# print(node.getAttribute("Sello"))
		print("FormaPago ->"+node.getAttribute("FormaPago"))
		print("NoCertificado ->"+node.getAttribute("NoCertificado"))
		# print(node.getAttribute("Certificado"))
		print("CondicionesDePago ->"+node.getAttribute("CondicionesDePago"))
		print("SubTotal ->"+node.getAttribute("SubTotal"))
		print("Moneda ->"+node.getAttribute("Moneda"))
		print("Total ->"+node.getAttribute("Total"))
		print("TipoDeComprobante ->"+node.getAttribute("TipoDeComprobante"))
		print("MetodoPago ->"+node.getAttribute("MetodoPago"))
		print("LugarExpedicion ->"+node.getAttribute("LugarExpedicion"))

		# # string1=string1 + " Version: "+node.getAttribute("Version")
		# string1=string1 + " Version: "+node.getAttribute("Version")
		# string1=string1 + " Serie: "+node.getAttribute("Serie")
		# string1=string1 + " Folio: "+node.getAttribute("Folio")
		# string1=string1 + " Fecha: "+node.getAttribute("Fecha")
		# # print(node.getAttribute("Sello"))
		# string1=string1 + " FormaPago: "+node.getAttribute("FormaPago")
		# string1=string1 + " NoCertificado: "+node.getAttribute("NoCertificado")
		# # print(node.getAttribute("Certificado"))
		# string1=string1 + " CondicionesDePago: "+node.getAttribute("CondicionesDePago")
		# string1=string1 + " SubTotal: "+node.getAttribute("SubTotal")
		# string1=string1 + " Moneda: "+node.getAttribute("Moneda")
		# string1=string1 + " Total: "+node.getAttribute("Total")
		# string1=string1 + " TipoDeComprobante: "+node.getAttribute("TipoDeComprobante")
		# string1=string1 + " MetodoPago: "+node.getAttribute("MetodoPago")
		# string1=string1 + " LugarExpedicion: "+node.getAttribute("LugarExpedicion")

		# f3.write( string1 + ',' )
		# string1=""



	print("#-------------------------------------------------------------")
	print("Emisor: \n")
	for node in dom.getElementsByTagName("cfdi:Emisor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		# print("Nombre: "+ str( node.getAttribute("Nombre")) )
		print("Nombre ->"+ node.getAttribute("Nombre") )
		print("RegimenFiscal ->"+node.getAttribute("RegimenFiscal"))

		# string1=string1 + " Rfc: "+node.getAttribute("Rfc")
		# string1=string1 + " Nombre: "+ node.getAttribute("Nombre")
		# string1=string1 + " RegimenFiscal: "+node.getAttribute("RegimenFiscal")
		# if "," in string1:
		# 	string1 = string1.replace(',', '/') #se elimina
		# f3.write( string1 + ',' )
		# string1=""

	print("#-------------------------------------------------------------")
	print("Receptor: \n")
	for node in dom.getElementsByTagName("cfdi:Receptor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		print("Nombre ->"+node.getAttribute("Nombre"))
		print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		# string1=string1 + " Rfc: "+node.getAttribute("Rfc")
		# string1=string1 + " Nombre: "+node.getAttribute("Nombre")
		# string1=string1 + " UsoCFDI: "+node.getAttribute("UsoCFDI")
		# f3.write( string1 + ',' )
		# string1=""

	print("#-------------------------------------------------------------")
	print("Conceptos: \n")

	for node in dom.getElementsByTagName("cfdi:Conceptos"):
		for node1 in node.getElementsByTagName("cfdi:Concepto"):
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

##----------------------------------------------------------------------
def addToDataBase_0(archivoInput,directorio):
	return '<h3>Archivo agregado ha BD</h3> '+archivoInput
##----------------------------------------------------------------------



##----------------------------------------------------------------------
def convertirCSV_v3_1(archivoInput,directorio):

	# from xml.dom.minidom import parse, parseString
	# from lxml import etree as ET

	archivo=directorio+archivoInput
	print(" Archivo input -->" + archivoInput )
	print(archivo)

	# def obtenerFactura(archivo):-----------------------------------
	string1=""
	string1="Comprobante,Emisor,Receptor,Conceptos,Impuestos"+'\n'
	# f3 = open (archivo+".csv",'wb')
	
	array=archivoInput.split('.')
	print( "solo name --> " + array[0] )
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
		print("Fecha ->"+node.getAttribute("Fecha"))
		# print(node.getAttribute("Sello"))
		print("FormaPago ->"+node.getAttribute("FormaPago"))
		print("NoCertificado ->"+node.getAttribute("NoCertificado"))
		# print(node.getAttribute("Certificado"))
		print("CondicionesDePago ->"+node.getAttribute("CondicionesDePago"))
		print("SubTotal ->"+node.getAttribute("SubTotal"))
		print("Moneda ->"+node.getAttribute("Moneda"))
		print("Total ->"+node.getAttribute("Total"))
		print("TipoDeComprobante ->"+node.getAttribute("TipoDeComprobante"))
		print("MetodoPago ->"+node.getAttribute("MetodoPago"))
		print("LugarExpedicion ->"+node.getAttribute("LugarExpedicion"))

		# string1=string1 + " Version: "+node.getAttribute("Version")
		string1=string1 + " Version: "+node.getAttribute("Version")
		string1=string1 + " Serie: "+node.getAttribute("Serie")
		string1=string1 + " Folio: "+node.getAttribute("Folio")
		string1=string1 + " Fecha: "+node.getAttribute("Fecha")
		# print(node.getAttribute("Sello"))
		string1=string1 + " FormaPago: "+node.getAttribute("FormaPago")
		string1=string1 + " NoCertificado: "+node.getAttribute("NoCertificado")
		# print(node.getAttribute("Certificado"))
		string1=string1 + " CondicionesDePago: "+node.getAttribute("CondicionesDePago")
		string1=string1 + " SubTotal: "+node.getAttribute("SubTotal")
		string1=string1 + " Moneda: "+node.getAttribute("Moneda")
		string1=string1 + " Total: "+node.getAttribute("Total")
		string1=string1 + " TipoDeComprobante: "+node.getAttribute("TipoDeComprobante")
		string1=string1 + " MetodoPago: "+node.getAttribute("MetodoPago")
		string1=string1 + " LugarExpedicion: "+node.getAttribute("LugarExpedicion")

		f3.write( string1 + ',' )
		string1=""



	print("#-------------------------------------------------------------")
	print("Emisor: \n")
	for node in dom.getElementsByTagName("cfdi:Emisor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		# print("Nombre: "+ str( node.getAttribute("Nombre")) )
		print("Nombre ->"+ node.getAttribute("Nombre") )
		print("RegimenFiscal ->"+node.getAttribute("RegimenFiscal"))

		string1=string1 + " Rfc: "+node.getAttribute("Rfc")
		string1=string1 + " Nombre: "+ node.getAttribute("Nombre")
		string1=string1 + " RegimenFiscal: "+node.getAttribute("RegimenFiscal")
		if "," in string1:
			string1 = string1.replace(',', '/') #se elimina
		f3.write( string1 + ',' )
		string1=""

	print("#-------------------------------------------------------------")
	print("Receptor: \n")
	for node in dom.getElementsByTagName("cfdi:Receptor"):
		print("Rfc ->"+node.getAttribute("Rfc"))
		print("Nombre ->"+node.getAttribute("Nombre"))
		print("UsoCFDI ->"+node.getAttribute("UsoCFDI"))

		string1=string1 + " Rfc: "+node.getAttribute("Rfc")
		string1=string1 + " Nombre: "+node.getAttribute("Nombre")
		string1=string1 + " UsoCFDI: "+node.getAttribute("UsoCFDI")
		f3.write( string1 + ',' )
		string1=""

	print("#-------------------------------------------------------------")
	print("Conceptos: \n")

	for node in dom.getElementsByTagName("cfdi:Conceptos"):
		for node1 in node.getElementsByTagName("cfdi:Concepto"):
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

						string1=string1 + " Base: " + node4.getAttribute("Base")
						string1=string1 + "Impuestos: " + node4.getAttribute("Impuestos")
						string1=string1 + "TipoFactor: " + node4.getAttribute("TipoFactor")
						string1=string1 + "TasaOCuota: " + node4.getAttribute("TasaOCuota")
						string1=string1 + "Importe: " + node4.getAttribute("Importe")

			print("#...............................")
			# <cfdi:Impuestos>
			# 		<cfdi:Traslados>
			# 			<cfdi:Traslado
		# print(node.getAttribute("Rfc"))
		# print(node.getAttribute("Nombre"))
		# print(node.getAttribute("UsoCFDI"))
		f3.write( string1 )
		f3.write( ',' )
		string1=""

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

				string1=string1 + " Impuesto: "+ node2.getAttribute("Impuesto")
				string1=string1 + " TipoFactor: "+ node2.getAttribute("TipoFactor")
				string1=string1 + " TasaOCuota: "+ node2.getAttribute("TasaOCuota")
				string1=string1 + " Importe: "+ node2.getAttribute("Importe")				
				# if(i5==0):
				# 	print("Importe ->"+ node2.getAttribute("Importe"))
				# 	i5=i5+1
			#
	string1=string1.replace(',',' / ')
	print(string1)
	print("[---------------------------------------]")
	print(string1)
	f3.write( string1 )
	f3.write( ',' )
	f3.write( "\n" )
	string1=""

	## Imprimir los resultados en un archivo
	##string1= """Anyo,Marca,Modelo,Descripcion,Precio """

	##f3 = open (archivo+".csv",'wb')
	##f3.write( string1 + '\n' )
	f3.close()
	# return 'archivo convertido test ->'+archivoInput
	return '<h3>Archivo convertido ha CSV</h3> '+archivoInput