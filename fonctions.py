# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:37:12 2021

@author: faous
"""

import numpy as np

import matplotlib.pyplot as plt
import os

def Apprentissage(images):


    X=[]
    path = os.listdir(images)
    for i in range(0,100):
         image=plt.imread(images + path[i])
         image=np.resize(image,4096)
         X.append(image)
     
    "Normalisation de X"    
    
    "les moyennes des colonnes"
    moyennes=np.mean(X,0)
     
    "Les ecarts type des colonnes"
    ecarts_type=np.std(X,0)
    
    M=[]
    M.append(moyennes)
    M.append(ecarts_type)
    
    Y=(X-moyennes)/ecarts_type     
         
    "Question 4"
    "Décomposition en valeurs singulières"
    
    [U,S,Vt]=np.linalg.svd(Y,full_matrices= False)
    
    S=np.diag(S)
    
    "determination de P et D d'après la question 4 partie 3"
    P=np.transpose(Vt)
    D=np.dot(np.transpose(S),S)
    
    "Question 5"
    "colonnes à retenir (tester k entre 50 et 70"
    
    "Inertie totale"
    I=np.trace(D)
    
    "on teste des valeurs entre 50 et 70"
    for i in range (50,71) :
        Dk=D[:,0:i]
        Ik=np.trace(Dk) 
        proportion=Ik/I
        if proportion >=0.95 :
            k=i
            break
    Pk=P[:,0:k]
    """on fixe un seuil à 95% donc les k premières colonnes doivent expliquer au 
     moins 95% de la variance. Mais on veut une réduction de dimensions, donc on 
     prend le plus petit k qui donne une proportion >=95% """
        
    
    "détermination de Z"
    
    Z=np.dot(Y,Pk)
        
    return M, Z, Pk

"Fonction ajout"

def ajout(image,M,Pk,Z):
    
    path = os.listdir(image)
    xm=plt.imread(image + path[2])
    xm=np.resize(xm,4096)
    ym=(xm-M[0])/M[1]  
    zm=np.dot(ym,Pk)
    np.append(Z,zm)
    
"""On rajoute en entreé images pour pouvoir afficher l'image correspondante
 dans notre BDD images """
def reconaissance(image,M,Pk,Z,images):
    path = os.listdir(image)
    img=plt.imread(image + path[4])
    
    xm=np.resize(img,4096)
    ym=(xm-M[0])/M[1]
    zm=np.dot(ym,Pk)
    d=[]
    for x in Z:
        diff=zm-x
        dist=np.linalg.norm(diff,2)   
        d.append(dist)

    min=np.argmin(d)
    
    path = os.listdir(images)        
    imagess=plt.imread(images + path[min])
         
    plt.figure()
    plt.imshow(imagess)
    plt.figure()
    plt.imshow(img)
    
    return min

    