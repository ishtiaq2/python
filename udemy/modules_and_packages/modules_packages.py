#Modules: a py script used by other pyscripts
#Pacakages: a collection of Modules

#pip install colorama
#pip install openpyxl # for excel

from colorama import init
init()
from colorama import Fore 


print (Fore.RED + 'some red text')

def my_func():
    print ('I am a function in a modules')