import os
import chardet


def convertFiles(files):
    for file in files['files']:
        arquivo_origem = files['basePath'] + '/' + file
        arquivo_destino = files['basePathDest'] + '/' + file

        with open(arquivo_origem, 'rb') as file:
            result = chardet.detect(file.read())
        print(result['encoding'])


        # Abrir o arquivo original com a codificação que ele tem
        with open(arquivo_origem, 'r', encoding=result['encoding']) as file_origem:
            conteudo = file_origem.read()

        # Escrever o conteúdo no novo arquivo com codificação UTF-8
        with open(arquivo_destino, 'w', encoding='utf-8') as file_destino:
            file_destino.write(conteudo)

        print(f"Arquivo convertido e salvo como {arquivo_destino}")


baseOldFolder = './tables'

oldPath = {
'basePath' : baseOldFolder + '/old',
'files' : os.listdir( baseOldFolder + '/old'),
'basePathDest' : baseOldFolder +  '/utf'

}

baseNewFolder = './tablesV2'
newPath = {
    'basePath' : baseNewFolder + '/old',
    'files': os.listdir(baseNewFolder + '/old'),
    'basePathDest' : baseNewFolder + '/utf'
}

convertFiles(newPath)
