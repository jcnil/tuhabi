
from app.core.exceptions import NotFoundException
from app.core.querysets import Queryset
from app.core.constants import OK

from config.settings import connect_db


class PropertyProcess:
    @staticmethod
    def get_property(
        state,
        year,
        city
    ) -> dict:
        """
        this function get some information about property
        :param request: state,year,city,status
        :return: response dictionary
        """

        conn = connect_db()

        cur = conn.cursor()

        rows = cur.execute(
            Queryset.get_property_by_params(),(year, city, )
        )

        result = [
            {
                'address': i[0],
                'city': i[1].upper(),
                'price': i[2],
                'description': i[3],
            }
            for i in rows
        ]

        if property is not None:
            return {
                "status": OK,
                "message": "Exist Property in Local Database",
                "data": result
            }
        raise NotFoundException
