import math_lib
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

print ('Division {}/{}={}:'.format(a, b, math_lib.div(a, b)))
print ('Addition {}+{}={}:'.format(a, b, math_lib.add(a, b)))
print ('Subtraction {}-{}={}:'.format(a, b, math_lib.substract(a, b)))

