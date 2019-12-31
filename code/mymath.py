def math(token_tip,toko):
	
		if token_tip[0][0] == 'INOUT' and token_tip[1][0] == 'IDENTIFIRE' and token_tip[2][1] == "=" and  token_tip[3][1] == toko[0][0] and token_tip[5][1] == toko[1][0] and token_tip[6][0] == "STATEMENT_END" :
						
				if token_tip[4][1] == "+":
					toko[2][1] = int(toko[0][1]) + int(toko[1][1])
					toko[-1][0]	= " "		

				elif token_tip[4][1] == "-":
					toko[2][1] = int(toko[0][1]) - int(toko[1][1])
					toko[-1][0]	= " "	
					
				elif token_tip[4][1] == "*":
					toko[2][1] = int(toko[0][1]) * int(toko[1][1])
					toko[-1][0]	= " "
					
				elif token_tip[4][1] == "%":
					toko[2][1] = int(toko[0][1]) % int(toko[1][1])
					toko[-1][0]	= " "
					
				elif token_tip[4][1] == "@":
					toko[2][1] = int(toko[0][1]) // int(toko[1][1])
					toko[-1][0]	= " "
				
				elif token_tip[4][1] == "/":
					toko[2][1] = int(toko[0][1]) / int(toko[1][1])
					toko[-1][0]	= " "

				else :
					print("Syntex ERROR : you miss the operator or you have wrong syntax [Ex. ~ num1 = a + b .] or Statement MISSING : you miss the Statement end notation '.'")
		#else:		#	else:
		#				print("Syntex ERROR :")		print(" ")

		return (toko)
def assignmentOpp(token_tip):
		toko = []
		token_chk = 1
		for i in range(0 ,len(toko)):
			tokens_id=toko[i][0]
			tokens_val=toko[i][1]
		for token in range(0,len(token_tip)):
			if token_tip[token][1]== '=':
				#token_tip[token-1][1] = token_tip[token+1][1]
				toko.append([token_tip[token-1][1],token_tip[token +1][1]])
		return (toko)
	
