import lexer_rules
import parser_rules
from ply.lex import lex
from ply.yacc import yacc

text = "7 + (14 + 6) * 2 + 5"
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
parser = yacc(module=parser_rules)
ast = parser.parse(text, lexer)
print(ast)
