
from app.core.handlers import PropertyHandler

if __name__ == '__main__':
    url = ''
    search = {'year': 2010, 'city': 'bogota'}
    headers = { 'Conten-Type' : 'application/json'}

    year = search.get('year')
    city = search.get('city')

    response = PropertyHandler.get_property(year,city)
