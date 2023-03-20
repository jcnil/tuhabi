

class PropertyModel():
    
    id: int 
    address: str
    city: str
    state: str
    price: float
    description: str
    year: int

    def to_json(self):

        return {
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "price": self.price,
            "description": self.description,
            "year": self.year
        }
