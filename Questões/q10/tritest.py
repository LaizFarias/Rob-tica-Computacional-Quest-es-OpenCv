#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este NÃO é um programa ROS

from __future__ import print_function, division 

import cv2
import os,sys, os.path
import numpy as np

import triutil

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())

# Arquivos necessários
video = "triangulos.mp4"


if __name__ == "__main__":

    print("Se a janela com a imagem não aparecer em primeiro plano dê Alt-Tab")

    n = 100

    a = (200, 500)
    b = (600, 500)
    c = (400, 100)

    w = 800
    h = 600


    while(True):

        img = triutil.make_empty()
        triutil.plot_tri(img,a,b,c)

        inside = (0,0,255) # cor para mostrar pontos dentro
        outside = (0,255, 0) # cor para mostrar pontos fora

        for i in range(n):
            # Sorteia um ponto aleatório
            p = triutil.random_point(w,h)
            # Testa se o ponto sorteado está dentro do triângulo
            if triutil.point_in_triangle(a,b,c, p):
                triutil.crosshair(img, p, 3, inside)
            else:
                triutil.crosshair(img, p, 3, outside)
        
        cv2.imshow('Teste do triutil', img)


        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cv2.destroyAllWindows()


