#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:04:46 2018

@author: pedrocampelo
"""

    import numpy as np  
    import matplotlib.pyplot as plt  
    import os

    
    
    
    
                #GRAFICO 1: Utilidade
    #RM
    x1 = np.linspace(0.001,3)
    y1= 1/x1
        
    x2 = np.linspace(0,2)
    y2 = -x2 + 2
    
    x3=np.linspace(0.001,4)
    y3= 1/x**(0.5)
    
    x4 = np.linspace(0,3)
    y4 = -(1/2)*x4 + (3/2)
   
    xp1 = (1)
    yp1 = (1) 
    
    xv1=[1,1,1,1]
    yv1=[0,0.25,0.5,1]
    

    xv2=[0,0.25,0.5,1]
    yv2=[1,1,1,1]
    
    fig2, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 7))
    axes[0].axis([-0.5, 4, -0.1, 2.5])
    axes[0].axis('off')
    axes[0].axhline(0, color='black')
    axes[0].axvline(0, color='black')
    axes[0].plot(x1, y1, color='red')
    axes[0].plot(x2, y2, color='black')
    axes[0].plot(xp1, yp1, 'ro')
    axes[0].plot(xv1, yv1, 'r--', color='black')
    axes[0].plot(xv2, yv2, 'r--', color='black') 
    axes[0].text( 3.1,0.3, '$U_1(x,y)$')
    axes[0].text( 2.5,-0.1, '$x_1$')
    axes[0].text(-0.5,2.4, '$x_2$')
    axes[0].text( 1.2,1, '$(x,y)=(1,1)$')
    axes[0].text( -0.8,2, '$TMS_1$')
    axes[0].text( 2,1.5, '$TMS_1= 1$') 
    axes[0].text(2,1.6, r'$\alpha = \beta$')
 
    axes[1].axis([-0.5, 4, -0.1, 2.5])
    axes[1].axis('off')
    axes[1].axhline(0, color='black')
    axes[1].axvline(0, color='black')
    axes[1].plot(x3, y3, color='red')
    axes[1].plot(x4, y4, color='black')
    axes[1].plot(xp1, yp1, 'ro')
    axes[1].plot(xv1, yv1, 'r--', color='black')
    axes[1].plot(xv2, yv2, 'r--', color='black') 
    axes[1].text( 4.1,0.5, '$U_2(x,y)$')
    axes[1].text( 2.7,-0.1, '$x_1$')
    axes[1].text(-0.5,2.4, '$x_2$')
    axes[1].text( 1.2,1, '$(x,y)=(1,1)$')
    axes[1].text( -0.8,1.5, '$TMS_2$')
    axes[1].text( 2,1.5, '$TMS_2<1$')
    axes[1].text(2,1.6, r'$\alpha < \beta$')


    fig2.tight_layout()

    
    
    
    
    
    
    
    #GRAF 2 - Função benefício
    
    #RM
    x5 = np.linspace(0.001,3)
    y5= 1/x5
    
    x6=np.linspace(0.001,3)
    y6= 3/x6
    
    x4 = np.linspace(0,3)
    y4 = x4 
   
    xp1 = (1)
    yp1 = (1) 
    
    xp2 = (1.5)
    yp2 = (2) 
    
    xv1=[1,1,1,1]
    yv1=[0,0.25,0.5,1]
    
    xv2=[0,0.25,0.5,1]
    yv2=[1,1,1,1]
    
    xv3=[1.5,1.5,1.5,1.5,1.5,1.5]
    yv3=[0,0.375,0.75,1,1.5,2]
    
    xv4=[0,0.5,1,1.5]
    yv4=[2,2,2,2]
    
   
    #Graf-1
    plt.axis([-0.3, 3.5, -0.3, 4])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    #plt.plot(x4, y4, color='red')
    plt.plot(x5, y5, color='red') 
    plt.plot(x6, y6, color='red')
    plt.plot(xp1, yp1, 'ro')
    plt.plot(xp2, yp2, 'ro')
    plt.plot(xv1, yv1, 'r--', color='black')
    plt.plot(xv2, yv2, 'r--', color='black') 
    plt.plot(xv3, yv3, 'r--', color='black')
    plt.plot(xv4, yv4, 'r--', color='black')     
    plt.annotate('.', xy=(1.5,2), xytext=(1, 1),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             ) 
    plt.grid()
    plt.text(-0.2, 3.5, '$y$')
    plt.text(3.4, -0.2, '$x$')
    plt.text(0.9, -0.3, r'$\overline{x}$')
    plt.text(-0.2, 1, '$\overline{y}$')
    plt.text(1.4, -0.3, r'$\overline{x} + \alpha x_0$')
    plt.text(-0.5, 2, r'$\overline{y} + \alpha y_0$')
    plt.text(3.1,0.3, '$U(\overline{x},\overline{y})$')
    plt.text(3.1,1, r'$U(\overline{x} + \alpha x_0,\overline{y} + \alpha y_0)$')
    plt.text(2,3, r'$ \alpha > 0$')
    plt.axis('off')



    #Graf-2
    plt.axis([-0.3, 3.5, -0.3, 4])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    #plt.plot(x4, y4, color='red')
    plt.plot(x5, y5, color='red') 
    plt.plot(x6, y6, color='red')
    plt.plot(xp1, yp1, 'ro')
    plt.plot(xp2, yp2, 'ro')
    plt.plot(xv1, yv1, 'r--', color='black')
    plt.plot(xv2, yv2, 'r--', color='black') 
    plt.plot(xv3, yv3, 'r--', color='black')
    plt.plot(xv4, yv4, 'r--', color='black')     
    plt.annotate('.', xy=(1,1), xytext=(1.5,2),
                 arrowprops=dict(facecolor='black', shrink=0.15),
             )
    plt.grid()
    plt.text(-0.2, 3.5, '$y$')
    plt.text(3.4, -0.2, '$x$')
    plt.text(0.8, -0.3, r'$\overline{x}+ \alpha x_0$')
    plt.text(-0.5, 1, r'$\overline{y}+ \alpha y_0$')
    plt.text(1.55, -0.3, r'$\overline{x} $')
    plt.text(-0.2, 2, r'$\overline{y} $')
    plt.text(3.1,0.3, r'$U(\overline{x} + \alpha x_0,\overline{y} + \alpha y_0)$')
    plt.text(3.1,1, r'$U(\overline{x},\overline{y})$')
    plt.text(2,3, r'$ \alpha < 0$')
    plt.axis('off')
    #plt.axis('off')


