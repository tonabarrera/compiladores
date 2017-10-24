from _ast import Add

from prueba.lexer_rules import tokens

def p_expression_suma(subexpr):
    'expression : expression SUMA term'
    subexpr[0] = subexpr[1] + subexpr[3]

def p_expression_term(subexpr):
    'expression : term'
    subexpr[0] = subexpr[1]

def p_term_producto(subexpr):
    'term : term PRODUCTO factor'
    subexpr[0] = subexpr[1] * subexpr[3]


def p_term_factor(subexpr):
    'term : factor'
    subexpr[0] = subexpr[1]

def p_factor_numero(subexpr):
    'factor : NUMERO'
    subexpr[0] = subexpr[1]

def p_factor_expresion(subexpr):
    'factor : IZQPARENTESIS expression DERPARENTESIS'
    subexpr[0] = subexpr[2]

def p_error(subexpr):
    raise Exception("Syntax error.")