from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'

# opening up connection and downloadind the page
uClient = uReq(myUrl) 
pageHtml = uClient.read()
uClient.close()

#html parse
pageSoup = soup(pageHtml, "html.parser")

#grabs the tables
tabla = pageSoup.findAll("tr", {"align":"right"})
tabla.pop(0) #Elimina la primera línea, de la primera tabla debido a que no nos interesa.

file = open("ibex.csv", "a")
file.write("Componente;CotFinal;CotMáxima;CotMínima;\n")


for componente in tabla:
	
	#Eliminamos los datos que sobran
	datos = componente.findAll("td")
	for i in [8,7,6,5,2,0]:
		datos.pop(i)

	#Nombre de la empresa	
	componenteNombre = componente.findAll("a")
	componenteNombre = componenteNombre[0].text

	#Cotización actual
	cotActual = datos[0].text


	#Cotización máxima del día actual
	cotMax = datos[1].text

	#Cotización mínima del día actual
	cotMin = datos[2].text

	file.write(componenteNombre + ";" + cotActual + ";" + cotMax + ";" + cotMin + ";\n")


file.close()