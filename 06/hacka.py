#!/usr/bin/python3

import sys,os
import hackass.parser as parser
import hackass.code as code
import hackass.symbol as symbol


class Assembler(object):
	"""assembler logic implementation as per hack spec"""
	def __init__(self):
		self.sym = symbol.Symbol()
		self.next_address = 16


	def pass_1(self, infile):
		'''builds symbol table associating label with ROM address'''
		p = parser.Parser(infile)		
		cmd_line = 0
		while p.has_more_command():			
			p.advance()
			command = p.command_type()
			if command == 'A_CMD' or command == 'C_CMD':
				cmd_line += 1
			else:
				symbol = p.symbol_l()
				self.sym.add_entry(symbol, cmd_line)


	def pass_2(self, file, outfile):
		'''builds the binary equivalent of each command'''
		p = parser.Parser(file)
		c = code.Code()
		out = open(outfile, 'w')

		while p.has_more_command():
			p.advance()
			command = p.command_type()
			if command == 'A_CMD':
				temp_sym = p.symbol_a()
				if temp_sym.isdigit():					
					token = temp_sym
				else:
					if self.sym.contains(temp_sym):
						token = self.sym.get_address(temp_sym)
					else:
						self.sym.add_entry(temp_sym, self.next_address)
						token = self.next_address
						self.next_address += 1
				out.write(c.generate_a(token) + '\n')

			elif command == 'C_CMD':
				out.write(c.generate_c(p.dest().strip(), p.comp().strip(), 
													p.jump().strip()) + '\n')

			else:
				pass
		out.close()


	def assemble(self, infile):
		'''drives the assembly process'''
		self.pass_1(infile)		
		self.pass_2(infile, self.outfile_name(infile))


	def outfile_name(self, infile):
		'''output file name generation'''
		if infile.endswith(".asm"):
			outfile = infile.replace(".asm", ".hack")
		else:
			outfile = infile + ".hack"

		return outfile




def main():
	# create instance of assembler
	a = Assembler()

	# start conversion
	a.assemble(infile)


if __name__ == "__main__":
	# check if exactly one argument is given
	if len(sys.argv) != 2:
		print("Usage: python hackass.py inputfile.asm")
	else:
		infile = sys.argv[1]

	# verify if input file exist
	if not os.path.isfile(infile):
		print("error: {} does not exist".format(infile))
		sys.exit(1)
	
	main()