#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este NÃO é um programa ROS

from __future__ import print_function, division 

import cv2
import os,sys, os.path
import numpy as np

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())

# Arquivos necessários
video = "../../robot20/media/lines.mp4"

def check_exists_size(name, size):
    """
        Função para diagnosticar se os arquivos estão com problemas
    """
    if os.path.isfile(name):
        stat = os.stat(name)
        print("Informações do arquivo ", name, "\n", stat)
        if stat.st_size !=size:
            print("Tamanho errado para o arquivo ", name, " Abortando ")
            mensagem_falta_arquivos()
            sys.exit(0)
    else:
        print("Arquivo ", name, " não encontrado. Abortando!")
        mensagem_falta_arquivos()
        sys.exit(0)

def mensagem_falta_arquivos():
    msg = """ls
    ls

    Tente apagar os arquivos em robot20/ros/exemplos_python/scripts:
         MobileNetSSD_deploy.prototxt.txt
         MobileNetSSD_deploy.caffemodel
    Depois
        No diretório robot20/ros/exemplos_python/scripts fazer:
        git checkout MobileNetSSD_deploy.prototxt.txt
        Depois ainda: 
        git lfs pull 

        No diretório No diretório robot20/media

        Fazer:
        git lfs pull

        Ou então baixe os arquivos manualmente nos links:
        https://github.com/Insper/robot20/tree/master/ros/exemplos_python/scripts
        e
        https://github.com/Insper/robot20/tree/master/media
    """
    print(msg)

if __name__ == "__main__":


    # Checando se os arquivos necessários existem
    check_exists_size(video, 942014)

    # Inicializa a aquisição da webcam
    cap = cv2.VideoCapture(video)

    print("Se a janela com a imagem não aparecer em primeiro plano dê Alt-Tab")


    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if ret == False:
            #print("Codigo de retorno FALSO - problema para capturar o frame")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
            #sys.exit(0)

        cv2.imshow('imagem', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


