import datetime

def main():
    uodate=input("input of dob \n ")
    if(uodate=="1998"):
      datenow=datetime.datetime.now().year
      age=datenow-int(uodate)
      print(type(uodate))
      print("uo age {} ".format(age))
    else:
        print("try again")

if __name__ == '__main__':main()

