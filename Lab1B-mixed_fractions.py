#   Nicolas Callier
#   CSCI 101 - Section A
#   Python Lab 1A
#   References: ZyBooks section 14.3, 15.1, 15.7, 20.2
#   Time: 45 minutes

print("Input the numerator of the improper fraction.")
numerator = (int(input("NUMERATOR>")))
print("Input the denominator of the improper fraction.")
denominator = (int(input("DENOMINATOR>")))
newNum = numerator % denominator
coefficient = int((numerator-newNum)/denominator)
print("OUTPUT ",coefficient,str(newNum)+"/"+str(denominator))
