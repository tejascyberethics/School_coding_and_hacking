# virus making in python, basic to advanced

""" Screen Rotataing Virus """


# import elements (core for installation and other)
import os
import time

# clear screen

os.system('clear')

# install packages


try:
    import rotatescreen
    print("Requirements satisfied")
except ImportError:
    os.system('pip install rotate-screen')



# import elements
import rotatescreen, time as rs


