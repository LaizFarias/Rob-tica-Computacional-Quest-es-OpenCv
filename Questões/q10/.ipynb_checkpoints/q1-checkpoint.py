#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este NÃO é um programa ROS

from __future__ import print_function, division 

import cv2
import os,sys, os.path
import numpy as np
import math

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())

# Arquivos necessários
video = "padrao.mp4"

## Trecho trazido do notebook com a explicação

#Fonte para escritas da opencv
font = cv2.FONT_HERSHEY_COMPLEX_SMALL    

    
def crosshair(img, point, size, color):
    """ Desenha um crosshair centrado no point.
        point deve ser uma tupla (x,y)
        color é uma tupla R,G,B uint8
    """
    x,y = point
    cv2.line(img,(x - size,y),(x + size,y),color,2)
    cv2.line(img,(x,y - size),(x, y + size),color,2)
    
def texto(img, a, p, thick=1,sz=1 ):
    """Escreve na img RGB dada a string a na posição definida pela tupla p"""
    cv2.putText(img, str(a), p, font,sz,(0,50,100),thick,cv2.LINE_AA)
      

def center_of_contour(contorno):
    """ Retorna uma tupla (cx, cy) que desenha o centro do contorno"""
    M = cv2.moments(contorno)
    # Condição inicial
    if M["m00"] == 0:
        M["m00"] = 1
    # Usando a expressão do centróide definida em: https://en.wikipedia.org/wiki/Image_moment
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])    
    return (int(cX), int(cY))



def centro_maior_contorno(mask):
    """Retorna uma tupla com (x,y) do centro do maior contorno da imagem binária passada como entrada.
        Retorna também o contorno para plot
    """
    contornos, arvore = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maior = -1.0
    maior_c = None
    for c in contornos:            
        a = cv2.contourArea(c) # área
        if a > maior:
            p = center_of_contour(c) # centro de massa
            maior = a
            maior_c = c    
    return p,maior_c

def dist(p0, p1):
    """Retorna a distância entre duas tuplas (x,y)"""
    dx = p0[0] - p1[0]
    dy = p0[1] - p1[1]
    return math.sqrt(math.pow(dx,2) + math.pow(dy, 2))

def middle(p0, p1):
    p = p0
    t = p1
    return (int((p[0]+t[0])/2.0), int((p[1]+t[1])/2.0))

def processa_dist(frame_bgr, f, H):
    """ Recebe um frame BGR e mede a distância em pixels entre os círculos verde e amarelo presentes na imagem"""            
    
    # Isolating the yellow circle
    ret, y = cv2.threshold(frame_bgr[:,:,2], 230, 255, cv2.THRESH_BINARY) # Veja https://github.com/mirwox/revisao2020
    img = frame_bgr.copy()
    
    # isolating the green circle
    g_in = img[:,:,1]&(~img[:,:,2])
    ret,g = cv2.threshold(g_in, 230, 255, cv2.THRESH_BINARY) 

    # creation of an image for display purposes
    or_img = y|g
    or_bgr = cv2.cvtColor(or_img, cv2.COLOR_GRAY2BGR)
    
    # Finding the contours
    centro_yellow,cont_yellow  = centro_maior_contorno(y)
    centro_green, cont_green = centro_maior_contorno(g)
    
    # Drawing the centers
    crosshair(or_bgr, centro_yellow, 5, (0,0,255))
    crosshair(or_bgr, centro_green, 5, (0,0,255))    
    
    # Drawing contours
    cv2.drawContours(or_bgr, [cont_yellow], -1, [0, 255, 255], 2);    
    cv2.drawContours(or_bgr, [cont_green], -1, [0, 255, 0], 2);        
    
    # Drawing labels
    font = cv2.FONT_HERSHEY_SIMPLEX    
    texto(or_bgr, "Amarelo", centro_yellow)
    texto(or_bgr, "Verde", centro_green)
    
    # Drawing a line between the 2 points
    cv2.line(or_bgr,centro_yellow,centro_green,(0,0,230), 1)
    
    # calculate measurements
    h = dist(centro_yellow,centro_green)
    texto(or_bgr, "h = {:2.1f}".format(h), middle(centro_yellow, centro_green))        
    
    # Computing distance D
    D = f*H/h
    
    texto(or_bgr, "D={:2.3f}m".format(D), (100,100), thick=1, sz=3 )        
    
    
    
    return or_bgr   

## Fim do trecho trazido do notebook


if __name__ == "__main__":

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

        # Our operations on the frame come here
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        out = processa_dist(frame, f=1190, H=0.1)


        # NOTE que em testes a OpenCV 4.0 requereu frames em BGR para o cv2.imshow
        cv2.imshow('Entrada', frame)
        cv2.imshow('Resposta', out)
        # moveWindow usado para uma janela não se sobrepor à outra
        cv2.moveWindow('Resposta', 300, 250)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


