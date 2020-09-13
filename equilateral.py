# INPUT firstSide value
# INPUT secondSide value
# INPUT thirdSide value
# IF firstSide == secondSide == thirdSide
#   PRINT "The triangle is equilateral."
# ELSE PRINT "The triangle is not equilateral."
# END.

firstSide = int(input("Enter the first side: "))
secondSide = int(input("Enter the second side: "))
thirdSide = int(input("Enter the third side: "))

if firstSide == secondSide == thirdSide:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.a")
