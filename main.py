import ply.lex as lex

# Lista de palabras reservadas
#Elaborado por Carlos Gómez
reserved = {
"__halt_compiler()":"_HALT_COMPILER()", 	
"break":"BREAK",    
"clone":"CLONE",
"die()":"DIE()",
"empty()":"EMPYT()",
"endswitch":"ENDSWITCH",
"final":"FINAL",
"function":"FUNCTION",
"include":"INCLUDE",
"isset()":"ISSET()",
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
"include_once":"INCLUDE_ONCE",
"list()":"LIST()",
"print":"PRINT",
"requie_once":"REQUIE_ONCE",
"trait":"TRAIT",
"while":"WHILE",
"and":"AND",
"case":"CASE",
"continue":"CONTINUE",
"echo":"ECHO",
"endfor":"ENDFOR",
"eval()":"EVAL()",
"fn":"FN",
"goto":"GOTO",
"instanceof":"INTANCEOF",
"match":"MACHT",
"private":"PRIVATE",
"return":"RETURN",
"try":"TRY",
"xor":"XOR",
"array()":"ARRAY()",
"cath":"CATH",
"declare":"DECLARE",
"else":"ELSE",
"endeforeach":"ENDFOREACH",
"exit()":"EXIT()",
"for":"FOR",
"if": "IF",
"for": "FOR",
"inteadof":"INTEADOF",
"namespace":"NAMESPACE",
"protected":"PROTECTED",
"static":"STATIC",
"unset()":"UNSET()",
"yeild":"YEILD",
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
"yeild_from":"YEILD_FROM"
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

