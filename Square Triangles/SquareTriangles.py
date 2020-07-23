import math

def isint(x):#getting around types in python to find if a number is an integer 
    a=str(x) #(e.g trying to show that 12.0 is an integer when functions like math.sqrt return floats)

    i=0
    while i < len(a):
        if (a[i]==(".")):
            l=i+1
            while l<len(a):
                if a[l]!="0":
                    return False
                l+=1
        i+=1
    return True

####################################################################################################
#BRUTE FORCE METHODS: inefficient

def findSquareTriangeNumbers(): 
    x=int(input("Enter a threshold number (Doesn't really matter, just makes sure the function doesn't loop forever, to get more results enter a bigger number): "))
    i=1
    t=1
    while t<x:                              #This just brute forces, going through every triange number, seeing if its square root is an integer
        t=(i*(i+1))/2                     # and if this is the case, printing it 
        if(isint(math.sqrt(t))):        
            print(t)                          #Therefore VERY INEFFICIENT
        i+=1

def findSumsofTriangleNumbersequallyatriangenumber():
    #I wrote this after noticing that for any Triangle number T(n), T(n)+T(n-1) is a square number:

    #We want to find T(n)+T(n+1) = T(m) where T(m) = N^2 (where N is just some number, T(k) means the 'k'th triangle number)

    #First:
    #We need to find T(n)+T(n+1) which = T(m):
        #Therefore:
    
        #( n(n+1)/2 )+( (n+1)(n+2)/2 ) = ( m(m+1)/2 ).
        #                           Hence:
        #(2n^2+4n+2)/2= ( m(m+1)/2 ).
        #n^2+2n+1 = ( m(m+1)/2 )
    
    #Second:
    #We want to show that T(m) is a square number, therefore:
        #N^2 = ( m(m+1)/2 )

        #Hence:
        #0=( m^2+m )/2 -N^2
        #0=m^2+m - 2N^2

        #Therefore by quadratic formula we can find m through:
        #m=(   -1±sqrt(  1-4*1*(-2N^2 )  )   )/2
        #m=(  -1±sqrt( 1+8(N^2) ) )/2

    #Third:
    #We also know by definition that N^2 = T(m) =T(n)+T(n+1)
        #Hence N^2 = n^2+2n+1 as using the result in part 1.
        #Therefore, subbing this into the result from part 2 gives:
            #m= (  -1±sqrt( 1+8(n^2+2n+1) )   )/2

    #If the 'm' returned by the equation from the third part is an integer, then we know we have found T(m) such that T(m) = N^2
    #Therefore we have found a square triangle number

    ###################
    #Doing what is written above#
    ###################

    x=int(input("Enter a threshold number (Doesn't really matter, just makes sure the function doesn't loop forever, to get more results enter a bigger number): ")) 
    print()
    print("###############")
    i=1
    t1=1#the first triange number is 1, only done to start while loop
       
    while t1<x:
        t1=(i*(i+1))/2 #finding T(n)
        t2=((i+1)*(i+2))/2 #finding T(n+1)
        if(isint(((-1)+math.sqrt((1+8*(t1+t2))))/2)):#if  'm' is an integer then square triange is found: hence print result
            print(t1," | ",i)                                             
            print(t2," | ",(i+1)) 
            print(t1+t2 ," | ",(((-1)+math.sqrt((1+8*(t1+t2))))/2)) #prints (T(m) | m )
            print("###############")#These print statements print each triange number used follow by which triangle number they are, i.e for the first iteration for which m is an int: t1=15,i=5 | t2=21,i+1=6 | t1+t2=36. m=8=((-1)+math.sqrt((1+4*(t1+t2)*2)))/2)
        i+=1                                            #Therefore this is printed: 15 | 5     21 | 6      36 | 8              
                                                           #Note, that (i+1)^2=t1+t2


        #Note: This is also a brute force method going through every pair of triange numbers therefore also:
        #INEFFICIENT


