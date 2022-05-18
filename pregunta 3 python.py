# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyswip import Prolog
abuelo = Prolog()
abuelo.assertz("abuelo(juan, maria)")
abuelo.assertz("abuelo(juan, julio)")
list(abuelo.query("padre(juan,X)")) == [{"X":"maria"},{"Y":"julio"}]
primos = ""
for e in abuelo.query("padre(X,Y)"):
    print(e["X"], "es el abuelo de ", e["Y"])
    print(e["Y"], "es el nieto de ", e["X"])
    primos = primos+ e["Y"]+ ", "
print(primos + "son primos")