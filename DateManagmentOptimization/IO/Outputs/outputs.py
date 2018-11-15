# Traditional format
v = "other text"
n = 10
print("One text", v, "and one number", n)

# Using the method format
c = "One text {} and one number {}".format(v,n)
c

c = "One text '{}' and one number '{}'".format(v,n)
c

c = "One text '{1}' and one number '{0}'".format(v,n)
c

c = "One text '{text}' and one number '{number}'".format(text = v,number = n)
c

c = "{v}, {v}, {v}".format(v = v)
c

# Is possible to align text
# In this case to the right with 30 spaces
print("{:>30}".format("word"))

# In this case to the left with 30 spaces
print("{:30}".format("word"))

# Align to the center
print("{:^30}".format("word"))

# To show just some characters
print("{:.3}".format("word"))

# Example
c = "{v:.2}, {v:.3}, {v:.4}".format(v = v)
c

# Example
c = "{v:>30.2}, {v:>20.3}, {v:>10.4}".format(v = v)
c

# Possible to format integer numbers, filled with spaces
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

# Possible to format integer numbers, filled with zeros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

# Possible to format decimal numbers, filled with spaces
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
