#VARIABLES
zero  = [1,1,0,1,1,1,1]
one   = [0,0,0,1,0,0,1]
two   = [1,0,1,1,1,1,0]
three = [1,0,1,1,0,1,1]
four  = [0,1,1,1,0,0,1]
five  = [1,1,1,0,0,1,1]
six   = [1,1,1,0,1,1,1]
seven = [1,0,0,1,0,0,1]
eight = [1,1,1,1,1,1,1]
nine  = [1,1,1,1,0,1,1]
error = [1,1,1,0,1,1,0]
list1 = [zero,one,two,three,four,five,six,seven,eight,nine,error]
temp  = [0,0,0,0,0,0,0]

#FUNCTION FOR DECIMAL INPUT
def decimalinput(num,list1):
   if (num>=0 and num<=9):
      temp=list1[num]
      printing(temp)
   else:
      printing(error)
      
def bin_dec(binary):
   decimal = 0
   for i in binary:
       if (int(i)==0 or int(i)==1):
           decimal = decimal*2 + int(i)
       else:
           print ("\nWRONG BINARY INPUT")
           printing(error)
           exit (0)
   print ("Decimal value is=",decimal)
   decimalinput(decimal,list1)

#FUNCTION FOR PRINTING THE 7 SEGMENT OUTPUT 
def printing (temp):     
   b=[]
   for i in range(0,7):
      if (i==0 or i==2 or i==5):
         if(temp[i] ==1):
            b.append("_")
         else:
               b.append(" ")
      else:
         if(temp[i]==1):
            b.append("|")
         else:
            b.append(" ")
         
#printing(b)      
   print("\nLCD output : ")
   print(" ",b[0],sep="")
   print(b[1],b[2],b[3],sep="")
   print(b[4],b[5],b[6],sep="")
   
#main
print("BCD TO 7 SEGMENGT DISPLAY ")     
while(1):
   ch=int(input("\n0.Exit\n1.Decimal input\n2.Binary input\n Enter your choice :"))
   if ch==0:
      print("\n\nEXIT!!!\n\n")
      exit (0)
   elif ch==1:
      dec = int(input("Enter decimal value :"))
      decimalinput(dec,list1)
   elif ch==2:
       bin = input("Enter binary input :")
       bin_dec(bin)
   else:
      print("Wrong input !!!")
      printing(error)