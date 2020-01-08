import parser
import lexer


def main():

	# Variable to store the contents of the file
	content = ""


	with open('test.lang', 'r') as file:
		# reading and storing the contents of the file
		content = file.read()

	############################
    #         Lexer           #
    ############################

	# Calling the lexer file Lexer class and initializing it with the source code in lex
	lex = lexer.Lexer(content)
	# Calling the tokenize method from inside the lexer instance
	tokens = lex.tokenize()

	############################
    #         Parser           #
    ############################

	# Calling the parser file Parser class and initializing it with the source code
	parse = parser.Par(tokens)
	# Calling the parse method from inside the parse instance
	parse.parse()


main()
