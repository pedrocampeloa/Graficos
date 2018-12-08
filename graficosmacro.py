#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:04:46 2018

@author: pedrocampelo
"""

    import numpy as np  
    import matplotlib.pyplot as plt  
    import os


                #GRAFICO 1: IS (taxa de juros constante)


    x1 = np.linspace(0.5,7.5)
    x2 = np.linspace(2.5,10)    
    y1 = (-4/3)*x1 + 12
    y2 = (-4/3)*x2 + 20
    
    xp1 = 4
    yp1 = 20/3  
 
    xp2=6
    yp2=12   

    xv1 = [4,4,4,4,4]
    yv1 = [0,(5/3),(10/3),(15/3),(20/3)]    
    xv2 = [0,1,2,3,4] 
    yv2 = [(20/3),(20/3),(20/3),(20/3),(20/3)]
  
    xv3 = [6,6,6,6,6]
    yv3=[0,3,6,9,12]
    xv4 = [0,1,2,3,4,5,6] 
    yv4 = [12,12,12,12,12,12,12]
        
    plt.axis([-1, 14, -2, 18])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot(x1, y1, color='red') 
    plt.plot(x2, y2, color='red') 
    plt.plot(xp1, yp1, 'ko') 
    plt.plot(xp2, yp2, 'ko') 
    plt.plot(xv1, yv1, 'r--', color='black')
    plt.plot(xv2, yv2, 'r--', color='black') 
    plt.plot(xv3, yv3, 'r--', color='black')
    plt.plot(xv4, yv4, 'r--', color='black') 
    plt.text(10.5, 7, '$IS_2$')
    plt.text(8, 2, '$IS_1$')
    plt.text(3.5, -1, '$Y_1$')
    plt.text(5.5, -1, '$Y_2$')
    plt.text(11, -1, 'Produto (Y)')
    plt.text(-2, 16, 'Taxa de')
    plt.text(-2, 15, 'Juros (r)')
    plt.text(-1, (20/3), '$r_1$')
    plt.text(-1, 12, '$r_2$')    
    plt.annotate('.', xy=(9,8), xytext=(7, (8/3)),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             )     
    plt.annotate('.', xy=(3,16), xytext=(1, (32/3)),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             )    
    plt.xlabel('Produto')
    plt.axis('off')
    #plt.grid()    
    plt.show()



                #GRAFICO 2: CP X RM

    #RM
    x3 = np.linspace(0.5,8)
    y3 = (-4/3)*x3 + 12
    
    #CP1
    x4 = np.linspace(0.5,8)
    y4 = (4/3)*x4 + (4/3)
    
    #CP2
    x5 = np.linspace(4.2,11.5)
    y5 = (4/3)*x5 - 4
    
    xp3 = 4
    yp3 = 20/3
 
    xp4=6
    yp4=4   

    xv5 = [4,4,4,4,4,4,4,4,4,4,4,4,4]
    yv5 = list(range(13)) 
  
    xv6 = [6,6,6,6,6,6,6,6,6,6,6,6,6]
    yv6 = list(range(13)) 
    
    xv7 = [0,1,2,3,4] 
    yv7 = [(20/3),(20/3),(20/3),(20/3),(20/3)]
    
    xv8 = [0,1,2,3,4,5,6] 
    yv8 = [4,4,4,4,4,4,4]

        
    plt.axis([-1, 14, -2, 18])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot(x3, y3, color='blue')
    plt.plot(x4, y4, color='green')
    plt.plot(x5, y5, color='green')
    plt.plot(xp3, yp3, 'ko') 
    plt.plot(xp4, yp4, 'ko') 
    plt.plot(xv5, yv5, color='black')
    plt.plot(xv6, yv6, color='black')
    plt.plot(xv7, yv7, 'r--', color='black')
    plt.plot(xv8, yv8, 'r--', color='black')
    plt.text(8.2, 1.3, '$RM$')
    plt.text(8.5, 11.3, '$CP_1$')
    plt.text(11.8, 11, '$CP_2$')
    plt.text(3.5, -1, '$Y_1$')
    plt.text(5.5, -1, '$Y_2$')
    plt.text(4, 12.5, '$Y^{P}_1$')
    plt.text(6,12.5, '$Y^{P}_2$')
    plt.text(11, -1, 'Produto (Y)')
    plt.text(-2, 16, 'Taxa de')
    plt.text(-2, 15, 'Inflação')
    plt.text(-1.5, 14, '($\pi$)')
    plt.text(-1.5, (20/3), '$\pi_1$')
    plt.text(-1.5, 4, '$\pi_2$')

    plt.annotate('.', xy=(6,10), xytext=(4, 10),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             )  
    plt.annotate('.', xy=(9,8), xytext=(7, (32/3)),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             )    
    plt.axis('off')
    #plt.grid()    
    plt.show()





    def y1(x): 
        return (4/3)*x -4
    
    #CP2
    x5 = np.linspace(4.2,11.5)
    y5 = (4/3)*x5 - 4
