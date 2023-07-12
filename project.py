class hotelmanage:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',indate='',outdate='',rno=1):

        print ("*****WELCOME TO HOTEl DE SUAREZ*****")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.indate=indate
        self.outdate=outdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your Fullname:")
        self.address=input("\nEnter your address:")
        self.indate=input("\nEnter your  in date:")
        self.outdate=input("\nEnter your out date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  Class A---->4000")

        print ("2.  Class B---->3000")

        print ("3.  Class C---->2000")

        print ("4.  Class D---->1000")

        x=int(input("Enter the number of your choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have choose room Class A")

            self.s=4000*n

        elif (x==2):

            print ("you have choose room Class B")

            self.s=3000*n

        elif (x==3):

            print ("you have choose room Class C")

            self.s=2000*n

        elif (x==4):
            print ("you have choose room Class D")

            self.s=1000*n

        else:

            print ("please choose a room")

        print ("your choosen room rent is =",self.s,"\n")