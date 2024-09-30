# virus making in python, basic to advanced

""" Screen Rotataing Virus """
""" if requirements.txt not responding then run the following command """

# import elements (core for installation and other)
import os
import time

# clear screen

os.system('clear')


# import elements


import rotatescreen as rs
import time as t

# main code


pd = rs.get_primary_display()

for i in range(5):
    angle_list = [90,180,270,0]
    for x in angle_list:
        pd.set_landscape_flipped(angle_list)
        t.sleep(0.5)

