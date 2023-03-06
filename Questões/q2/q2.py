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
imgname = "bandeiras.png"

if __name__ == "__main__":

    frame = cv2.imread(imgname)
    
    # Our operations on the frame come here
    img = frame.copy()
    
    # NOTE que em testes a OpenCV 4.0 requereu frames em BGR para o cv2.imshow
    cv2.imshow('Input', frame)
    cv2.imshow('Output', img)

    cv2.waitKey()
    cv2.destroyAllWindows()

