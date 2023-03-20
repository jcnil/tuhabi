import json

from .models import (
    PropertyModel
)


class Queryset:

    @staticmethod
    def get_property_by_params() -> str:
        """
        Return a property based in .
        :param state: str, year: int,city: str
        :return: PropertyModel
        """

        return """
        SELECT p.id,
        p.address,
        p.city,
        p.price,
        p.description,
        `year`,
        sh.status_id 
                   FROM property p 
                   INNER JOIN status_history sh 
                   ON p.id=sh.property_id 
                         WHERE p.year= %i AND
                               p.city= %s AND
                               sh.status_id in (3,4,5);
        """
