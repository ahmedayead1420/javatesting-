def main():
    try:
        x=input("enter the value  x \n")
        y=input("enter the value of   y\n")
        z=int(x)/int(y)
        print("z= {}".format(z))
    except :
        print("division on zero")
    else:
        print("the opreation is completed")

if __name__ == '__main__':main()
