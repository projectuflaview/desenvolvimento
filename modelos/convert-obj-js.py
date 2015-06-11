# Script Convert-obj-js
# Enrico Navarro
# convert_obj_three.py by mrdoob -
# https://github.com/mrdoob/three.js/blob/master/utils/converters/obj/convert_obj_three.py
# V1.0

import os

def main():
    ''' Fun��o principal do c�digo, le o comando, separa o caminho e chama
        outras fun��es. '''
    #Le o comando / Exemplo, obj/*.obj
    s = raw_input("Digite o comando: ")

    #Separa o Caminho
    i = s.index('*')
    caminho = s[:i]

    #Chamada de Fun��es
    objList = readObj(caminho)
    convertJs(objList,caminho)

    raw_input("\nEnd of Code")

def readObj(caminho):
    ''' Fun��o responsavel por listar todos os arquivos dentro de um diret�rio'''
    listaObj = os.listdir(caminho)
    return listaObj

def convertJs(objList,caminho):
    ''' Fun��o responsavel por executar a intera��o dentro da lista do diret�rio,
        Caso o elemento da lista for .obj converte para .js. '''
    for i in objList:
        indice = i.index(".")
        if(i[indice:] != '.obj'):
            print "\nArquivo Invalido"
        else:
            comando = "convert_obj_three.py -i " + caminho + i + " -o " + "json/" + i[:indice] + ".js" 
            os.system(comando)
            print "\nConversao realizada com sucesso."
    
main()
