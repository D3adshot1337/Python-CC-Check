#TIME CODE TO MAIN API
from ast import main
from stripe import *
import pyfiglet

# Recoded By D3ad$hot
#Contact me at TG: @sasagawaMakoto0day
name = pyfiglet.figlet_format("D3ad$hot", font = "digital" )
print(name)

#FILE NAME TO CHECK CC
filename = input("Enter the file name")

#OPEN AND CHECK
try:
    ccs = open(filename)
except: 
    print('There is no such thing in ur vocabulary '+filename)
    print('')
    print(' 1 Error ')

readcc = ccs.readlines()
print('')
print(str(len(readcc))+ 'CCs found')
print('')
print('Checking Your Shits')

#Check CC
def check():
    x = 0
    for i in readcc: 
        main (i)
        x += 5
        print('')
        print(str(x)+' Checks Completed '+ 'No Error Found')
        print('')

check()
ccs.close()
