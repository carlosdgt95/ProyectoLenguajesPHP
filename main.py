import tkinter
from tkinter import *
import tkinter.scrolledtext as st
import sintactico
import lexicophp 

valorLexico= lexicophp.lexer
valorsintatico=sintactico.parser
analizadorLexico=lexicophp.obtener_validador_lexico()
analizadorSintactico= sintactico.obtener_analizador_sintactico()

ventana=tkinter.Tk(className='PHP')
ventana.geometry("900x800")

mensaje = tkinter.Label(ventana, text="Analizador del Lenguaje de PHP" , fg="#FFFFFF", bg='#008080',  font=("Arial", 25) )
mensaje.grid(row = 0, column = 0, padx = 15, columnspan=2)

mensaje_in = tkinter.Label(ventana, text="Ingrese su código aquí:" , bg='#008080',  font=("Arial", 12))
mensaje_in.grid(row = 1, column = 0, padx = 2)

#cajatexto=tkinter.Entry(ventana)
## Caja de ingreso
cajatexto = tkinter.scrolledtext.ScrolledText(ventana, width= 80, height = 12, wrap=WORD)
cajatexto.grid(row=2, column=0, padx=20, pady=20, rowspan=5)

## Caja de salida
muestra = tkinter.scrolledtext.ScrolledText(ventana, width= 80, height = 12, wrap=WORD)
muestra.grid(row = 12, column=0, padx = 20 ,pady = 20, rowspan=5)


mensaje_out = tkinter.Label(ventana, text="Salida:" , bg='#008080',  font=("Arial", 12))
mensaje_out.grid(row = 11, column = 0, padx = 2)

cajatextoSalida=tkinter.Entry(ventana)

#sintactico Carlos Gomez
def sintatico():
    #obtenemos el codigo
    codigo = cajatexto.get()

    
    # Habilitamos la seccion para que pueda ser modificable
    muestra.configure(state='normal')

    # Borramos el contenido Anterior
    muestra.delete("1.0", END)

    #Aquí debe hacerse el análisis sintáctico con el código y mostrarlo    
    #analizadorSintactico.lineno = 1
    analisis = str(analizadorSintactico.parse(codigo))   
    if len(sintactico.errores_sintaxis) > 0:
        errores = '\n'.join(sintactico.errores_sintaxis) + '\n'
        muestra.insert("1.0", errores, 'warning')
        sintactico.errores_sintaxis.clear() 
    else:
        # Insertamos el resultado
        muestra.insert("1.0", analisis)

    # deshabilitar la seccion p
    muestra.configure(state='disabled')   
        


#lexico Carlos Gomez
def lexico():
    codigo = cajatexto.get()
    muestra.configure(state='normal')

    # Borramos el contenido Anterior
    muestra.delete("1.0", END)
   
    lista = []
    # lexicophp.lineno = 1
    lista.append(codigo)
    analizadorLexico.input(codigo)
    lexicophp.getTokens(analizadorLexico, lista)    
    analisis = ''

    for elem in lista:
        #print("xxxxeeee",elem)
        analisis += repr(elem)
        analisis += ' '
       
    
    #VL=lexicophp.analizar(analisis)
    muestra.insert('1.0',analisis)
    #print("algooooo", analisis)
    muestra.configure(state='disabled')
    #print("algoxxx",(VL))
    #lexicophp.getTokens(VL,lista)
    
    
    #muestra(lexicophp.analizar(analisis))
 
def limpiar():
    cajatexto.delete("1.0", END)
    muestra.delete("1.0", END)

def salir():
    ventana.destroy()

#presentacion
botonLex = tkinter.Button(ventana, text="Análisis \nLéxico", width = 10, height=2, command=lexico)
botonLex.grid(row = 3, column = 1, padx = 15)

botonSin = tkinter.Button(ventana, text="Análisis \nSintactico", width = 10, height=2, command=sintatico)
botonSin.grid(row = 4, column = 1, padx = 15)

botonSem = tkinter.Button(ventana, text="Análisis \nSemántico", width = 10, height=2)
botonSem.grid(row = 5, column = 1, padx = 15)

b_limpiar = tkinter.Button(ventana, text="Limpiar", width = 10, height=2, command=limpiar)
b_limpiar.grid(row = 14, column = 1, padx = 15, columnspan=1)

b_salir = tkinter.Button(ventana, text="Salir", width = 10, height=2, command=salir)
b_salir.grid(row = 15, column = 1, padx = 15, columnspan=1)

ventana.configure(bg='#008080')
ventana.mainloop()
