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

## Inicio dos valores de conferencia
## USe isto para testar seu programa

simples = cv2.imread("cruz_branca_negra_simples.png")
simples = cv2.cvtColor(simples, cv2.COLOR_BGR2GRAY)

check1_brancas_simples = [(4, 10), (8, 10), (12, 10), (16, 10), (20, 10)]
check1_negras_simples = [(4, 20), (8, 20), (12, 20), (16, 20), (20, 20)]


brancas_negras = cv2.imread("cruz_branca_negra_simples.png")
brancas_negras = cv2.cvtColor(brancas_negras, cv2.COLOR_BGR2GRAY)

check2_brancas = [(4, 3), (4, 15), (8, 3), (8, 15), (12, 3), (12, 15), (16, 3), (16, 15), (20, 3), (20, 15)]
check2_negras =  [(4, 6), (4, 12), (8, 6), (8, 12), (12, 6), (12, 12), (16, 6), (16, 12), (20, 6), (20, 12)]
check2_brancasnegras = [(4, 3), (8, 3), (12, 3), (16, 3), (20, 3)]
check2_negrasbrancas = [(4, 12), (8, 12), (12, 12), (16, 12), (20, 12)]


quad = cv2.imread("exemplo_quadrante_75_100_125_150.png")
quad = cv2.cvtColor(quad, cv2.COLOR_BGR2GRAY)


# Valores para dentro da região cinza 75

brancas75 =[(5, 5), (5, 17), (9, 5), (9, 17), (13, 5), (13, 17)]
negras75 = [(5, 8), (5, 14), (9, 8), (9, 14), (13, 8), (13, 14)]
brancasnegras75 = [(5, 14), (9, 14), (13, 14)]
negrasbrancas75 = [(5, 5), (9, 5), (13, 5)]


# Valores para dentro da região cinza 100

brancas100 =[(5, 27), (5, 39), (9, 27), (9, 39), (13, 27), (13, 39)]

negras100 = [(5, 30), (5, 36), (9, 30), (9, 36), (13, 30), (13, 36)]

brancasnegras100 = [(5, 36), (9, 36), (13, 36)]

negrasbrancas100 = [(5, 27), (9, 27), (13, 27)]


# Valores para dentro da região cinza 125

brancas125=[(27, 5), (27, 17), (31, 5), (31, 17), (35, 5), (35, 17), (39, 5), (39, 17)]
negras125 =  [(27, 8), (27, 14), (31, 8), (31, 14), (35, 8), (35, 14), (39, 8), (39, 14)]
brancasnegras125 = [(27, 14), (31, 14), (35, 14), (39, 14)]
negrasbrancas125  = [(27, 5), (31, 5), (35, 5), (39, 5)]

# Valores para dentro da região cinza 150

brancas150 =[(27, 27), (27, 39), (31, 27), (31, 39), (35, 27), (35, 39), (39, 27), (39, 39)]
negras150 = [(27, 30), (27, 36), (31, 30), (31, 36), (35, 30), (35, 36), (39, 30), (39, 36)]
brancasnegras150 = [(27, 36), (31, 36), (35, 36), (39, 36)]
negrasbrancas150 = [(27, 27), (31, 27), (35, 27), (39, 27)]

# Fim dos valores de conferencia



teste1 = cv2.imread("q1_final_v1.png")
teste2 = cv2.imread("q1_final_v2.png")

frames = [teste1, teste2]




# Trabalhe nesta função
# Pode criar e chamar novas funções o quanto quiser
def processa(frame_gray): 
    
    l_brancas = []
    l_negras = []
    l_brancas_negras = []
    l_negras_brancas = []
    
    color = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)        
    
    return l_brancas, l_negras, l_brancas_negras, l_negras_brancas, color

## Adicionados DEPOIS da prova para melhorar a clareza

def resize_big(img, scale):
    """ Resizes a grayscale image"""
    out_size = np.array(img.shape)*int(scale)
    print(img.shape, out_size)
    return cv2.resize(src=img, dsize=tuple(out_size), interpolation=cv2.INTER_NEAREST)

def resize_big_color(img, scale):
    """ Resizes a grayscale image"""
    out_size = np.array(img.shape)*int(scale)
    out_size = out_size[:-1]
    print(img.shape, out_size)
    return cv2.resize(src=img, dsize=tuple(out_size), interpolation=cv2.INTER_NEAREST)


if __name__ == "__main__":

    # Inicializa a leitura dos arquivos
    bgr = frames
    
    print("Se a janela com a imagem não aparecer em primeiro plano dê Alt-Tab")

    print("No código-fonte há imagens de testes com GABARITOS. Temos também um notebook de rascunho na pasta")


    for frame in bgr: 
        # Capture frame-by-frame

        # Our operations on the frame come here
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Você vai trabalhar na função processa!
        brancas, negras, l_brancas_negras, l_negras_brancas, saida_color = processa(gray)

        
        saida_color = resize_big_color(saida_color, 4)
        # NOTE que em testes a OpenCV 4.0 requereu frames em BGR para o cv2.imshow
        cv2.imshow('imagem processada', saida_color)

        if cv2.waitKey(1500) & 0xFF == ord('q'):
            break