def usingdiscriminant():

    #Using the result found for the above function i.e. m= (  -1±sqrt( 1+8(t1+t2) )   )/2, subbing t1+t2 = N^2:
    #Hence: m= (  -1±sqrt( 1+8(N^2) )   )/2

    #For m to be an integer, sqrt( 1+8(N^2) ) must be an integer (i.e. the discriminant of the formula for m must be an integer).
    #Lets call this integer 'a', therefore: a =sqrt( 1+8(N^2) )

    #Rearrange to get N = sqrt(  ( a^2 - 1 )/8  )
    #Now all we have to do is find integer 'N's when inputing integer 'a's to find a square triangle number
    
    #############
    #Why do this?
    #the input number x can be far smaller in this function than the previous to yield the same output and in theory therefore this is more efficient.
    #############

    
    x=int(input("Enter a number (Doesn't really matter, just makes sure the function doesn't loop forever, to get more results enter a bigger number): ")) 
    discrim=0 #renamed 'a' to discrim to indicate where it comes from                                        
    while discrim<x: 
        try:#To get around crashes with bad sqrts
            n=math.sqrt(((discrim**2)-1)/8) #As we start with an integer discriminant, we have to check that the n produced is also an integer, else it isn't a square number
            if(isint(n)):
                   print(n," | n")  
                   m=(discrim-1)/2#finishing the quadratic formula, as (-1±discrim)/2=m, m must be positive therefore m = (discrim-1)/2
                   print(discrim," | discriminant")
                   print("~~")
                   print((m*(m+1))/2, " | SquareTriange")#use the m value to find T(m) which is S(n) (could have also just squared n to get the value printed
                   print("#######")

                   
        except:
            print("nope")
        discrim+=1 #Brute force for every natural integer therefore INEFFICIENT


#END OF BRUTE FORCE METHODS
####################################################################################################

def findnextn(nlist): #This one will take a lot of explaining, see other document
    length=len(nlist)#finds the number of triangle numbers the computer already knows
    
    i=0
    coefficients=[]
    while i<=(length):
     coefficients.append(((math.factorial(length))/(math.factorial(i)*math.factorial(length-i)))*(3**i)*((-1)**(i)))#Had to write the choose function in full,Used document formula
     i+=1 #Coefficients will is a list of the coeffiecients to each STwhich will be needed to find the next n (using formula from the end of the document)

    if((length+1)%2==0):#This calulates "Value" from the formula in the document, length + 1 is as we are finding the next n, not in the list
        newn=2**(3*((length-1)/2)) #if even | is length -1 since the value tested to be even is length +1, and that number -2 must be used, length +1 -2 = length-1
    else:
        newn=0#if odd
    
    l=0
    while l<length:#This goes through eeach known square triangle number, times it by the appropriate coefficient as per the formula and takes it from the total as per the formula
            newn=newn-(coefficients[length-l]*nlist[l])#This doesn't go negative because "coefficients[length-l]*nlist[l]" alternates between being positive an negative itself
            l+=1
    nlist.append(newn)#adds the new root of a square triangle number onto the list
    return nlist

def findnextSquaretriangle(nlist):
    sqtrianglelist=[]
    numberoftrianglesquares=int(input("how many square triangle numbers do you want to find? "))#To make the program stop after a point
    
    while len(sqtrianglelist)<numberoftrianglesquares:
        nlist=findnextn(nlist)
        sqtriangle=nlist[-1]**2#square each number from the nlist to get the actual square triangle numbers
        
        sqtrianglelist.append(int(sqtriangle))#the int is only so that when printing to console, no ".0"s show as they are annoying and clutter the screen, the actual numbers
                                                            #are integers
    print(sqtrianglelist)#print the square triangle to the screen




########################################################################################
def printoptions():
    print("MENU")
    print("------------------------------")
    print("1. Test if an input number is an integer")
    print("2. A BRUTE FORCE method to find square triangle numbers")
    print("3. A BRUTE FORCE method to find square triangle numbers using two consecutive triangle numbers")
    print("4. A BRUTE FORCE method to find value for n using the discriminant of the quadratic formula for m")
    print("±±±±±±±±±±±±±±±±±±±±±±±")
    print("FORMULA BASED (Should be much more efficient than methods above)")
    print("5. Given a list of values of known values of n, from n^2=(m(m+1))/2, calculate the next n")
    print("6. Use method from option 5 to produce a list of the square triangle numbers")
    print("±±±±±±±±±±±±±±±±±±±±±±±")
    print("9. Quit")
    print("------------------------------")
    print()
    print()

def getchoice():
    i=input("Enter menu selection ")
    try:
        i=int(i)
    except:
        print("choose a better value")
        getchoice()
    return i

def formatscreen():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("\n"*2)#Just to try to make things more readable


if __name__ == '__main__':
    i=0
    nlist=[0]
    
    
    while i!=9:
        formatscreen()
        printoptions()
        i=getchoice()
        if(i==1):
            number=input("Enter a number ")
            print(isint(number))
            print()
        if(i==2):
            findSquareTriangeNumbers()
            print()
        if(i==3):
            findSumsofTriangleNumbersequallyatriangenumber()
            print()
        if(i==4):
            usingdiscriminant()
            print()
        if(i==5):
            nlist=findnextn(nlist)
            print(nlist)
            print()
        if(i==6):
            nlist=[0]
            findnextSquaretriangle(nlist)
            print()
        x=input("Continue?")
