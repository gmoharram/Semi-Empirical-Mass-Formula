# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 01:35:25 2020

@author: gmoha
"""
import matplotlib.pyplot as plt


def isotopeBindingEnergy(A,Z):
    
    
    
    a_v = 15.85  #MeV
    a_s = 18.34 
    a_c = 0.71
    a_a = 92.84
    a_p = 12
    
    vol_term = a_v * A
    surf_term = - a_s * A**(2/3)
    coul_term = - a_c * ((Z**2 - Z)/(A**(1/3)))
    assym_term = - a_a * (Z - A/2)**2/A
    
    n1 = A%2 #0 if A even, 1 if odd
    n2 = Z%2
    delta = ((-1)**n1 + (-1)**n2)/2 # 1 if both even, -1 if both odd, 0 else
    pair_term = delta*a_p/A**(1/2) #

    return vol_term + surf_term + coul_term + assym_term + pair_term

def bindingPerNucleus(A,Z):
    return isotopeBindingEnergy(A,Z)/A

def plotIsobars(A):
    E = []
    for i in range(1,A):
        E.append(isotopeBindingEnergy(A,i))
    plt.plot(E, 'x')
    plt.ylabel('Binding Energy')
    plt.show
    
    
    