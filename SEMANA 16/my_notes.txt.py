#SE ABRE Y SE CIERRA EL DOCUMENTO
with open('My_Notes.txt','r' ) as archivo:
    lineas =archivo.readlines()
 # SE IMPRIME LA LINEAS DEL ARCHIVO  MY_NOTES.TXT
    print(lineas)
with open('My_Notes.txt', 'a') as archivo:
 # CON EM METODO WRITE SE PUEDE AGRGAR LAS LINEAS QEU QUERRAMOS
    archivo.write('NO ES CASUALIDAD QUE ESTES AQUI \n LA VIDA ES UN REGALO\n')
for l in lineas:
    print(l.replace('\n', ''))

