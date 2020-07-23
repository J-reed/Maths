import math

def AddToPrimeList():
    global limit, primelist,ATPL_Number
    
    while (len(primelist)<limit):

        if((6*ATPL_Number+1)!=1):
            primelist.append(6*ATPL_Number+1)

        primelist.append(6*ATPL_Number+5)

    

        ATPL_Number=ATPL_Number+1

    
    
def AddToNon_Prime():

    global primelist, non_prime
    x=0

    while(x<len(primelist)):
        i=0

        
        while((primelist[x]*primelist[i])<primelist[-1]):
            if(non_prime.count(primelist[x]*primelist[i])==0):
                non_prime.append(primelist[x]*primelist[i])
            i=i+1
        x=x+1
        
          
    
def RemoveNon_Primes():

    global primelist, non_prime,RNP_Number


    while(RNP_Number<len(non_prime)):
        
        if(primelist.count(non_prime[RNP_Number])!=0):
            primelist.remove(non_prime[RNP_Number])
    
        RNP_Number=RNP_Number+1
        
    

#####
global limit,primelist,non_prime,ATPL_Number,RNP_Number

text_file = open("Prime_file2.txt","w")
text_file2 = open("Non_Primefile.txt","w")
limit=int(input("How many cycles of the program?"))

ATPL_Number=0
RNP_Number=0

primelist=[]
non_prime=[]

###

AddToPrimeList()
AddToNon_Prime()
RemoveNon_Primes()

text_file.write("Ignore last number in this list. All of the others are always correct \n")

text_file.write(str(primelist)+ "\n")
text_file2.write(str(non_prime))


print(str(len(primelist))+" primes found")
text_file.close()
text_file2.close()
