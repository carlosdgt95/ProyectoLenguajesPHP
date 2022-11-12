import ply.lex as lex

# Lista de palabras reservadas
#Elaborado por Carlos Gómez
reserved = {

"break":"BREAK",    
"clone":"CLONE",


"endswitch":"ENDSWITCH",
"final":"FINAL",
"function":"FUNCTION",
"include":"INCLUDE",

"or": "OR",
"requiere":"REQUIERE",
"throw":"THROW",
"var":"VAR",
"abstract":"ABSTRACT",
"callable":"CALLABLE",
"const":"CONST",
"do":"DO",
"endddeclare":"ENDDECLARE",
"endwhile":"ENDWHILE",
"finally":"FINALLY",
"global":"GLOBAL",


"print":"PRINT",

"trait":"TRAIT",
"while":"WHILE",
"and":"AND",
"case":"CASE",
"continue":"CONTINUE",
"echo":"ECHO",


"fn":"FN",

"instanceof":"INTANCEOF",
"match":"MACHT",
"private":"PRIVATE",
"return":"RETURN",
"try":"TRY",
"xor":"XOR",

"cath":"CATH",
"declare":"DECLARE",
"else":"ELSE",


"for":"FOR",
"if": "IF",
"for": "FOR",
"inteadof":"INTEADOF",
"namespace":"NAMESPACE",
"protected":"PROTECTED",
"static":"STATIC",


"as":"AS",
"class":"CLASS",
"default":"DEFAULT",
"elseif":"ELSEIF",
"endif":"ENDIF",
"extends":"EXTENDS",
"foreach":"FOREACH",
"implements":"IMPLEMENTS",
"interface":"INTERFACE",
"new":"NEW",
"public":"PUBLIC",
"switch":"SWITCH",
"use":"USE",

}
#Elaborado Carlos Gomez
#Definicion de tokens
tokens = (
    'ENTERO',
    'FLOTANTE',
  
) + tuple( reserved.values() )

#ER para tokens definidos

def t_ENTERO(t):
    r'(-?[1-9]\d*)|0'
    t.value = int(t.value)
    return t

def t_FLOTANTE(t):
    r'(-?[1-9]\d*\.\d+)|0.0'
    t.value = float(t.value)
    return t
#Carlos Gomez
#lee archivo--------------------------------------------------------------------------------------
# archivo = open("archivo.txt")
# for linea in archivo:
#     print(">>"+linea)
#     analizar(linea)
#     if len(linea) == 0:
#         break


# def getTokens(lexer):

#     while True:
    
#         tok = lexer.token()
    
#         if not tok:
#             break
    
#         print(tok)

# lexer = lex.lex()


# linea = " "

# while linea != "":

#     linea=input(">>")
#     lexer.input(linea)
#     getTokens(lexer)

# print("Ejecución terminada")
