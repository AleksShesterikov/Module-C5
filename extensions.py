import requests
import json
from config import PAYLOAD, keys


class APIException(Exception):
    pass


class CryptoConvector:
    @staticmethod
    def get_price(base: str, quote: str, amount:str):

        if base not in keys:
            raise APIException(f'Ой. ошибочка, проверьте валюту {base}')
        else:
            base_tiker = base

        if quote not in keys:
            raise APIException(f'Ой. ошибочка, проверьте валюту {quote}')
        else:
            quote_tiker = quote

        if quote_tiker == base_tiker:
            raise APIException(f'Невозможно перевести одинаковые валюты')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Ой. ошибочка, проверьте количество валюты')

        r = requests.get('http://api.exchangeratesapi.io/v1/latest', params=PAYLOAD)

        if base_tiker != 'EUR':
            base_price = json.loads(r.content)['rates'][base_tiker]

        else:
            base_price = 1

        if quote_tiker != 'EUR':
            quote_price = json.loads(r.content)['rates'][quote_tiker]
        else:
            quote_price = 1
        try:
            total = (quote_price / base_price) * amount
        except ZeroDivisionError as e:
            raise APIException('Что-то сломалось. Попробуем еще раз?')
        return total



