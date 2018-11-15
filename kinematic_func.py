# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:31:14 2018

@author: jieqiang
"""
import numpy as np

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

def three_agents(y, t, d_12, d_23, d_31):
    y_11, y_12, y_21, y_22, y_31, y_32 = y # three agents, six components
    beta_12 = np.linalg.norm([y_11-y_21, y_12-y_22])**2
    beta_23 = np.linalg.norm([y_21-y_31, y_22-y_32])**2
    beta_31 = np.linalg.norm([y_31-y_11, y_32-y_12])**2
    # let us denote the edge in this order 1=12, 2=23, 3=31
    rho_1 = np.true_divide((beta_12+d_12**2)*(beta_12-d_12**2),beta_12**2)
    rho_2 = np.true_divide((beta_23+d_23**2)*(beta_23-d_23**2),beta_23**2)
    rho_3 = np.true_divide((beta_31+d_31**2)*(beta_31-d_31**2),beta_31**2)
    
    dydt = [-(rho_1*(y_11-y_21)+rho_3*(y_11-y_31)),-(rho_1*(y_12-y_22)+rho_3*(y_12-y_32)),\
            -(rho_2*(y_21-y_31)+rho_1*(y_21-y_11)),-(rho_2*(y_22-y_32)+rho_1*(y_22-y_12)),\
            -(rho_3*(y_31-y_11)+rho_2*(y_31-y_21)),-(rho_3*(y_32-y_12)+rho_2*(y_32-y_22))]
    return dydt