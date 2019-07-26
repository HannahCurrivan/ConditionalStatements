# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:19:36 2019

@author: hcurrivan
"""

#You are looking for a fuel with a specific impulse of 289 Isp.
specific_impulse = 289
specific_impulse_2 = 356

if specific_impulse >= 289:
    print("This is greater than specific impulse that the engine needs.")
    
    if specific_impulse_2 == 256:
        print("Fuel type needed for a 256 Specific Impulse is Kerosene")
        
    else: 
        print("This fuel is incapable to give the specific impulse needed to launch such rocket.")
    
elif specific_impulse == 320:
    print("This means you can use Kerosene with the Specific Impulse of 320.")
    
else:
    print("Fuel type needed for a 289 Specific Impulse is Kerosene")
    

    

