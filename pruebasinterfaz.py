
import tkinter
from tkinter import *
import tkinter.scrolledtext as st
import main
import lexicophp
from main import obtener_analizador_sintactico,errores_sintaxis
from tkinter import *
from lexicophp import  getTokens
valorLexico= lexicophp.lexer
valorsintatico=main.parser
analizadorLexico=lexicophp.obtener_validador_lexico()
analizadorSintactico=obtener_analizador_sintactico()
ventana=tkinter.Tk()
ventana.geometry("1000x500")
etiqueta= tkinter.Label(ventana,text="PHP")
botonComprobarLexico= tkinter.Button(ventana,text="Comprobar")
cajatexto=tkinter.Entry(ventana)
cajatextoSalida=tkinter.Entry(ventana)

# cajatextoSalida.grid(row=10, column=5,padx=50)
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
    if len(errores_sintaxis) > 0:
        errores = '\n'.join(errores_sintaxis) + '\n'
        muestra.insert("1.0", errores, 'warning')
        errores_sintaxis.clear() 
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
    getTokens(analizadorLexico, lista)    
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
 

#presentacion
cajatexto.grid(row=4, column=5,padx=50)
botonLex = tkinter.Button(ventana, text="Análisis \nLéxico", width = 10, height=2, command=lexico)
botonLex.grid(row = 4, column = 7, padx = 15)
botonSin = tkinter.Button(ventana, text="Análisis \nSintactico", width = 10, height=2, command=sintatico)
botonSin.grid(row = 4, column = 9, padx = 15)
muestra = st.ScrolledText(ventana, width= 120, height = 14, wrap=WORD)
muestra.grid(row = 10, columnspan=10, sticky = W+E, padx = 15 ,pady = 5)
etiquetaSalida = tkinter.Label(ventana, text = "Salida:", justify = "left")


#etiqueta.pack()
#cajatexto.pack()
#botonLex.pack()
#etiquetaSalida.pack()
#muestra.pack()
#cajatextoSalida.pack()








ventana.mainloop()
