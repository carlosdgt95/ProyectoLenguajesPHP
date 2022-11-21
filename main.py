
#import sintactico
import ply.yacc as yacc
from lexicophp import tokens

import logging


# Definición del logger root
# -----------------------------------------------------------------------------
logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level  = logging.INFO,
    filemode = "a"
    )

# Nuevos handlers
# -----------------------------------------------------------------------------
# Si el root logger ya tiene handlers, se eliminan antes de añadir los nuevos.
# Esto es importante para que los logs no empiezen a duplicarse.
if logging.getLogger('').hasHandlers():
    logging.getLogger('').handlers.clear()
    
# Se añaden dos nuevos handlers al root logger, uno para los niveles de debug o
# superiores y otro para que se muestre por pantalla los niveles de info o
# superiores.
file_debug_handler = logging.FileHandler('logs_debug.log')
file_debug_handler.setLevel(logging.DEBUG)
file_debug_format = logging.Formatter('%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s')
file_debug_handler.setFormatter(file_debug_format)
logging.getLogger('').addHandler(file_debug_handler)

consola_handler = logging.StreamHandler()
consola_handler.setLevel(logging.INFO)
consola_handler_format = logging.Formatter('%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s')
consola_handler.setFormatter(consola_handler_format)
logging.getLogger('').addHandler(consola_handler)

# ======================= MAIN SCRIPT ============================================
logging.debug('Inicio main script')
logging.info('Inicio main script')
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

logging.debug('Fin main script')
logging.info('Fin main script')

logging.shutdown()

