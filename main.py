# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:20:29 2021

@author: faous
"""

import numpy as np

import matplotlib.pyplot as plt
import os
import fonctions

images = "C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD2/FG2/"
image = "C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD1/FG1/"

M, Z, Pk = fonctions.Apprentissage(images)

fonctions.ajout(image,M,Pk,Z)

Min = fonctions.reconaissance(image,M,Pk,Z,images)