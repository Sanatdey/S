
import re
class Lexer(object):
	def __init__(self, code):
		self.code = code
	def tokenize(self):
		tokens = []
		code = self.code.split()
		code_len = 0
		while code_len < len(code):
			word = code[code_len]			
			if word == "var":
				tokens.append(["VARIABLE", word])
			elif re.match('[a-z]', word) or re.match('[A-Z]', word) and word != 'var' and word !='showme':
				if word[-1] == '.':
					tokens.append(["IDENTIFIRE", word[0:len(word)-1]])
				else:
					tokens.append(["IDENTIFIRE", word])
			elif re.match('[0-9]',word):
				if word[-1]=='.':
					tokens.append(["INTEGER", word[0:len(word)-1]])
				else:
					tokens.append(["INTEGER", word])
			elif word in "+-*/%=@":
				tokens.append(["OPARETOR", word])
			elif word == ",":
				tokens.append(["COMMA", word])
			elif '"' in word:
				if word[-1] == '.':
					tokens.append(["STRING", word[1:len(word)-2]])
				else:
					tokens.append(["STRING", word[1:len(word)-1]])
			if word == '.':
				tokens.append(["STATEMENT_END", word])
			elif word[-1] == '.':
				tokens.append(["STATEMENT_END", word[-1]])
			elif word in "()[]":
				tokens.append(["BRACKET",word])
			elif word == "~":
				tokens.append(["INOUT",word])
			code_len = code_len+1
		tokens.append(["EMPTY",0])
		return tokens