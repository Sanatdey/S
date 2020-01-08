import mymath
class Par(object):
	def __init__(self,tokens):
		self.tokens=tokens
	def parse(self):
		self.count = 0
		while self.count < len(self.tokens):
			tokens_type = self.tokens[self.count][0]
			tokens_value = self.tokens[self.count][1]
			#print(tokens_type , tokens_value)
			if tokens_type == 'VARIABLE' and tokens_value == 'var':
				self.par_var_dec(self.tokens[self.count:len(self.tokens)])
				ask = (mymath.assignmentOpp(self.tokens[self.count:len(self.tokens)]))
			elif tokens_type == 'IDENTIFIRE' and tokens_value == 'showme':
				self.showme(self.tokens[self.count:len(self.tokens)],ask)
			elif tokens_type == 'INOUT' and tokens_value == '~':
				mymath.math(self.tokens[self.count:len(self.tokens)],ask)
			
			self.count += 1
	def par_var_dec(self ,token_tip	):
		token_chk = 0
		for token in range(0,len(token_tip)+1):
			tokens_type = token_tip[token_chk][0]
			tokens_value = token_tip[token_chk][1]
			il=[]
			for i in range(1,len(token_tip)+1,4):
				il.append(i)
			ol=[]
			for j in range(2,len(token_tip)+1,4):
				ol.append(j)
			vl=[]
			for h in range(3,len(token_tip)+1,4):
				vl.append(h)
			cl=[]
			for k in range(4,len(token_tip)+1,4):
				cl.append(k)
			if tokens_type == 'STATEMENT_END':
				break
			
			elif token in il:
				if tokens_type == "IDENTIFIRE":
					identifire = tokens_value
				else :
					print("Syntax ERROR : you must give a variable name after variable decliaration")		
					break
			elif token in ol:#2 or token == 4 or token == 6 or token == 8:
				if tokens_type == "OPARETOR":
					tok =1
					
				else :
					print("Syntax ERROR :you miss the assignment operator after VARIABLE name")
					break
			elif token in vl:#== 3 or token == 5 or token == 7 or token == 9:
				if tokens_type == 'STRING':
					strg = tokens_value
				elif tokens_type == 'INTEGER':
					initalization =1
				else :
					print("Syntax ERROR : IT CAN BE A INTEGER, STRING OR IDEMTIFIRE I.E. variable")
					break
			
			elif token in cl:
				if tokens_type == 'COMMA':
					comma = tokens_value
				elif tokens_type == "STATEMENT_END":
					break
				else :
					print("Syntax ERROR : in this position you can used comma for multiple decliaration or u can used assignment operator for initalization")
					break
			token_chk = token_chk + 1 
			
		
			
			
	def showme(self,token_tip,toko):
	
		if token_tip[1][0] == "INOUT" :
			if token_tip[2][0] == "STRING":
				print(token_tip[2][1])
			elif token_tip[3][0]=="EMPTY":
				print("Statement MISSING : you have to give '.' for debag")
			
		else:
			print("Syntax ERROR : you have to type string within parentisis or you have to give output operator")
			
		token_chk = 1
		for i in range(0 ,len(toko)):
			tokens_id=toko[i][0]
			tokens_val=toko[i][1]
			if token_tip[1][0] == "INOUT" and token_tip[2][1] == tokens_id and token_tip[3][0] == 'STATEMENT_END':
					print(tokens_val)
			

		

	
