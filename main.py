
#import sintactico
import ply.yacc as yacc
from lexicophp import tokens


#### Todas las instrucciones disponibles ###
def p_instrucciones(p):  
  '''instrucciones : valor
                    | datos
                    | asignacion
                    | salida 
                    | estructuras_control
                    | estructuras_datos
                    | funciones  
                    | op_logica
                    | op_pila
  '''
## Definicion de una variable
def p_asignacion(p):
  "asignacion : SIGNO_DOLAR CADENA IGUAL valor PUNTO_COMA"

## Valores que pueden ir en una variable
# Ejemplo: $_variable = regla_valor
def p_valor(p):
  '''valor : datos 
          | pila
          | cola
  '''

#Tipos de datos primitivos
def p_datos(p):
  '''datos : ENTERO
          | FLOTANTE
          | STRING 
          | BOOLEANO 
  '''


#Múltiples salidas permitidas
def p_salida_forma1(p):
  '''salida : ECHO CADENA PUNTO_COMA'''

def p_salida_forma2(p):
  '''salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA'''

def p_salida_forma3(p):
  '''salida : PRINT STRING PUNTO_COMA'''



### Definiciones Generales ###

def p_estructuras_control(p):
  ''' estructuras_control : if_else 
                          | switch1
  '''

def p_estructuras_datos(p):
  ''' estructuras_datos : pila 
                        | cola
  '''

def p_funciones(p):
  '''funciones : funcion_variable 
                | sinRetorno
  '''

### Operadores Logicos ###
def p_operad_log(p):
  '''operad_log : IDENTICO
                | DIFERENTE
                | MAYOR_QUE
                | MAYOR_IGUAL
                | MENOR_QUE
                | MENOR_IGUAL
  '''

########## CARLOS GOMEZ  ##########
## Funcion sin retorno 

def p_sinretorno(p):
  '''sinRetorno : FUNCTION CADENA PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ salida LLAVE_DER'''


## Cola 
def p_cola(p):
  " cola : NEW QUEUE PAREN_IZQ PAREN_DER "

## Switch 
def p_switch1(p):
   '''switch1 : SWITCH PAREN_IZQ  SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ CASE ENTERO PUNTODOBLE  BREAK LLAVE_DER'''


########## KARLA CASTRO  ##########

##  Sentencia IF-ELSEIF-ELSE
# Ejemplo: if(3>=2){print"mayor";}elseif(3==2){print "iguales";}else{print "menor";}

def p_if_else(p):
  ''' if_else : if_else_corto
              | if_else_extendido
  '''
# if-else
def p_if_else_corto(p):
  " if_else_corto : if_else_inicio if_else_fin"

# if-elseif-else
def p_if_else_extendido(p):
  " if_else_extendido : if_else_inicio if_else_cuerpo if_else_fin"

# bloque IF
def p_if_else_inicio(p):
  "if_else_inicio : IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER"

# bloque ELSEIF
def p_if_else_cuerpo(p):
  "if_else_cuerpo : ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER"

# bloque ELSE
def p_if_else_fin(p):
  "if_else_fin : ELSE LLAVE_IZQ salida LLAVE_DER"

#Permitidas para tipos de datos iguales
def p_op_logica(p):
  ''' op_logica : ENTERO operad_log ENTERO
                | FLOTANTE operad_log FLOTANTE
                | STRING operad_log STRING
                | BOOLEANO
  '''



## PILA 

# regla_variable new SplStack();
def p_pila(p):
  " pila :  NEW STACK PAREN_IZQ PAREN_DER"

# métodos de la pila
# Ejemplo: $_pila1 -> push(2);
def p_op_pila(p):
  " op_pila : SIGNO_DOLAR CADENA RESTA MAYOR_QUE operad_pila"

# push:añade, pop:elimina, count:cuenta, current:muestra el valor
def p_operad_pila(p):
  ''' operad_pila : PUSH PAREN_IZQ datos PAREN_DER PUNTO_COMA 
                  | POP PAREN_IZQ PAREN_DER PUNTO_COMA
                  | COUNT PAREN_IZQ PAREN_DER PUNTO_COMA
                  | CURRENT PAREN_IZQ PAREN_DER PUNTO_COMA
  '''


## Funciones con lista de argumentos de longitud variable

# Ejemplo: function abc(...$_num){ return $_suma}
def p_funcion_variable(p):
  ''' funcion_variable : FUNCTION CADENA PAREN_IZQ TRES_PUNTOS SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ bloque LLAVE_DER'''

#bloques de código permitidos para esta funcion
def p_bloque(p):
  ''' bloque : asignacion
              | salida
              | retorno
  '''

# retorno de variable
def p_retorno(p):
  " retorno : RETURN SIGNO_DOLAR CADENA"




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
