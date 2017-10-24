from prueba import lexer_rules, parser_rules
from prueba.ply.lex import lex
from prueba.ply.yacc import yacc

text = "(14 + 6) * 2"
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
parser = yacc(module=parser_rules)
ast = parser.parse(text, lexer)
print(ast)