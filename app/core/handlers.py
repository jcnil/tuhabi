from app.core.process import (
    PropertyProcess
)


class PropertyHandler:
    @staticmethod
    def get_property(
        state: str,
        year: str,
        city: str
    ):
    
        obj = PropertyProcess()
        return obj.get_property(state,year,city)


