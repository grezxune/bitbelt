from functools import wraps
from flask import request, abort

def require_json(func):
    @wraps(func)
    def contains_json_data(*args, **kwargs):
        if(request.method == 'GET' or
          (request is not None and
           request.json is not None)):
            print('in decorator success')
            return func(*args, **kwargs)
        else:
            print('400 from decorator')
            abort(400)

    return contains_json_data
