#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re


# In[15]:



print('Magic Calculator')
print('type quit to EXIT\n')

previous = 0
run = True
name = input('Enter Your Name:')

def performMath():
    global run
    global previous
    global name
    equation=""
    if previous == 0:
        equation = input('Enter Equation:')
    else:
        equation = input(str(previous))
    try:
        if equation == 'quit':
            print("goodbye, {}".format(name))
            run = False
        else:
            equation = re.sub('[a-zA-Z,.:()" "]','', equation)
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
            print('you typed {}'.format(previous))
    except SyntaxError:
        print('tolong masukan angka')
        
while run:
    performMath()


# In[ ]:




