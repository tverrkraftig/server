from flask import Response
from functools import wraps
from helpers import unicode_to_str

def get_str_object_or_404(action):
    @wraps(action)
    def wrapper(*args, **kwargs):
        result = action(*args, **kwargs)
		if not result:
            return Response(response = {}, status = 404, mimetype = "application/json")
        else:
            return Response(response = unicode_to_str(result), mimetype = "application/json")
    return wrapper

def verify_signature(request):
	def real_wrapper(action):
		@wraps(action)
		def wrapper(*args, **kwargs):
			userAllowed 
			if not userAllowed:
				# request should be denied
				# raise exception
				pass
			else:
				return Response(response = unicode_to_str(result), mimetype = "application/json")
		return wrapper
	return real_wrapper
