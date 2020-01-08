# using the regular expression library
import re

# Lexer class to generate and return tokens
class Lexer(object):

	# Initalizing source code to the Lexer
	def __init__(self, code):
		self.code = code
	
	# Method used to create tokens
	def tokenize(self):

		# list to store all tokens created by the lexer
		tokens = []

		# Creating a list of words from the source code
		code = self.code.split()

		# Index of the word we are present
		code_index = 0
		
		# Looping throug each word in the source code to generate tokens
		while code_index < len(code):
			
			# Taking each word at a time and generating tokens with it
			word = code[code_index]			
			
			# Creating variable declaration token
			if word == "var":
				tokens.append(["VARIABLE", word])
			
			# Creating identifier tokens	
			elif re.match('[a-z]', word) or re.match('[A-Z]', word) and word != 'var' and word !='showme':
				if word[-1] == '.':
					tokens.append(["IDENTIFIER", word[0:len(word)-1]])
				else:
					tokens.append(["IDENTIFIER", word])
			
			# Creating Integer token 	
			elif re.match('[0-9]',word):
				if word[-1]=='.':
					tokens.append(["INTEGER", word[0:len(word)-1]])
				else:
					tokens.append(["INTEGER", word])
			
			# Creating Operator token	
			elif word in "+-*/%=@":
				tokens.append(["OPERATOR", word])
			
			# Token for comma
			elif word == ",":
				tokens.append(["COMMA", word])
			
			# Token for String
			elif '"' in word:
				if word[-1] == '.':
					tokens.append(["STRING", word[1:len(word)-2]])
				else:
					tokens.append(["STRING", word[1:len(word)-1]])
			
			# Statement End token
			if word == '.':
				tokens.append(["STATEMENT_END", word])
			elif word[-1] == '.':
				tokens.append(["STATEMENT_END", word[-1]])
			
			# Parenthesis token
			elif word in "()[]":
				tokens.append(["BRACKET",word])
			
			# Inout token 
			elif word == "~":
				tokens.append(["INOUT",word])
			
			# Increamenting token index for next word
			code_index = code_index+1
		
		tokens.append(["EMPTY",0])
		
		# Finally returning the tokens generated.
		return tokens