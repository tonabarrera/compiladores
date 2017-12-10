from lexer_rules import tokens
from arbol import Nodo


# La primera linea comentada realiza la operacion correspondiente
# La segunda linea utiliza un arbol mediante una lista
def p_expression_suma(p):
    """expression : expression SUMA term"""
    # p[0] = p[1] + p[3]
    # p[0] = ('+', p[1], p[3])
    p[0] = Nodo('SUMA', [p[1], p[3]], p[2])


def p_expression_term(p):
    """expression : term"""
    # p[0] = p[1]
    # p[0] = (p[1])
    p[0] = Nodo('TERM', [p[1]])


def p_term_producto(p):
    """term : term PRODUCTO factor"""
    # p[0] = p[1] * p[3]
    # p[0] = ('*', p[1], p[3])
    p[0] = Nodo('PRODUCTO', [p[1], p[3]], p[2])


def p_term_factor(p):
    """term : factor"""
    # p[0] = p[1]
    # p[0] = (p[1])
    p[0] = Nodo('FACTOR', [p[1]])


def p_factor_numero(p):
    """factor : NUMERO"""
    # p[0] = p[1]
    # p[0] = ('NUMERO', p[1])
    p[0] = Nodo('NUMERO', None, p[1])


def p_factor_expresion(p):
    """factor : IZQPARENTESIS expression DERPARENTESIS"""
    # p[0] = p[2]
    # p[0] = (p[2])
    p[0] = Nodo('EXPRESION', [p[2]])


def p_error(p):
    raise Exception("Syntax error.")
