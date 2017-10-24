tokens = [
    'IZQPARENTESIS',
    'DERPARENTESIS',
    'COMA',
    'PUNTOCOMA',
    'IDENTIFICADOR',
    'NUMERO',
]
palabras_reservadas = {
    'if': 'IF',
    'while': 'WHILE',
    'var': 'VAR',
    'asig': 'ASIG',
    'sumar': 'SUMAR',
    'mayorque': 'MAYOR_QUE',
    'restar': 'RESTAR',
    'menorque': 'MENOR_QUE',
    'eof': 'EOF',
}
tokens += list(palabras_reservadas.values())

t_IZQPARENTESIS = r'\('
t_DERPARENTESIS = r'\)'
t_COMA = r','
t_PUNTOCOMA = r';'


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabras_reservadas.get(t.value, 'IDENTIFICADOR')  # Check for reserved words
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("ERROR '%s'" % t.value[0])
    t.lexer.skip(1)
