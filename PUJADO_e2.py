# filename    : Maria.e2.py
# author      : Maria Angelica Pujado
# description : 2 activity

import sys
sustained_winds = sys.argv[1]
sustained_winds = float (sustained_winds)

if sustained_winds >= 220.0:
    print ("Super Typhoon")
elif sustained_winds >= 110.0:
    print ("Typhoon")
else:
    print("I dont know")