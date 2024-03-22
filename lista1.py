ls_nombre = []

var_n = (input('ingrese su nombre:  '))
if var_n == '':
    enter = input('debe de ingresra un nombre: <ENTER>  ')
else:
    ls_nombre.append(var_n)
    enter = input(f'{var_n} Ha sido almacenado con exito <ENTER>')
    

print(ls_nombre)