#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este NÃO é um programa ROS

from __future__ import print_function, division 

import cv2
import os,sys, os.path
import numpy as np
import random

def make_empty(w=800, h=600, color=(0,0,0)):
    """ Creates an empty image of width and height w and h and fills it with bg color"""
    img = np.zeros((h,w,3), dtype=np.uint8)
    cv2.rectangle(img, (0,0), (w,h), color, -1)
    return img

def crosshair(img, point, size, color=(255, 0, 0)):
    """ Desenha um crosshair centrado no point.
        point deve ser uma tupla (x,y)
        color é uma tupla R,G,B uint8
    """
    x,y = point
    cv2.line(img,(x - size,y),(x + size,y),color,1)
    cv2.line(img,(x,y - size),(x, y + size),color,1)
    
font = cv2.FONT_HERSHEY_SIMPLEX

def texto(img, a, p):
    """Escreve na img RGB dada a string a na posição definida pela tupla p"""
    cv2.putText(img, str(a), p, font,1,(0,50,100),2,cv2.LINE_AA)

def plot_tri(img, a,b,c, color=(255,0,0)):
    """Given image img and points a,b,c draws a triangle"""
    cv2.line(img, pt1=a,pt2=b, color=color, thickness=2)
    cv2.line(img, pt1=b,pt2=c, color=color, thickness=2)
    cv2.line(img, pt1=a,pt2=c, color=color, thickness=2)
    texto(img, "A", a)
    texto(img, "B", b)
    texto(img, "C", c)    
    
def random_point(lim_x, lim_y):
    """Generates a random point given limits lim_x and lim_y"""
    x = random.randint(0, lim_x)
    y = random.randint(0, lim_y)
    return x, y

def random_tri(lim_x, lim_y):
    """ Generates a random triangle inside limits lim_x and lim_y"""
    a = random_point(lim_x, lim_y)
    b = random_point(lim_x, lim_y)
    c = random_point(lim_x, lim_y)
    return a,b,c
 
def point_in_triangle(A,B,C,P):
    """ 
        Devolve True se o ponto P estiver dentro do triângulo definido pelos pontos A,B e C
        Reference: https://github.com/SebLague/Gamedev-Maths/blob/master/PointInTriangle.cs """
    x = 0
    y = 1
    s1 = C[y] - A[y]
    s2 = C[x] - A[x]
    s3 = B[y] - A[y]
    s4 = P[y] - A[y]
    w1 = (A[x] * s1 + s4 * s2 - P[x] * s1) / (s3 * s2 - (B[x]-A[x]) * s1)
    w2 = (s4- w1 * s3) / s1
    return w1 >= 0 and w2 >= 0 and (w1 + w2) <= 1
