import ply.yacc as yacc
import ply.lex as lex
from lexicophp import tokens 


#### Todas las instrucciones disponibles ###
def p_instrucciones(p):  
  '''instrucciones : valor
                    | decl_variable
                    | menor
                    | mayor
                    | asignacion
                    | salida
                    | prueba
                    | estructuras_control
                    | estructuras_datos
                    | funciones  
                    | op_logica
                    | op_pila
                    | declaracion
                    | declaracionp
                    | declaracion_s
                    | crecimiento
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
  '''salida : ECHO STRING PUNTO_COMA'''

def p_prueba(p):
  '''prueba : ECHO SIGNO_DOLAR VARIABLE PUNTO_COMA'''

def p_salida_forma2(p):
  '''salida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA'''

def p_salida_forma3(p):
  '''salida : PRINT STRING PUNTO_COMA'''



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
#bloques de código permitidos dentro de alguna funcion
def p_bloque(p):
  ''' bloque : asignacion
              | salida
              | retorno
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
   '''for : FOR PAREN_IZQ declaracion declaracionp declaracion_s PAREN_DER LLAVE_IZQ prueba LLAVE_DER'''

def p_declaracion(p):
  '''declaracion :  SIGNO_DOLAR VARIABLE IGUAL ENTERO PUNTO_COMA'''
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

##### REGLAS SINTACTICAS

##  Sentencia IF-ELSEIF-ELSE
# Ejemplo: if(3>=2){print"mayor";}elseif(3==2){print "iguales";}else{print "menor";}


# if-else
def p_if_else_corto(p):
  " if_else : if_else_inicio if_else_fin"

# if-elseif-else
def p_if_else_extendido(p):
  " if_else : if_else_inicio if_else_cuerpo if_else_fin"

# bloque IF
def p_if_else_inicio(p):
  "if_else_inicio : IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER"

# bloque ELSEIF
def p_if_else_cuerpo(p):
  ''' if_else_cuerpo : ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER
                    |  ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER if_else_cuerpo
  '''

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
  " op_pila : decl_variable RESTA MAYOR_QUE operad_pila"

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


# retorno de variable
def p_retorno(p):
  ''' retorno : RETURN decl_variable PUNTO_COMA'''

##### REGLAS SEMANTICAS

## Concatenación de String

## Casting



########## EMILY CORDERO  ##########
def p_contenido(p):
    '''contenido : bloque
               | sinRetorno'''

## While
def p_whileDeclaracion(p):
    "whileDeclaracion : WHILE PAREN_IZQ decl_variable operad_log valor PAREN_DER LLAVE_IZQ contenido LLAVE_DER"


## Array 
## array() 
## array(....)
## array( )
def p_valoresSeparadosComa(p):
    'valores : valor repite_valores'

def p_repite_valoresSeparadosComa(p):
    ''' repite_valores : COMA valor
                        | COMA valor repite_valores
    '''

def p_arreglo_asociativo(p):
    "arreglo : decl_variable IGUAL ARRAY PAREN_IZQ valor FLECHA valor PAREN_DER PUNTO_COMA"


def p_arreglo_parentesis(p):
    "arreglo : decl_variable IGUAL ARRAY PAREN_IZQ valores PAREN_DER PUNTO_COMA"


#para array con asignacion con flecha
def p_valoresArregloAsociativo(p):
    " valoresflecha : valor FLECHA valor repite_valores_f"


def p_repite_valoresSeparados_flecha(p):
  ''' repite_valores_f : COMA valor FLECHA valor
                        | COMA valor FLECHA valor repite_valores
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
        errores_sintaxis.append("Error de sintaxis en token {}, en la linea {}".format(p.type, p.lineno))
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

