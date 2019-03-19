def main():
    try:
        read=open("a.text","r")
        for line in read:
            print(line)
    except IOError:
        print("the file is not found")
if __name__ == '__main__':main()
