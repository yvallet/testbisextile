# annee bisextile
import math
import os
import sys

if 'PYTHONPATH' in os.environ:
    print ("PYTHONPATH :" , os.environ['PYTHONPATH'])

else:
    print ("pas defini")

os.environ['PYTHONPATH'] = 'C:\\Users\\yvall\\PycharmProjects\\test1;C:\\Users\\yvall\\PycharmProjects\\test1\\venv'
print("PYTHONPATH :", os.environ['PYTHONPATH'])

from outil_yv  import *

# poir executer en mode commande sous windows :
# set PYTHONPATH=C:\Users\yvall\PycharmProjects\test1;C:\Users\yvall\PycharmProjects\test1\venv

# sys.path=sys.path + str("C:\\Users\\yvall\\PycharmProjects\\test1") + str("C:\\Users\\yvall\\PycharmProjects\\test1\\vevn")
# papath=sys.path + str("C:\\Users\\yvall\\PycharmProjects\\test1") + str("C:\\Users\\yvall\\PycharmProjects\\test1\\vevn")
# test = sys.path
# test = test + str("C:\\Users\\yvall\\PycharmProjects\\test1")
# print (test)

""" ## <== fonction dans outil_yv
def verif_num(var):
    for i in var:
        if i < "0" or i > "9":
            print("entree invalide, non numerique !")
            return False
        return True
"""

# ajout   aaa bb
#

var = "hello world"
x=type(var)
print ("ca marche",var)
print(x)

a=16
print ("a: ", a,   " racine carre ede a : ", math.sqrt(a))

## annee bisextile
## Non si pas divisible par 4   + exceptions : divisible par 100 , sauf 400=OK

numerique = False
annee = 0
while numerique is False:
    try:
        annee = input("annee: ")
        numerique = verif_num(annee)
        if numerique == False:
            continue
        annee = int(annee)
        if annee < 1001:
            raise ValueError("l'annee doit etre superieure a 1000 !")
    except:
        print ("annee : valeur incorrecte ")
        numerique = False


if annee % 4 != 0 :
    print ("annee ", annee, "Non bisextile")
else:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print ("BISEXTILE , divisibla par 400")
        else:
            print ("div par 100 : NON")
    else:
        print ("OK, div par 4 et non 100")

##Correction
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'annÃ©e saisie est bissextile.")
else:
    print("L'annÃ©e saisie n'est pas bissextile.")


##input avec try
aa = 0
while True:
    annee = input("annee : ")
    try:
        aa = int(annee)   # si annee non NUM, leve automatiquement 1 exception
        if aa < 1001:
            # levee volontaire
            raise()
        else:
            break
    except:
        print ("saisie fausse , doit etre Numerique, Superieur a  1000")
        continue

print ("aa :", aa)

os.system("pause")

