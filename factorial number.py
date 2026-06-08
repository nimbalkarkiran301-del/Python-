fact = 1

while(True):
    num = int(input('enter number :'))
    
    if num < 0:
        print ('invalid number ,enter non negative number.')
        continue 
    
    for i in range (1,num+1):
            fact = fact * i
    print (fact)   
    
    ch = input("Do you want to calculate another factorial, yes/no :"  )
    if (ch == "yes"):
        fact = 1
        continue 
    else:
        break