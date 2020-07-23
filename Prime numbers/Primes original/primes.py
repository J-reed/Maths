

text_file = open("Primefile.txt","w")
text_file2 = open("Non_Primefile.txt","w")
limit=int(input("how many primes?"))
primelist=[]
non_prime=[]
x=len(primelist)
while (len(primelist)<limit):
   
    
        
    primelist.append(6*x+1)
    primelist.append(6*x+5)

    ii=0
    while((ii<len(primelist))):
        if(non_prime.count(primelist[ii]*(6*x-1))==0):        
            non_prime.append(primelist[ii]*(6*x-1))  
        if(non_prime.count(primelist[ii]*(6*x-5))==0): 
            non_prime.append(primelist[ii]*(6*x-5))
        ii=ii+1

    if(non_prime.count((6*x-5)*(6*x-5))==0):        
        non_prime.append((6*x-5)*(6*x-5))
    if(non_prime.count((6*x-1)*(6*x-1))==0): 
        non_prime.append((6*x-1)*(6*x-1))

    i=0
    while(i<len(non_prime)):
        if(primelist.count(non_prime[i])!=0):
            if(non_prime[i]!=5):
                if(non_prime[i]!=7):
                    if(non_prime[i]!=11):
                        if(non_prime[i]!=2):
                            if(non_prime[i]!=3):
                                primelist.remove(non_prime[i])
        i=i+1

    text_file=open("Primefile.txt","w")
    text_file2 = open("Non_Primefile.txt","w")
    text_file.write(str(primelist)+"\n")

    text_file2.write(str(non_prime)+"\n")

    text_file.close()
    text_file2.close()

    x=x+1
              
    


#print(primelist)
print()

#text_file2.write(str(non_prime)+", ")
non_prime.sort()
#print(non_prime)
print()
print(str(len(primelist))+" primes found")
text_file.close()
