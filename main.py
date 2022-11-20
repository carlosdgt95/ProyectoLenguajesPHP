#import sintactico
import ply.yacc as yacc
from lexicophp import tokens

#def p_cuerpo(p):
# '''cuerpo: salida
#  | variable'''


def p_salida_forma1(p):
  "salida : ECHO STRING PUNTO_COMA"


def p_salida_forma2(p):
  "salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA"


def p_salida_forma3(p):
  "salida : PRINT STRING PUNTO_COMA"


def p_variable_ps(p):
  "variable : ASIGNACION ID IGUAL STRING PUNTO_COMA"


def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


parser = yacc.yacc()


def validaRegla(s):
  result = parser.parse(s)
  print(result)


while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
'''Ejemplos que por ahora puede validar
a=20
variable=30.2
imprimir(var)
imprimir(20.3)
'''
'''
Para practicar implemente las siguientes reglas:
a=30+23
var=20-310*292/23
cond=20>variable
if var>10: imprimir(True)
'''
