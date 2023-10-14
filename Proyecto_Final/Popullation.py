import csv

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
    dict_countries = {pais[countries]:str(countries+1) for countries in range(1,len(pais))}
    if word in dict_countries:
        num_country=dict_countries.get(word)
    else:
        num_country = 'Empty'
        print("No se encontro el pais")
    country_info=data[int(num_country)]
    return country_info

def popullation_stadistics(country_dict):
    graphic_info={}
    for text in country_dict:
        if 'Population' in text:
            graphic_info[text]=country_dict[text]
    graphic_info.pop('World Population Percentage')
    print(graphic_info)

if __name__ == '__main__':
    data = read_csv('./data.csv')
    #print(data[0])
    print('*****'*10)
    #usser_choice=input('Escribe el nombre del pais a graficar')
    country_info=find_country('Argentina')
    print(type(country_info))
    popullation_stadistics(country_info)
    