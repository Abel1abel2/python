def main():
    time=input("enter the time ")
    a=time.replace("am"," ").replace("pm"," ")


    convert(a)

def convert(a):
     d,b=a.split(":")
     x=float(d)
     y=float(b)
     r=x*60+y
     s=(r*0.5)/30
     
    
   
     if s>=7 and s<=8:
          
               print("breakfast",s)
     elif s>=12 and s<=13:
        
               print("lunch",s)
     elif s>=18 and s<=19:
            
               print("lunch",s)
     else:
          print("not time for food")
main()