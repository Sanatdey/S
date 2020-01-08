# Defination for mathematical operation
def math(token_ip_stream,toko):
	
		if token_ip_stream[0][0] == 'INOUT' and token_ip_stream[1][0] == 'IDENTIFIRE' and token_ip_stream[2][1] == "=" and  token_ip_stream[3][1] == toko[0][0] and token_ip_stream[5][1] == toko[1][0] and token_ip_stream[6][0] == "STATEMENT_END" :
						
				if token_ip_stream[4][1] == "+":
					toko[2][1] = int(toko[0][1]) + int(toko[1][1])
					toko[-1][0]	= " "		

				elif token_ip_stream[4][1] == "-":
					toko[2][1] = int(toko[0][1]) - int(toko[1][1])
					toko[-1][0]	= " "	
					
				elif token_ip_stream[4][1] == "*":
					toko[2][1] = int(toko[0][1]) * int(toko[1][1])
					toko[-1][0]	= " "
					
				elif token_ip_stream[4][1] == "%":
					toko[2][1] = int(toko[0][1]) % int(toko[1][1])
					toko[-1][0]	= " "
					
				elif token_ip_stream[4][1] == "@":
					toko[2][1] = int(toko[0][1]) // int(toko[1][1])
					toko[-1][0]	= " "
				
				elif token_ip_stream[4][1] == "/":
					toko[2][1] = int(toko[0][1]) / int(toko[1][1])
					toko[-1][0]	= " "

				else :
					print("Syntax ERROR : you miss the operator or you have wrong syntax [Ex. ~ num1 = a + b .] or Statement MISSING : You miss the Statement end notation '.'")

		return (toko)

# Defination for assignment operation
def assignmentOpp(token_ip_stream):
		toko = []
		token_chk = 1
		for i in range(0 ,len(toko)):
			tokens_id=toko[i][0]
			tokens_val=toko[i][1]
		for token in range(0,len(token_ip_stream)):
			if token_ip_stream[token][1]== '=':
				toko.append([token_ip_stream[token-1][1],token_ip_stream[token +1][1]])
		return (toko)
	
