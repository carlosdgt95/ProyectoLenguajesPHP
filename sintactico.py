import ply.yacc as yacc
import ply.lex as lex
from lexicophp import tokens 


#### Todas las instrucciones disponibles ###
def p_instrucciones(p):  
  '''instrucciones : valor
                    | asignacion
                    | concatenacion
                    | salida
                    | estructuras_control
                    | estructuras_datos
                    | funciones
                    | op_pila
                    | valorc
  '''

def p_decl_variable(p):
  "decl_variable : SIGNO_DOLAR VARIABLE"

## Definicion de una variable
def p_asignacion(p):
  "asignacion : decl_variable IGUAL valor PUNTO_COMA"


## Valores que pueden ir en una variable
# Ejemplo: $_variable = regla_valor
def p_valor(p):
  '''valor : datos 
          | pila
          | cola
          | arreglo
  '''

#Tipos de datos primitivos
def p_datos(p):
  '''datos : ENTERO
          | FLOTANTE
          | STRING 
          | BOOLEANO 
  '''

#Todos los objetos posibles como salidas
def p_salidas_pos(p):
  '''salidas_pos : datos
                | decl_variable
                | conca_string
  '''


#Múltiples salidas permitidas
def p_salida_forma1(p):
  '''salida : ECHO salidas_pos PUNTO_COMA'''

def p_salida_forma2(p):
  '''salida : PRINT PAREN_IZQ salidas_pos PAREN_DER PUNTO_COMA'''

def p_salida_forma3(p):
  '''salida : PRINT salidas_pos PUNTO_COMA'''



### Definiciones Generales ###

def p_estructuras_control(p):
  ''' estructuras_control : if_else 
                          | for
                          | whileDeclaracion
  '''

