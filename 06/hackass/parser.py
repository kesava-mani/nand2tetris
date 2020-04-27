#!/usr/bin/python3


import os

class Parser(object):
	"""parses the input file as per hack assembly spec"""

	def __init__(self, infile):
		self.asm = []
		self.command = ''
		self.line_number = 0

		
		# open the file input and temporary output file 
		with open(infile, 'r') as f_in, open(".temp.txt", 'a') as f_out :
			for line in f_in:
				#strip whitespaces and // comments
				line = line.split("//")[0].replace(' ', '').strip()
				f_out.write("{}\n".format(line))

		# convert temp file contents into list of lines 
		with open(".temp.txt", 'r') as f_out:
			temp_asm = f_out.readlines()
			for line in temp_asm:
				if line != '\n':
					self.asm.append(line)


	def has_more_command(self):
		'''checks if there is more lines are there to process'''
		return not self.line_number == len(self.asm)


	def advance(self):
		'''proceed to next command. Initially 0th command'''
		if self.has_more_command():
			self.command = self.asm[self.line_number]
			self.line_number += 1			


	def command_type(self):
		"""returns the type of input command""" 
		if self.command[0] == '@':
			cmd_type = 'A_CMD'
		elif self.command[0] == '(':
			cmd_type = 'L_CMD'
		else:
			cmd_type = 'C_CMD'
		
		return cmd_type


	def symbol_a(self):
		'''returns symbol of A COMMAND'''
		sym = self.command[1:-1]

		return sym


	def symbol_l(self):
		'''returns symbol of L PSEUDO COMMAND'''
		sym = self.command[1:-2]

		return sym


	def dest(self):
		'''retuns stripped destination part of C COMMAND as string'''
		if '=' in self.command:
			sym = self.command.split('=')[0]
		else:
			sym = ''			
		
		return sym


	def comp(self):
		'''retuns stripped computation part of C COMMAND as string'''
		if '=' in self.command:
			temp_sym = self.command.split('=')[1]
			sym = temp_sym.split(";")[0]
		else:
			sym = self.command.split(';')[0]			

		return sym


	def jump(self):
		'''retuns stripped jump part of C COMMAND as string'''
		if self.command.find(';') != -1:
			sym = self.command.split(';')[1]
		else:
			sym = ''

		return sym


	def __del__(self):
		if os.path.isfile('.temp.txt'):
			os.remove('.temp.txt')
