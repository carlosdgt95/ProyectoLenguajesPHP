#import sintactico
import ply.yacc as yacc
from lexicophp import tokens

#def p_cuerpo(p):
# '''cuerpo: salida
#  | variable'''

def p_instrucciones(p):  #todas las disponibles
  '''instrucciones : valor
                    | asignacion
                    | salida 
                    | estructuras_control  
                    | op_logica
  '''
#tipos de datos
def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | STRING 
          | BOOLEANO 
  '''

def p_asignacion(p):
  "asignacion : SIGNO_DOLAR CADENA IGUAL valor PUNTO_COMA"

#Múltiples salidas permitidas
def p_salida_forma1(p):
  "salida : ECHO STRING PUNTO_COMA"

def p_salida_forma2(p):
  "salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA"

def p_salida_forma3(p):
  "salida : PRINT STRING PUNTO_COMA"

def p_estructuras_control(p):
  " estructuras_control : if_else "


# Sentencia IF-ELSEIF-ELSE Karla Castro
def p_if_else(p):
  ''' if_else : if_else_corto
              | if_else_extendido
  '''

def p_if_else_corto(p):
  " if_else_corto : if_else_inicio if_else_fin"

def p_if_else_extendido(p):
  " if_else_extendido : if_else_inicio if_else_cuerpo if_else_fin"

def p_if_else_inicio(p):
  "if_else_inicio : IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER"

def p_if_else_cuerpo(p):
  "if_else_cuerpo : ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER"

def p_if_else_fin(p):
  "if_else_fin : ELSE LLAVE_IZQ salida LLAVE_DER"

#Permitidas para tipos de datos iguales
def p_op_logica(p):
  ''' op_logica : ENTERO operad_log ENTERO
                | FLOTANTE operad_log FLOTANTE
                | STRING operad_log STRING
                | BOOLEANO
  '''

def p_operad_log(p):
  '''operad_log : IDENTICO
                | DIFERENTE
                | MAYOR_QUE
                | MAYOR_IGUAL
                | MENOR_QUE
                | MENOR_IGUAL
  '''



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