def p_estructuras_datos(p):
  ''' estructuras_datos : pila 
                        | cola
                        | arreglo
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

### Operadores Logicos ###
def p_operad_arit(p):
  '''operad_arit : SUMA
                | RESTA
                | MULTIPL
                | DIVISION
                | DIVISION_ENT
                | POTENCIA
                | MODULO
  '''


#bloques de código permitidos dentro de alguna funcion
def p_bloque(p):
  ''' bloque : asignacion
              | salida
              | retorno
              | estructuras_control
  '''

########## CARLOS GOMEZ  ##########
## Funcion sin retorno 

def p_sinretorno(p):
  '''sinRetorno : FUNCTION VARIABLE PAREN_IZQ decl_variable PAREN_DER LLAVE_IZQ salida LLAVE_DER'''


## Cola 
def p_cola(p):
  " cola : NEW QUEUE PAREN_IZQ PAREN_DER "


## for
def p_for(p):
   '''for : FOR PAREN_IZQ asignacion declaracionp declaracion_s PAREN_DER LLAVE_IZQ salida LLAVE_DER'''


def p_declaracionM(p):
   '''declaracionp :  SIGNO_DOLAR VARIABLE valorc'''

def p_menor(p):
  '''menor : MENOR_IGUAL ENTERO PUNTO_COMA'''

def p_mayor(p):
  '''mayor : MAYOR_IGUAL ENTERO PUNTO_COMA'''

def p_valorC(p):
  ''' valorc : menor
              | mayor'''

def p_declaracionsimple(p):
   '''declaracion_s : SIGNO_DOLAR VARIABLE crecimiento'''

def p_crecimiento(p):
  '''crecimiento : INCREMENTO 
                | DECREMENTO'''


########## KARLA CASTRO  ##########

#### Reglas Sintácticas

# if-else
def p_if_else_corto(p):
  " if_else : if_else_inicio if_else_fin"

# if-elseif-else
def p_if_else_extendido(p):
  " if_else : if_else_inicio if_else_cuerpo if_else_fin"

# bloque IF
def p_if_else_inicio(p):
  "if_else_inicio : IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ bloque LLAVE_DER"

# bloque ELSEIF
def p_if_else_cuerpo(p):
  ''' if_else_cuerpo : ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ bloque LLAVE_DER
                    |  ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ bloque LLAVE_DER if_else_cuerpo
  '''

# bloque ELSE
def p_if_else_fin(p):
  "if_else_fin : ELSE LLAVE_IZQ bloque LLAVE_DER"

#Permitidas para tipos de datos iguales
def p_op_logica(p):
  ''' op_logica : ENTERO operad_log ENTERO
                | FLOTANTE operad_log FLOTANTE
                | STRING operad_log STRING
                | BOOLEANO
  '''


## PILA 

# regla_variable new SplStack()
def p_pila(p):
  " pila :  NEW STACK PAREN_IZQ PAREN_DER"

# métodos de la pila
# Ejemplo: $_pila1 -> push(2);
def p_op_pila(p):
  " op_pila : decl_variable ASIG_OBJ operad_pila"

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
  ''' funcion_variable : FUNCTION VARIABLE PAREN_IZQ TRES_PUNTOS decl_variable PAREN_DER LLAVE_IZQ bloque LLAVE_DER'''


# retorno de variables, datos primitivos
def p_retorno(p):
  ''' retorno : RETURN salidas_pos PUNTO_COMA'''


#### Reglas semánticas

## Concatenacion 
# Ejemplos:
# $var = "casa"
# $var.= 2    -----> "casa2"
# $var.=true ------> "casa1"
def p_concatenacion(p):
  "concatenacion : decl_variable ASIG_CONCA datos PUNTO_COMA"

def p_conca_string(p):
  "conca_string : STRING PUNTO STRING"

## Salida de objetos
# Solo print_r permite imprimir las estructuras de datos sin recorrerlas
def p_salida_obj(p):
  "salida : PRINT_R PAREN_IZQ valor PAREN_DER PUNTO_COMA "

def p_salidas_pos_obj(p):
  '''salidas_pos_obj : valor
                | decl_variable
                | conca_string
  '''



########## EMILY CORDERO  ##########
def p_contenido(p):
    '''contenido : bloque
               | sinRetorno'''

## While
def p_whileDeclaracion(p):
    "whileDeclaracion : WHILE PAREN_IZQ decl_variable operad_log valor PAREN_DER LLAVE_IZQ contenido LLAVE_DER"



def p_valoresSeparadosComa(p):
    'valores : datos repite_valores'

def p_repite_valoresSeparadosComa(p):
    ''' repite_valores : COMA datos
                        | COMA datos repite_valores
    '''

def p_arreglo_asociativo(p):
    "arreglo :  ARRAY PAREN_IZQ datos FLECHA datos PAREN_DER"


def p_arreglo_parentesis(p):
    "arreglo : ARRAY PAREN_IZQ valores PAREN_DER"


#para array con asignacion con flecha
def p_valoresArregloAsociativo(p):
    " valoresflecha : datos FLECHA datos repite_valores_f"


def p_repite_valoresSeparados_flecha(p):
  ''' repite_valores_f : COMA datos FLECHA datos
                        | COMA datos FLECHA datos repite_valores
  '''

def p_arreglo_asociativo(p):
    "arreglo : decl_variable IGUAL ARRAY PAREN_IZQ valoresflecha PAREN_DER PUNTO_COMA"

# Función dentro de otra funcion
def p_sinretorno(p):
  '''sinRetorno : FUNCTION VARIABLE PAREN_IZQ decl_variable PAREN_DER LLAVE_IZQ contenido LLAVE_DER'''



errores_sintaxis = []  
def p_error(p):
    if p:
        print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        errores_sintaxis.append("Error de sintaxis en token {}, en la linea {}, Col: {}".format(p.type, p.lineno, p.lexpos))
        parser.errok()
        # logs_file.write(today.strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +"Error de sintaxis - Token: "+ str(p.type) +", Línea: "+ str(p.lineno) +", Col: "+ str(p.lexpos) +"\n")
    else:
        errores_sintaxis.append("Error de sintaxis Fin de Linea")
        print("Error de sintaxis Fin de Linea")
        # logs_file.write(today.strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +"Error de sintaxis Fin de Linea"+"\n")

#Construya el lexer


parser = yacc.yacc()
def obtener_analizador_sintactico():
    return yacc.yacc()


def validaRegla(s):
    result1 = parser.parse(s)
    print(result1)
    return result1




# Método para analizar cada línea

# archivo = open("algoritmos.txt")
# for linea in archivo:
#   print(">>" + linea)
#   validaRegla(linea)
#   logs_file = open ('logs.txt','w')
#   if len(linea) == 0:
#     logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +linea+"\n")
 
#     break
    



# while True:
  # try:
  #   #Crear archivo para logs
  #   logs_file = open ('logs.txt','a')
  #   s = input('calc > ')

  # except EOFError:
  #   break
  # if not s: continue
  # logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +s+"\n")
  # validaRegla(s)

