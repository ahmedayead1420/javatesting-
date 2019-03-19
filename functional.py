def sizeoftrin(b,h):
    size=1/2*(b*h)
    return size

def main():
    b=input("enter of basic \n")
    h=input("enter of hogh \n")
    si= sizeoftrin( int(b),int(h))
    print("The size {}".format(si))


if __name__ == '__main__':main()
