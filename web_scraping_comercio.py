from bs4 import BeautifulSoup
import requests

pag_madre = "https://elcomercio.pe/buscar/venezuela/todas/descendiente/"
cant_pag = 803
contador = 0

for i in range(1, cant_pag):

    #___________________________________________________________________________
    if i > 1:
        url = "%s/%d/" % (pag_madre, i)
    else:
        url = pag_madre

    #___________________________________________________________________________
    req = requests.get(url)
    #___________________________________________________________________________
    status_code = req.status_code
    if status_code == 200:

        # ______________________________________________________________________
        soup = BeautifulSoup(req.text, "html.parser")

        # ______________________________________________________________________
        entradas = soup.find_all('div', {'class': 'story-item__bottom'})

        # ______________________________________________________________________
        for entrada in entradas:
            contador += 1
            titulo = entrada.find('h2', {'class' : 'story-item__content-title'}).getText()
            fecha = entrada.find('a', {'class' : 'story-item__author'}).getText()
            autor = entrada.find('p', {'class' : 'story-item__date'}).getText()

            print ("{} - {},  {},  {}".format(contador, titulo, fecha, autor))
            
    else: 
        print ('Status Code', status_code) 
        break