ls_programas = []

import os
sw = True
def fnt_agreagar(p):
    global ls_programas
    if p == '':
        enter = input('debe ingresar un programa <ENTER>')
    else:
        ls_programas.append(p)
        enter = input(f'El programa {p} Ha sido registrado con exito <ENTER>')
def fnt_selccion(op):
    if op == '1':
        program = input('ingrese el nombre del progrma ')
        fnt_agreagar(program)
    elif op == '2':
        if len(ls_programas) > 0:
            fnt_mostrar()
        else:
            enter = input('\nNo se encontraron registros <ENTER>')
    elif op == '3':
        fnt_eliminar()
    elif op == '4':
        print(ls_programas,'\n')
        pos = input('\nIngrese la posicion del progrma a eliminar')
        fnt_eliminarP(pos)    
        
def fnt_mostrar():
    print(ls_programas)
    enter = input('\n<ENTER>')
def fnt_eliminar():
    ls_programas.pop()
    enter = input('\nProgrma eliminado con exito <ENTER>')
def fnt_eliminarP(pos):
    tamaño = len(ls_programas) 
    if len(ls_programas) >0: 
        if tamaño > int(pos):
            ls_programas.pop(int(pos))
            enter = input('\nProgrma eliminado con exito <ENTER> ')
        else:
            enter =  input('\nError, posición no valida <ENTER>')
    else:
        enter = input('\nNo hay programas /  posicion no valida <ENTER>')

while sw == True:
    os.system('cls')
    var_opcion = input('<<<< MENU >>>> \n1. AGREGAR\n2. MOSTRAR\n3. ELIMINAR PROGRMA x ORDEN\n4. ELIMININACION POR POSICION\n -->')
    fnt_selccion(var_opcion)



