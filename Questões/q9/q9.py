#!/usr/bin/python3
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
videos = [
    "attempt1.mp4",
    "attempt2.mp4",
    "attempt3.mp4"
]

def meteoro_acertou(bgr):
    """
    Identifica se o meteoro acertou o personagem e imprime  resposta na imagem,
    junto com os bounding boxes e imprimir as profundidades no terminal
    """ 

    img = bgr.copy()
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    # Você deverá trabalhar aqui

    return img


if __name__ == "__main__":

    for video in videos:
        # Inicializa a aquisição da webcam
        cap = cv2.VideoCapture(video)

        print("Se a janela com a imagem não aparecer em primeiro plano dê Alt-Tab")

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            if ret == False:
                #print("Codigo de retorno FALSO - problema para capturar o frame")
                #cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break

            # Our operations on the frame come here
            img = meteoro_acertou(frame.copy())

            # NOTE que em testes a OpenCV 4.0 requereu frames em BGR para o cv2.imshow
            cv2.imshow('Input', frame)
            cv2.imshow('Output', img)

            # Pressione 'q' para interromper o video
            if cv2.waitKey(1000//30) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

