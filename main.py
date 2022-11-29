import tkinter
from tkinter import *
import tkinter.scrolledtext as st
import sintactico
import lexicophp 

from datetime import datetime 

today = datetime.now()

valorLexico= lexicophp.lexer
valorsintatico=sintactico.parser
analizadorLexico=lexicophp.obtener_validador_lexico()
analizadorSintactico= sintactico.obtener_analizador_sintactico()


##Logs
logs_file = open ('logs.txt','w')



## Root GUI
ventana=tkinter.Tk(className='PHP')
ventana.geometry("900x800")

## Etiqueta Principal
mensaje = tkinter.Label(ventana, text="Analizador del Lenguaje de PHP" , fg="#FFFFFF", bg='#008080',  font=("Arial", 25) )
mensaje.grid(row = 0, column = 0, padx = 15, columnspan=2)

##Etiqueta Ingreso
mensaje_in = tkinter.Label(ventana, text="Ingrese su código aquí:" , bg='#008080',  font=("Arial", 12))
mensaje_in.grid(row = 1, column = 0, padx = 2)

## Caja de ingreso
cajatexto = tkinter.scrolledtext.ScrolledText(ventana, width= 80, height = 12, wrap=WORD)
cajatexto.grid(row=2, column=0, padx=20, pady=20, rowspan=5)

## Caja de salida
muestra = tkinter.scrolledtext.ScrolledText(ventana, width= 80, height = 12, wrap=WORD)
muestra.grid(row = 12, column=0, padx = 20 ,pady = 20, rowspan=5)
muestra.configure(state='disabled')   

## Etiqueta Salida
mensaje_out = tkinter.Label(ventana, text="Salida:" , bg='#008080',  font=("Arial", 12))
mensaje_out.grid(row = 11, column = 0, padx = 2)


#sintactico Carlos Gomez
def sintatico():
    #obtenemos el codigo
    codigo = cajatexto.get("1.0", END)

    ##### LOGS #####
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\n")
    logs_file.write("Entrada:"+"\n" +codigo+"\n")
    ################

    # Habilitamos la seccion para que pueda ser modificable
    muestra.configure(state='normal')
    # Borramos el contenido Anterior
    muestra.delete("1.0", END)

    ##### LOGS #####
    logs_file.write("Salida:"+"\n")
    ################
    
    #Aquí debe hacerse el análisis sintáctico con el código y mostrarlo
    analisis = str(analizadorSintactico.parse(codigo))   
    #print(analisis)
    if len(sintactico.errores_sintaxis) > 0:
        #print(sintactico.errores_sintaxis)
        #errores = '\n'.join(sintactico.errores_sintaxis) + '\n'
        #muestra.insert("1.0", errores, 'warning')
        for i in range(len(sintactico.errores_sintaxis)):
            ##### LOGS #####
            logs_file.write(str(sintactico.errores_sintaxis[i])+"\n")
            ################
            muestra.insert( float(i+1), str(sintactico.errores_sintaxis[i])+"\n")
    
        sintactico.errores_sintaxis.clear() 
    else:
        # Insertamos el resultado
        muestra.insert("1.0", "Ingresi Válido")

    # deshabilitar la seccion p
    muestra.configure(state='disabled')   
        

def lexico():
    codigo = cajatexto.get("1.0", END)

    ##### LOGS #####
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\n")
    logs_file.write("Entrada:"+"\n" +codigo+"\n")
    ################

    ##Se habilita el bloque de salida
    muestra.configure(state='normal')
    # Limpiamos la caja
    muestra.delete("1.0", END)
   
    lista_tokens = [] 
    analizadorLexico.input(codigo)  #Pasamos el código a analizar
    lexicophp.getTokens(analizadorLexico, lista_tokens) # Enviamos el resultado del análisis a la lista    
  
    ##### LOGS #####
    logs_file.write("Salida:"+"\n")
    ################

    ## Mostramos los tokens en la caja de salida
    for i in range(0,len(lista_tokens)):
        
        ##### LOGS #####
        logs_file.write(str(lista_tokens[i])+"\n")
        ################

        muestra.insert( float(i+1), str(lista_tokens[i])+"\n")
    
    muestra.configure(state='disabled') #Volvemos a deshabilitar la caja de salida
 
def limpiar():
    cajatexto.delete("1.0", END)
    muestra.configure(state='normal')
    muestra.delete("1.0", END)

def salir():
    ventana.destroy()

#presentacion
botonLex = tkinter.Button(ventana, text="Análisis Léxico", width = 15, height=2, command=lexico)
botonLex.grid(row = 3, column = 1, padx = 15)

botonSin = tkinter.Button(ventana, text="Análisis Sintactico", width = 15, height=2, command=sintatico)
botonSin.grid(row = 4, column = 1, padx = 15)

botonSem = tkinter.Button(ventana, text="Análisis Semántico", width = 15, height=2)
botonSem.grid(row = 5, column = 1, padx = 15)

b_limpiar = tkinter.Button(ventana, text="Limpiar", width = 10, height=2, command=limpiar)
b_limpiar.grid(row = 14, column = 1, padx = 15, columnspan=1)

b_salir = tkinter.Button(ventana, text="Salir", width = 10, height=2, command=salir)
b_salir.grid(row = 15, column = 1, padx = 15, columnspan=1)

ventana.configure(bg='#008080')
ventana.mainloop()
