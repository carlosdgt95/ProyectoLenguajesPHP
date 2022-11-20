#import sintactico
import ply.yacc as yacc
from lexicophp import tokens

#def p_cuerpo(p):
# '''cuerpo: salida
#  | variable'''

	
def p_sentencias(p):
  '''sentencias : valor
                  | estructuras_control 
                  | tipoFunciones '''
def p_estructuras_control(p):
	'''estructuras_control : SWITCH1
                          | cola'''
def p_funciones(p):
  '''tipoFunciones : sinRetorno'''

def p_sinretorno(p):
  '''sinRetorno : FUNCTION CADENA PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ salida1 LLAVE_DER'''
def p_cola(p):
  '''cola : SIGNO_DOLAR CADENA IGUAL NEW QUEUE PAREN_IZQ PAREN_DER'''
def p_switch1(p):
   '''SWITCH1 : SWITCH PAREN_IZQ  SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ CASE ENTERO PUNTODOBLE  BREAK LLAVE_DER'''

def p_valor(p):
  ''' valor :  STRING
   '''



def p_salida_forma1(p):
  '''salida1 : ECHO CADENA PUNTO_COMA'''


def p_salida_forma2(p):
  '''salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA'''


def p_salida_forma3(p):
  '''salida : PRINT STRING PUNTO_COMA'''


def p_variable_ps(p):
  '''variable : SIGNO_DOLAR CADENA IGUAL STRING PUNTO_COMA'''




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

