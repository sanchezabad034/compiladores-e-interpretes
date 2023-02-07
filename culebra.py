"""Integrantes: Solis Valdivia Danna Vanessa, Salazar Escobedo Cristopher Adan, De la hoya Quiñones Sherlyn
    y Rodriguez Sanchez Jose Abad  8 - A . 
"""
import ply.lex as lex 
tokens = (
    'NUM_IMAGINARIO',
    'IGUAL',
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION', 
)
reserved = {
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'CLASS': 'CLASS',
    'FOR': 'FOR',
    'BOOLEAN': 'BOOLEAN',
    'FLOAT': 'FLOAT',
    'INT': 'INT',
    'STRING': 'STRING',
    'CHAR': 'CHAR',
    'FUCTION': 'FUCTION',
    'VOID': 'VOID',
    'BREAK': 'BREAK',
    'CONTINUE': 'CONTINUE',
    'GET': 'GET',
    'SETTER': 'SETTER',
    'PRINT': 'PRINT',
    'MAIN': 'MAIN'
    
}

token = list(tokens) + list(reserved.values())

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = '/'
t_IGUAL = r'='
t_NUM_IMAGINARIO = r'/d+[a-z]+'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PALABRA(t):
    r'\w+'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print('Token desconocido: ''%s' % t.value)
    t.lexer.skip(1)

t_ignore = r' \t\n'

lexer = lex.lex()
with(open('data.txt','r')) as file:
    data = file.read()
    lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok: 
        break
    print(tok)