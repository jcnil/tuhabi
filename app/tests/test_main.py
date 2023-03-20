from unittest import TestCase

from config.settings import connect_db
from app.core.process import PropertyProcess


class TestGetProperty(TestCase):
    @classmethod
    def setUpClass(cls):
        connect_db()
    
    def test_get_property(self):

    request = {
        "search": {
           "state": "Cundinamarca",
           "year": 2010,
           "city": "bogota"
        }
    }

    year = request.get('year')
    city = request.get('city')

    response = PropertyProcess.get_property(year,city)
  
    assert len(response["data"])>0
    assert response.get('status')==OK
