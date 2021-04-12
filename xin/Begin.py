import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'./MyData')
sys.path.append(r'./MyUI')
import UI
from UI import *
#import Draw
#from Draw import draw
import GetData
from GetData import *

window = tk.Tk()
BuDemo(window)
window.mainloop()

'''
userdata = get_user_data()
for i in range(len(userdata)):
        print(userdata[i])
'''

