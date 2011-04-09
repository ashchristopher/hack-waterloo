import datetime
from decimal import Decimal
import json

class JSONEncoder(json.JSONEncoder):
    '''
    Extended JSON Encoder which can handle more than primative types
    such as dates and Decimals.
    '''
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)

def encode_json(data):
    return JSONEncoder().encode(data)

