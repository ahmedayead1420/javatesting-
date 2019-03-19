import math
def main():
    i=3
    while(i<5):
        a=input("enter the value of a \n")
        b=input("enter the value of b \n")
        c=input("entre the value of c \n")
        x=math.pow(int(b),2)-4*(int(a)*int(c))
        if(x>=0 and a!=0):
            x1=math.sqrt(x)
            y=2*int(a)
            z=-int(b)+x1
            so=z/y
            print("The first solution = ",so)
            z1 = int(b) + x1
            so2 = z1 / y
            print("The secend solution = ", so2)
        else:
            print("The solution is complex")

            i+=1


if __name__ == '__main__':main()
