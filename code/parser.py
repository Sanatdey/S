
import mymath

class Par(object):

	def __init__(self,tokens):
		self.tokens=tokens

	# Method to parse the entire set of tokens
	def parse(self):
		
		# To store the tokens index
		self.token_index = 0
		
		while self.token_index < len(self.tokens):
			
			# Variables to store token type and value
			tokens_type = self.tokens[self.token_index][0]
			tokens_value = self.tokens[self.token_index][1]
			
			if tokens_type == 'VARIABLE' and tokens_value == 'var':
				self.par_var_dec(self.tokens[self.token_index:len(self.tokens)])
				ask = (mymath.assignmentOpp(self.tokens[self.token_index:len(self.tokens)]))
			elif tokens_type == 'IDENTIFIER' and tokens_value == 'showme':
				self.showme(self.tokens[self.token_index:len(self.tokens)],ask)
			elif tokens_type == 'INOUT' and tokens_value == '~':
				mymath.math(self.tokens[self.token_index:len(self.tokens)],ask)
			
			self.token_index += 1

	# Method to parse variable declaration statement
	def par_var_dec(self ,token_ip_stream	):
		token_chk = 0
		for token in range(0,len(token_ip_stream)+1):
			tokens_type = token_ip_stream[token_chk][0]
			tokens_value = token_ip_stream[token_chk][1]
			il=[]
			for i in range(1,len(token_ip_stream)+1,4):
				il.append(i)
			ol=[]
			for j in range(2,len(token_ip_stream)+1,4):
				ol.append(j)
			vl=[]
			for h in range(3,len(token_ip_stream)+1,4):
				vl.append(h)
			cl=[]
			for k in range(4,len(token_ip_stream)+1,4):
				cl.append(k)
			if tokens_type == 'STATEMENT_END':
				break
			
			elif token in il:
				if tokens_type == "IDENTIFIER":
					identifier = tokens_value
				else :
					print("Syntax ERROR : You must give a variable name after variable declaration")		
					break
			elif token in ol:#2 or token == 4 or token == 6 or token == 8:
				if tokens_type == "OPERATOR":
					tok =1
					
				else :
					print("Syntax ERROR : You miss the assignment operator after VARIABLE name")
					break
			elif token in vl:#== 3 or token == 5 or token == 7 or token == 9:
				if tokens_type == 'STRING':
					strg = tokens_value
				elif tokens_type == 'INTEGER':
					initalization =1
				else :
					print("Syntax ERROR : IT CAN BE A INTEGER, STRING OR IDENTIFIER I.E. variable")
					break
			
			elif token in cl:
				if tokens_type == 'COMMA':
					comma = tokens_value
				elif tokens_type == "STATEMENT_END":
					break
				else :
					print("Syntax ERROR : In this position you can used comma for multiple declaration or you can used assignment operator for initalization")
					break
			token_chk = token_chk + 1 
			
		
			
	# Method to parse Input output function
	def showme(self,token_ip_stream,toko):
	
		if token_ip_stream[1][0] == "INOUT" :
			if token_ip_stream[2][0] == "STRING":
				print(token_ip_stream[2][1])
			elif token_ip_stream[3][0]=="EMPTY":
				print("Statement End MISSING : you have to give '.' for debug")
			
		else:
			print("Syntax ERROR : You have to type string within parenthesis or you have to give output operator")
			
		token_chk = 1
		for i in range(0 ,len(toko)):
			tokens_id=toko[i][0]
			tokens_val=toko[i][1]
			if token_ip_stream[1][0] == "INOUT" and token_ip_stream[2][1] == tokens_id and token_ip_stream[3][0] == 'STATEMENT_END':
					print(tokens_val)
			

		

	
