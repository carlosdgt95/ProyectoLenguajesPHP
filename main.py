import ply.yacc as yacc
from lexicophp import tokens


def p_instrucciones(p):
    '''instrucciones : salida
                    | asignacion
                    | whileDeclaracion
                    | arreglo
                    | tipoFunciones'''


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


def p_contenido(p):
    '''contenido : salida
               | asignacion
               | sinRetorno'''

def p_whileDeclaracion(p):
    "whileDeclaracion : WHILE PAREN_IZQ SIGNO_DOLAR CADENA condicion valor PAREN_DER LLAVE_IZQ contenido LLAVE_DER"


#para array
def p_valoresSeparadosComa(p):
    'valores : valor repite_valores'


def p_repite_valoresSeparadosComa(p):
    '''
  repite_valores : COMA valor
                | COMA valor repite_valores'''


def p_arreglo_asociativo(p):
    "arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valor FLECHA valor PAREN_DER PUNTO_COMA"


def p_arreglo_parentesis(p):
    "arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valores PAREN_DER PUNTO_COMA"


#para array con asignacion con flecha


def p_valoresArregloAsociativo(p):
    'valoresflecha : valor FLECHA valor repite_valores_f'


def p_repite_valoresSeparados_flecha(p):
    '''
  repite_valores_f : COMA valor FLECHA valor
                | COMA valor FLECHA valor repite_valores'''


def p_arreglo_asociativo(p):
    "arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valoresflecha PAREN_DER PUNTO_COMA"

##########
def p_funciones(p):
  '''tipoFunciones : sinRetorno'''

def p_sinretorno(p):
  '''sinRetorno : FUNCTION CADENA PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ contenido LLAVE_DER'''

##########

  
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