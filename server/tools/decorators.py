from flask import Response
from functools import wraps
from helpers import unicode_to_str
from crypto import Signature
# gotta import the pycrypto stuff

mongodb = MongoClient().db

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
# putt koden din her Odd
			# get the JSON as a dictionary
        	data = request.get_json(force=True, cache=False)
			userID = data["userID"]
			signature = data["signature"]
			json = data["body"]
			# some function that gets the public key associated with this ID
			user = users.find_one({'user_id': userID})
			key = user["public_key"]
			h = SHA.new(json)
			verifier = PKCS1_PSS.new(key)
			userAllowed = verifier.verify(h, signature)
			if not userAllowed:
				# request should be denied
				# raise exception
				pass
			else:
				# I think this should return the body or whatever instead but idk
				return action(*args, **kwargs)
		return wrapper
	return real_wrapper
