import csv
from queue import Empty
import matplotlib.pyplot as plt

def list_of_countries():
    data = read_csv('./data.csv')
    pais = []
    for row in range(1,len(data)):
        pais.append(data[row].get('Country')) 
    return pais

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        cabecera = next(reader)
        data=[]
        for row in reader:
            iterable = zip(cabecera,row)
            CSV_dict = { key:value for key, value in iterable}
            data.append(CSV_dict)
    return data

def find_country(word):
    data = read_csv('./data.csv')
    pais = []
    for row in range(1,len(data)):
        pais.append(data[row].get('Country'))    
    print('esto es', pais)
    dict_countries = {pais[countries]:str(countries+1) for countries in range(1,len(pais))}
    try: 
        if word in dict_countries:
            num_country=dict_countries.get(word)
        else:
            num_country = 'Empty'
            raise Exception("Pais no encontrado")
        if num_country != 'Empty':
            country_info=data[int(num_country)]
    except Exception as error:
        print(error)
    return country_info

def popullation_stadistics(country_dict):
    graphic_info={}
    country_dict.pop('World Population Percentage')
    for text in country_dict:
        if 'Population' in text:
            graphic_info[text[0:4]]=country_dict[text]
    for text in graphic_info:
            graphic_info[text]=int(graphic_info[text])/1000000
    labels = list(graphic_info.keys())
    values = list(graphic_info.values())
    return labels,values #Informacion del pais

def generate_bar_chart(labels,values,country): 
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.xlabel('Years')  
    plt.ylabel('Millons of People')
    plt.title(country)
    plt.show()

def usser_request(listado):
    choose_country = input(f"Escoge el pais que deseas graficar\n")
    choose_country=choose_country.capitalize()
    while not choose_country in listado:
        print(f"OPCION NO VALIDA TE AYUDAREMOS CON LA LISTA DE PAISES A ELEGIR\n",listado)
        choose_country = input(f"Escoge el pais que deseas graficar\n")
        choose_country=choose_country.capitalize()
        
    return choose_country

if __name__ == '__main__':
    data = read_csv('./data.csv')
    listado=list_of_countries()
    print('*****'*10)
    choose_country=usser_request(listado)
    country_info=find_country(choose_country)
    labels,values = popullation_stadistics(country_info)
    generate_bar_chart(labels,values,choose_country)