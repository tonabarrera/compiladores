tokens = [
    'p',
    'q',
    'c',
    'z',
    'a',
    'n',
]
palabras_reservadas = {
    'if': 'i',
    'while': 'l',
    'var': 'v',
    'asig': 'b',
    'sumar': 'o',
    'mayorque': 'm',
    'restar': 'o',
    'menorque': 'm',
    'eof': 'f',
}
tokens += list(palabras_reservadas.values())

# Parentesis izq
t_p = r'\('
# Parentesis der
t_q = r'\)'
# Coma
t_c = r','
# Punto y coma
t_z = r';'


# ID
def t_a(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Check for reserved words
    t.type = palabras_reservadas.get(t.value, 'a')
    return t


# Numero
def t_n(t):
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
