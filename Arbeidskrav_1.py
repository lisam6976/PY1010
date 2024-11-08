# -*- coding: utf-8 -*-
"""
PY1010 - Arbeidskrav 1
Lisa Lindseth Samuelsen

@author: Lisa
"""

print("Kostnadar for bensinbil")
F = 7500 # [forsikring bensinbil]
print("F =", F)
T = 8.38 * 365 # [trafikkforsikringsavgift]
print("T =", T)
KM = 10000 # [km/år]
D = 1*KM # [pris på drivstoff]
print("D =", D)
B = 0.3*KM # [årleg bomavgift]
print("B =", B)
TK = F + T + D + B
print("TK =", TK) # [totalkostnad per år for bensinbil]

print("Kostnadar for elbil")
FE = 5000 # [forsikring elbil]
print("FE =", FE)
print("T =", T) # [trafikkforsikringsavgift]
S = (KM*0.2)*2 # [km ganger antall kwh per km, ganger 2 kroner per kwh er lik strømpris]
print("S =", S)
BE = 0.1*KM # [bomavgift for elbil]
print("BE =", BE)
TKE = FE + T + S + BE
print("TKE =", TKE)

print("kostnadsdifferanse")
K = TK - TKE # [kostnadsdifferanse]
print("K =", K)

print("Kostnadsdifferansen er 10500 kr, det er altå 10500 kr dyrare i året med bensinbil enn med elbil")

"""
Det kostar altså 10500kr mindre i året å køyre elbil enn besinbil. 
"""
