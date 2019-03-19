

import math

def main():
    degree=input("enter of degree \n")
    if(degree>="85"):
        if(degree>="95"):
            print("A+")
        else:
            print("A-")

    elif(degree>="75" and degree <"85"):
        print("B")
    elif(degree>="65" and degree <"75"):
        print("C")
    elif(degree>="50" and degree <"65"):
        print("D")
    else:
        print("end app")





if __name__ == '__main__':main()
