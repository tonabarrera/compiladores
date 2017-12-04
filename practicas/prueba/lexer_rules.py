tokens = [
    'NUMERO',
    'SUMA',
    'PRODUCTO',
    'IZQPARENTESIS',
    'DERPARENTESIS',
]

t_SUMA = r"\+"
t_PRODUCTO = r"\*"
t_IZQPARENTESIS = r"\("
t_DERPARENTESIS = r"\)"


def t_NUMERO(token):
    r"[1-9][0-9]*"
    token.value = int(token.value)
    return token

t_ignore = " \t"


def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)


def t_error(token):
    message = "Token desconocido:"
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
