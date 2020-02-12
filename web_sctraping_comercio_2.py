from bs4 import BeautifulSoup
import requests
import pandas as pd


titulo_list = list()
fecha_list = list()
autor_list = list()


def siguiente(pag, intento = 0):
    req = requests.get(pag)
    soup = BeautifulSoup(req.content, "html.parser")
    link = soup.find_all('a', {'class': 'pagination__page'})
    #print (link[6].get('href'))
    #link[len(link) -1].get('href')
    url = 'https://elcomercio.pe' + link[len(link) -1].get('href')
    url_end = soup.find('p', {'class': 'pagination__page--disabled'})
    # ______________________________________________________________________
    entradas = soup.find_all('div', {'class': 'story-item__bottom'})
    # ______________________________________________________________________
    for entrada in entradas:
        titulo = entrada.find('h2', {'class' : 'story-item__content-title'}).getText()
        autor = entrada.find('a', {'class' : 'story-item__author'}).getText()
        fecha = entrada.find('p', {'class' : 'story-item__date'}).getText()
        #print ("{},  {},  {}".format(titulo, fecha, autor))
        titulo_list.append(titulo)
        fecha_list.append(fecha)
        autor_list.append(autor)
    #print (pag)
    # ______________________________________________________________________    
    if intento == 1:
        siguiente(url)
    else:
        if url_end == None:
            siguiente(url)

siguiente("https://elcomercio.pe/buscar/venezuela/todas/descendiente/800/?query=venezuela", 1)

#print(titulo_list, autor_list, fecha_list)

tabla = pd.DataFrame({'Noticias': titulo_list, 'Fechas': fecha_list, 'Autor': autor_list})

tabla.to_csv('scraping_comercio.csv', encoding = 'utf_32')

print (tabla)






    

    


   