import ply.yacc as yacc
from lexicophp import tokens


def p_instrucciones(p):
    '''instrucciones : salida
                    | asignacion
                    | whileDeclaracion
                    | arreglo'''

def p_bucleWhile(p):
  '''bucleWhile : asignacion
                '''

def p_salida_forma1(p):
    "salida : ECHO STRING PUNTO_COMA"


def p_salida_forma2(p):
    "salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA"


def p_salida_forma3(p):
    "salida : PRINT STRING PUNTO_COMA"


def p_valor(p):
    '''valor : ENTERO
          | FLOTANTE
          | STRING
          | BOOLEANO'''


def p_asignacion_ps(p):
    "asignacion : SIGNO_DOLAR CADENA IGUAL valor PUNTO_COMA"

#para while
def p_condicion(p):
    '''condicion : IDENTICO
              | DIFERENTE
              | MAYOR_QUE
              | MENOR_QUE
              | MAYOR_IGUAL
              | MENOR_IGUAL'''

def p_whileDeclaracion(p):
  "whileDeclaracion : WHILE PAREN_IZQ SIGNO_DOLAR CADENA condicion valor PAREN_DER LLAVE_IZQ LLAVE_DER"

#para array
def p_arreglo_asociativo(p):
  "arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valor FLECHA valor PAREN_DER PUNTO_COMA"


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
