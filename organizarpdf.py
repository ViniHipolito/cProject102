import os
import shutil

## troque o [NOME DO USUARIO] com o do seu computador, caso contrário não irá funcionar
from_dir = 'C:/Users/[NOME DO USUARIO]/Downloads'
to_dir = 'C:/Users/[NOME DO USUARIO]/Downloads/Arquivos_PDF'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for d in list_of_files:
    name, extension = os.path.splitext(d)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.pdf']:
        path1 = from_dir + '/' + d
        path2 = to_dir + '/' + 'pdf'
        path3 = to_dir + '/' + 'pdf' + '/' + d
        
        if os.path.exists(path2):
            print('movendo' + d)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('movendo' + d)
            shutil.move(path1, path3)