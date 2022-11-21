import ply.lex as lex
#
# Lista de palabras reservadas
#Elaborado por Carlos Gómez
reserved = {
  "break": "BREAK",
  "clone": "CLONE",
  "endswitch": "ENDSWITCH",
  "final": "FINAL",
  "function": "FUNCTION",
  "include": "INCLUDE",
  "or": "OR",
  "requiere": "REQUIERE",
  "throw": "THROW",
  "var": "VAR",
  "abstract": "ABSTRACT",
  "callable": "CALLABLE",
  "const": "CONST",
  "endddeclare": "ENDDECLARE",
  "finally": "FINALLY",
  "global": "GLOBAL",
  "print": "PRINT",
  "trait": "TRAIT",
  "and":"AND",
  "continue": "CONTINUE",
  "echo": "ECHO",
  "fn": "FN",
  "instanceof": "INTANCEOF",
  "match": "MACHT",
  "private": "PRIVATE",
  "return": "RETURN",
  "try": "TRY",
  "cath": "CATH",
  "declare": "DECLARE",
  "inteadof": "INTEADOF",
  "namespace": "NAMESPACE",
  "protected": "PROTECTED",
  "static": "STATIC",
  "as": "AS",
  "class": "CLASS",
  "default": "DEFAULT",
  "extends": "EXTENDS",
  "implements": "IMPLEMENTS",
  "interface": "INTERFACE",
  "new": "NEW",
  "public": "PUBLIC",
  "use": "USE",
  "count": "COUNT",
  "strrev" : "STRREV",
  #Estructuras de Control
  "if": "IF",
  "elseif": "ELSEIF",
  "else": "ELSE",
  "endif": "ENDIF",
  "for": "FOR",
  "foreach": "FOREACH",
  "do": "DO",
  "while": "WHILE",
  "endwhile": "ENDWHILE",
  "switch": "SWITCH",
  "case": "CASE",
  #Estructuras de datos
  "array" : "ARRAY",
  "SplStack" : "STACK",
  "push" : "PUSH",
  "pop" : "POP",
  "current": "CURRENT",
  "SplQueue" : "QUEUE",
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
  'SIGNO_DOLAR',
  'SALTO_LINEA',
  'TABULACION',
  'LLAVE_IZQ',
  'LLAVE_DER',
  'CORCH_IZQ',
  'CORCH_DER',
  'PAREN_IZQ',
  'PAREN_DER',
  'ASIG_CONCA',
  'ASIG_REFER',
  'IGUAL',
  'IDENTICO',
  'DIFERENTE',
  'SUMA',
  'RESTA',
  'MULTIPL',
  'DIVISION',
  'DIVISION_ENT',
  'POTENCIA',
  'MODULO',
  'INCREMENTO',
  'DECREMENTO',
  'MAYOR_QUE',
  'MAYOR_IGUAL',
  'MENOR_QUE',
  'MENOR_IGUAL',
  'AND_SYMB',
  'OR_SYMB',
  'PUNTO',
  'PUNTO_COMA',
  'INTERROG_CE',
  'CADENA',
  'COMA'

  ###
) + tuple(reserved.values())
#Emily Cordero
# Regular expression rules for simple tokens

t_SIGNO_DOLAR  = r'\$'
t_SALTO_LINEA = r'\\n'
t_TABULACION = r'\\t'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCH_IZQ = r'\['
t_CORCH_DER = r'\]'
t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'
t_ASIG_CONCA = r'\.='
t_IGUAL = r'='
t_IDENTICO = r'=='
t_DIFERENTE = r'!='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPL = r'\*'
t_DIVISION = r'/'
t_DIVISION_ENT = r'//'
t_POTENCIA = r'\*{2}'
t_MODULO = r'\%'
t_INCREMENTO = r'\+{2}'
t_DECREMENTO = r'\-{2}'
t_MAYOR_QUE = r'>'
t_MAYOR_IGUAL = r'>='
t_MENOR_QUE = r'<'
t_MENOR_IGUAL = r'<='
t_AND_SYMB = r'\&{2}'
t_OR_SYMB = r'\|{2}'
t_PUNTO = r'\.'
t_PUNTO_COMA = r';'
t_INTERROG_CE = r'\?'
t_COMA = r'\,'


def t_ENTERO(t):
  r'(-?[1-9]\d*)|0'
  t.value = int(t.value)
  return t


def t_FLOTANTE(t):
  r'(-?\d*\.\d+)|^0.0$'
  t.value = float(t.value)
  return t


def t_BOOLEANO(t):
  r'(true|True|TRUE|false|False|FALSE)'
  t.type = reserved.get(t.value, "BOOLEANO")
  return t


def t_CADENA(t):
  r'([a-zA-Z0-9_]?[a-zA-Z0-9_]+)'
  t.type = reserved.get(t.value, 'CADENA')
  return t


def t_STRING(t):
  r'("[^"]*"|\`[^\']*\`)'
  t.type = reserved.get(t.value, "STRING")
  return t


def t_error(t):
  print("No es reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_COMENTARIO(t):
  r'\#.*'
  pass


t_ignore = ' \t'

#Construya el lexer
lexer = lex.lex()

###  Lea el archivo algoritmos.txt y retorne los tokens

'''
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
###############
'''
