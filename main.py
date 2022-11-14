import ply.lex as lex

# Lista de palabras reservadas
#Elaborado por Carlos Gómez
reserved = {
    "break": "BREAK",
    "clone": "CLONE",
    "endswitch": "ENDSWITCH",
    "final": "FINAL",
    "function": "FUNCTION",
    "include": "INCLUDE",

    #"or": "OR",
    "requiere": "REQUIERE",
    "throw": "THROW",
    "var": "VAR",
    "abstract": "ABSTRACT",
    "callable": "CALLABLE",
    "const": "CONST",
    "do": "DO",
    "endddeclare": "ENDDECLARE",
    "endwhile": "ENDWHILE",
    "finally": "FINALLY",
    "global": "GLOBAL",
    "print": "PRINT",
    "trait": "TRAIT",
    "while": "WHILE",
    #"and":"AND",
    "case": "CASE",
    "continue": "CONTINUE",
    "echo": "ECHO",
    "fn": "FN",
    "instanceof": "INTANCEOF",
    "match": "MACHT",
    "private": "PRIVATE",
    "return": "RETURN",
    "try": "TRY",
    "xor": "XOR",
    "cath": "CATH",
    "declare": "DECLARE",
    "else": "ELSE",
    "for": "FOR",
    "if": "IF",
    "for": "FOR",
    "inteadof": "INTEADOF",
    "namespace": "NAMESPACE",
    "protected": "PROTECTED",
    "static": "STATIC",
    "as": "AS",
    "class": "CLASS",
    "default": "DEFAULT",
    "elseif": "ELSEIF",
    "endif": "ENDIF",
    "extends": "EXTENDS",
    "foreach": "FOREACH",
    "implements": "IMPLEMENTS",
    "interface": "INTERFACE",
    "new": "NEW",
    "public": "PUBLIC",
    "switch": "SWITCH",
    "use": "USE",
}
#Elaborado Carlos Gomez
#Definicion de tokens
tokens = (
    'ENTERO',
    'FLOTANTE',
    ### Karla Castro
    'BOOLEANO',
    'COMENTARIO',
    'STRING',
    'VARIABLE',
    'SIGNO_DOLAR',
    'SALTO_LINEA',
    'TABULACION',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'CORCH_IZQ',
    'CORCH_DER',
    'PAREN_IZQ',
    'PAREN_DER',
    'ASIGNACION',
    'ASIG_CONCA',
    'ASIG_REFER',
    'IGUAL',
    'IDENTICO',
    'DIFERENTE',
    'SUMA',
    'RESTA',
    'MULTIPL',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    'INCREMENTO',
    'DECREMENTO',
    'MAYOR_QUE',
    'MAYOR_IGUAL',
    'MENOR_QUE',
    'MENOR_IGUAL',
    'AND',
    'OR',
    'PUNTO',
    'PUNTO_COMA',
    'INTERROG_CE',
    'CADENA',
    'ID'

    ###
) + tuple(reserved.values())
#Emily Cordero
# Regular expression rules for simple tokens
#t_SIGNO_DOLAR  = r'\$'

t_SALTO_LINEA = r'\n'
t_TABULACION = r'\t'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCH_IZQ = r'\['
t_CORCH_DER = r'\]'
t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'
t_ASIGNACION = r'\$'
t_ASIG_CONCA = r'.='
#t_ASIG_REFER = r'=&$'
t_IGUAL = r'='
t_IDENTICO = r'=='
t_DIFERENTE = r'!='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPL = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\*{2}'
t_MODULO = r'\%'
t_INCREMENTO = r'\+{2}'
t_DECREMENTO = r'\-{2}'
t_MAYOR_QUE = r'>'
t_MAYOR_IGUAL = r'>='
t_MENOR_QUE = r'<'
t_MENOR_IGUAL = r'<='
t_AND = r'\&{2}'
t_OR = r'\|{2}'
t_PUNTO = r'\.'
t_PUNTO_COMA = r';'
t_INTERROG_CE = r'\?'
def t_ENTERO(t):
    r'(-?[1-9]\d*)|0'
    t.value = int(t.value)
    return t

def t_FLOTANTE(t):
    r'(-?[1-9]\d*\.\d+)|0.0'
    t.value = float(t.value)
    return t

def t_ID(t):

    r'[A-z_]\w*'
    t.type = reserved.get(t.value, 'ID')

    return t


def t_error(t):

    print("No es reconocido '%s'" %t.value[0])
    t.lexer.skip(1)


def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_COMENT(t):
  
    r'//.*'
    
   
    pass
def t_COMENT2(t):
  
    r'\#.*'
    
   
    pass

t_ignore = ' \t'

#Construya el lexer
lexer = lex.lex()

###  Lea el archivo algoritmos.txt y retorne los tokens


# Método para analizar cada línea
def analizar(data):
  lexer.input(data)
  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok)


# Leer archivos
archivo = open("algoritmos.txt")
for linea in archivo:
  print(">>" + linea)
  analizar(linea)
  if len(linea) == 0:
    break
