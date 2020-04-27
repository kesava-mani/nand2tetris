#!/usr/bin/python3


class Symbol(object):
	"""symbol organization and address generation"""
	def __init__(self):
		self.sym_table = {
						    "SP": 0,
						    "LCL": 1,
						    "ARG": 2,
						    "THIS": 3,
						    "THAT": 4,
						    "SCREEN": 16384,
						    "KBD": 24576,
						 }
		for x in xrange(0,16):			
			temp_sym = 'R' + str(x)
			self.sym_table.update({temp_sym:x})


	def add_entry(self, symbol, address):
		'''Adds input symbol and its address to symbol table'''
		self.sym_table.update({symbol:address})


	def contains(self, symbol):
		'''Checks if input symbol is in symbol table'''
		return symbol in self.sym_table.keys()
	

	def get_address(self,symbol):
		'''Gets the address of input symbol'''
		return self.sym_table.get(symbol)
