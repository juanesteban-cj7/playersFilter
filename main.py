players = [
    {
        'name': 'Jeronimo Arias', 
        'nationality': 'Colombia', 
        'years': 22,
        'countryClub': 'España',
        'club': 'Mallorca'
    },
    {
        'name': 'Alberto Diaz', 
        'nationality': 'México',
        'years': 28,
        'countryClub': 'México', 
        'club': 'Pumas'
    },
    {
        'name': 'Hugo Sheifty', 
        'nationality': 'Canadá', 
        'years': 33,
        'countryClub': 'Inglaterra',
        'club': 'Chelsea',
    },
    {
        'name': 'Filikh Shalka',
        'nationality': 'Suecia',
        'years': 19,
        'countryClub': 'España',
        'club': 'Real Madrid'
    },
    {
        'name': 'James Chuck',
        'nationality': 'Inglaterra', 
        'years': 27,
        'countryClub': 'Inglaterra', 
        'club': 'Arsenal', 
    },
    {
        'name': 'Mario Meister',
        'nationality': 'Alemania',
        'years': 36,
        'countryClub': 'Argentina',
        'club': 'Boca',
    },
    {
        'name': 'Marek Jetmar',
        'nationality': 'Dinamarca', 
        'years': 30,
        'countryClub': 'España',
        'club': 'Real Betis',
    },
    {
        'name': 'Kauan Barros', 
        'nationality': 'Brasil', 
        'years': 26,
        'countryClub': 'Alemania', 
        'club': 'Dortmund',
    },
]

def name(): 
    what_name = input('Ingresa el nombre que estas buscando: ')
    filtred_list = list(filter(lambda x: x['name'] == what_name, players)) 
    print(filtred_list)

def nationality(): 
    what_nationality = input('Ingresa el país de origen del jugador: ')
    filtred_list = list(filter(lambda x: x['nationality'] == what_nationality, players))
    print(filtred_list)

def years(): 
    min_or_max = input('Mínimo(mi) o máximo(ma): ')
    if min_or_max == 'mi': 
        number = int(input('Introduzca edad mínima del jugador: '))
        filtred_list = list(filter(lambda x: x['years'] >= number, players))  
        print(filtred_list)
    elif min_or_max == 'ma': 
        number = int(input('Introduzca edad máxima del jugador: '))
        filtred_list = list(filter(lambda x: x['years'] <= number, players))
        print(filtred_list)

def countryClub(): 
    what_country = input('Ingrese país del club del jugador: ')
    filtred_list = list(filter(lambda x: x['countryClub'] == what_country, players))
    print(filtred_list)

def club(): 
    what_club = input('Ingrese club del jugador: ')
    filtred_list = list(filter(lambda x: x['club'] == what_club, players))
    print(filtred_list)


select_filter = input('Introduce el filtro: ')
if select_filter == 'name': 
    name()
if select_filter == 'nationality': 
    nationality()
if select_filter == 'years': 
    years()
if select_filter == 'countryClub': 
    countryClub()
if select_filter == 'club': 
    club()
