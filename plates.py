def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>1 and len(s)<7:
       
        if s[0].isalpha() and s[1].isalpha():
             for i in s:
               
                if i.isalpha():
                     if s.index(i)+ 1==len(s):
                         return s
                else:
                    if i.isdigit():
                        if i=='0':
                            break
                        else:
                            if s.index(i)<len(s)-1:
                                c=s.index(i)+1
                     
                                if s[c].isalpha():
                                    break
                                else:
                                    continue

                            else:
                                return s
                    
                    
                          
                     


       
          




main()
