class search_options():
	max_results=1;
	q='Agriculture'
	def __init__(self,query):
		self.q=query;
	def display(self):
		print self.q;