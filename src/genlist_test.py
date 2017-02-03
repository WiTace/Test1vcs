import random
def generate_list():
        alist = [x for x in range(random.radint(-10,10))]
        return alist
    """
    git print(generate_list)
    """
def printIt()
    print(generate_list())
    
def main():
    printIT()
    """
    If this scrit file is called, it will run main() directly
    """
    if _name_=='_main_':
        print("Test printIt():")
        main()
#! Insert the current directory path to Python path
import sys
import os
cwd = os.getced()

sys.path.append(cwd)
#print(sys.path)
#test the module: gqnerate_list
from generate_list import printIt()
printIt()
