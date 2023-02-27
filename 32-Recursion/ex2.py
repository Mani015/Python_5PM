#
import sys
# # sys:The sys modules provieds accesss to the system specific parameter and function
# print('Capcity of interpreter:',sys.getrecursionlimit())
# Capcity of interpreter: 1000




sys.setrecursionlimit(20)

def f1():
    print('fucntion')
    f1()
f1()




