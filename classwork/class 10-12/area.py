shape = input("enter shape")

if (shape == "triangle"):
    b = int(input("enter base"))
    h = int(input("enter height"))
    print("are of triangle is: ", (.5) * b * h)

elif (shape ==  "square"):
    s = int(input("enter side"))
    print ("area of square is: ", (s ** 2))

elif (shape == "rectangle"):
    l = int(input("enter length"))
    w = int(input("enter width"))
    print("area of rectangle is: ", ((l) * (w)))

elif (shape == "parallelogram"):
    b = int(input("enter base"))
    h = int(input("enter height"))
    print("area of parralelogram is ", ((b) * (h)))

elif (shape == "trapezoid"):
    b1 = int(input("enter base 1"))
    b2 = int(input("enter base 2"))
    h = int(input("enter height"))
    print("area of circle is ", ((0.5) * ((b1) + (b2) * (h))))

elif (shape == "circle"):
    r = int(input("enter radius"))
    print("area of circle is ", ((3.14) * (r ** 2)))

elif (shape == "rhombus"):
    b = int(input("enter base"))
    h = int(input("enter height"))
    print("area of parralelogram is ", ((b) * (h)))

else:
    print("error wrong shape")