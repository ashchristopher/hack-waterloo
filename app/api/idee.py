from api import Api

class PixMatch(Api):
	
	api_url = "http://pixmatch-r.hackdays.tineye.com/rest/"
	
	def process(self, data):
		local_context = {}

		# post url to pixmatch

		return local_context