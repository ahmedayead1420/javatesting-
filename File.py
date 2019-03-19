def main():
    out=open("ahmed.text","a")
    out.write("\n رضي الله عن الخلفاء الراشدين ")
    out.close()
    read=open("ahmed.text","r")
    for line in read:
        print(line)
if __name__ == '__main__':main()
