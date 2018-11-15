from operations import * 

a, b, c, d = (10, 5, 0, "Hello")

print( "{} + {} = {}".format(a, b, sumS(a, b) ) )
print( "{} - {} = {}".format(b, d, sub(b, d) ) )
print( "{} * {} = {}".format(b, b, mul(b, b) ) ) 
print( "{} / {} = {}".format(a, c, divS(a, c) ) )

