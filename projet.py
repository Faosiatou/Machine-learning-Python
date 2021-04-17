# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import matplotlib.pyplot as plt
import os

"4)Phase d'apprenstissage"

" Question 1 et 2"
"Lecture et transformation dans une matrice ligne de taille 4096 "
images = os.listdir("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD1/FG1/")



X=[]
tab = []
for i in range(0,100) :
     image=plt.imread("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD1/FG1/" + images[i])
     tab.append(image)
     image=np.resize(image,4096)
     X.append(image)
     
"Question 3) création de la matrice Y"

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

Dk=D[:,0:5]

I1=np.trace(Dk)

proportion1=I1/I

"A partir de la 55ème valeur on a 95%"


P55=P[:,0:55]

"Question 6"
"détermination de Z"

Z=np.dot(Y,P55)

"Base de données en dimension réduite"

Xm=[]
for i in range(0,1680) :
     imag=plt.imread("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD1/FG1/" + images[i])
     imag=np.resize(imag,4096)
     Xm.append(imag)

     
"Normalisation de Xm"    
Ym=(Xm-M[0])/M[1]

"Zm qui donne les coordonnées"
Z=np.dot(Ym,P55)    

"Reconnaissance faciale"
"Question 1" 
"Rechercher un visage inconnu dans BDD1 ou BDD2"

images2 = os.listdir("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD2/FG2/")




"Construction d'une matirce formée d visages de la base de données BDD2"
X2=[]
for i in range(0,100) :
     image2=plt.imread("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD2/FG2/" + images2[i])
     image2=np.resize(image2,4096)
     X2.append(image2)
     
     
     

    
"Comparaison des lignes des matrices X2 ET X pour trouver un visage inconnu"

xm=[]
for i in Xm:
    a = i.tolist()
    xm.append(a)
    
x2=[]
for i in X2:
    a = i.tolist()
    x2.append(a)

xc = []
for i in range(0, 1680) :
    for j in range(0, 100) : 
       if xm[i] == x2[j] :
           print(xm[i])
           xc.append(xm[i])

"Choix d'une ligne"

xp=X2[90]

"Question 2 "
" Normalisation de xp et création de yp"

yp=(xp-M[0])/M[1]

"Question3"

"Coordonées de cette image dans la base des composantes principales retenues"

zp=np.dot(yp,P55)

"Question 4"

"Calcul des distances entre la nouvelle image et celles de la BDD "

di=[]
for i in range(0,1680):
    
    dist=zp-Z[i]
    d=np.linalg.norm(dist, 2)
    di.append(d)
    
"Question 5"

"Identification du visage par la recherche de la distance minimale"

dist_min =np.min(di)

indice_visage=np.argmin(di)
"le visage 90 de la BBD2 est proche au visage 626 de la BDD2"

w=plt.imread("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD1/FG1/" + images[626])
plt.figure()
plt.imshow(w)

G=plt.imread("C:/Users/faous/Desktop/eisti/semestre 2/TP Analyse numérique/BDD2/FG2/" + images2[90])
plt.figure()
plt.imshow(G)







    
    

            
    
    








    
     