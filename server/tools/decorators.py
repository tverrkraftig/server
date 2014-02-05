from functools import wraps
from helpers import unicode_to_str

def get_str_object_or_404(action):
    @wraps(action)
    def wrapper(*args, **kwargs):
        result = action(*args, **kwargs)
        if not result:
            return {}, 404
        else:
            return unicode_to_str(result)
    return wrapper
