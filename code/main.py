import par
import lexer


def main():

	content = ""

	with open('test.lang', 'r') as file:
		content = file.read()
	lex = lexer.Lexer(content)
	tokens = lex.tokenize()
	parse = par.Par(tokens)
	obj = parse.parse()


main()
