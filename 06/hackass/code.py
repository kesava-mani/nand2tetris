#!/usr/bin/python3


class Code(object):
	"""convert commands to their respective binary code"""

	#default codes of dest, comp and jump tokens
	dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
	
	comp_codes = {
				"0"    :  "0101010",
				"1"    :  "0111111",
				"-1"   :  "0111010",
				"D"    :  "0001100",
				"A"    :  "0110000",
				"!D"   :  "0001101",
				"!A"   :  "0110001",
				"-D"   :  "0001111",
				"-A"   :  "0110011",
				"D+1"  :  "0011111",
				"A+1"  :  "0110111",
				"D-1"  :  "0001110",
				"A-1"  :  "0110010",
				"D+A"  :  "0000010",
				"D-A"  :  "0010011",
				"A-D"  :  "0000111",
				"D&A"  :  "0000000",
				"D|A"  :  "0010101",
				"M"    :  "1110000",
				"!M"   :  "1110001",
				"-M"   :  "1110011",
				"M+1"  :  "1110111",
				"M-1"  :  "1110010",
				"D+M"  :  "1000010",
				"D-M"  :  "1010011",
				"M-D"  :  "1000111",
				"D&M"  :  "1000000",
				"D|M"  :  "1010101"
				}

	jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

	
	def __init__(self):
		"""constructor of Code class"""
		pass

	def binary(self, num):
		"""convert input to binary with '0b' sliced off"""
		return bin(int(num))[2:]	
	

	def dest(self, token):
		"""compute binary equivalent of input dest token"""
		return self.binary(self.dest_codes.index(token)).zfill(3)


	def comp(self, token):
		"""compute binary equivalent of input comp token"""
		return self.comp_codes.get(token)


	def jump(self, token):
		"""compute binary equivalent of input jump token"""
		return self.binary(self.jump_codes.index(token)).zfill(3)


	def generate_c(self, dest, comp, jump):
		"""concatenate all tokens into binary C_COMMAND"""
		return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)


	def generate_a(self, address):
		"""concatenate  address token into binary A_COMMAND"""
		return '0' + self.binary(address).zfill(15)
		
