def calculate_nextlayer(old_array):
    new_array=[]
    i=0
    while (i < len(old_array)-1):
        if(old_array[i+1]>old_array[i]):
            new_array.append(old_array[i+1]-old_array[i])
        if(old_array[i]>old_array[i+1]):
            new_array.append(old_array[i]-old_array[i+1])
        if(old_array[i]==old_array[i+1]):
            new_array.append(old_array[i]-old_array[i+1])
        i=i+1
    return new_array

def find_prime(listarray):
    bottomlayer=[1]

    listarray.append(bottomlayer)
    lastArrayPosition=listarray.index(listarray[-1])

    DecisionArray=[]

    while(lastArrayPosition>-1):
        x=0
        if(lastArrayPosition==0):
               listarray[lastArrayPosition].append(listarray[lastArrayPosition][-1]+listarray[lastArrayPosition+1][-1])

        else:
                if(listarray[lastArrayPosition][-1]-listarray[lastArrayPosition+1][-1]<-1 and x==0):
                   listarray[lastArrayPosition].append(listarray[lastArrayPosition][-1]+listarray[lastArrayPosition+1][-1])
                   x=1
                   DecisionArray.append("+")

                if(listarray[lastArrayPosition][-1]-listarray[lastArrayPosition+1][-1]>-1 and x==0):
                    listarray[lastArrayPosition].append(listarray[lastArrayPosition][-1]-listarray[lastArrayPosition+1][-1])
                    x=1
                    DecisionArray.append("-")

        lastArrayPosition=lastArrayPosition-1

    isprime=testforprime(listarray[0][-1],listarray)
    if(isprime==1):
        print("Last Digit Prime")
    if(isprime==0):
 #       print("Last Digit Not Prime")
        try_again(listarray,DecisionArray)

def testforprime(number, array):

    i=0
    while (i < (len(array[0])-1)):
        test=number/(array[0][i])
        if(round(test)==test):
              return 0
        i=i+1
    return 1

def try_again(listarray,decisionArray):

    i=2
    while(True):
        print(listarray)
        del(listarray[0][-1])
        del(listarray[1][-1])
        del(listarray[2][-1])

        if(decisionArray[-2]=="-"):
            listarray[2].append(listarray[3][-1]+listarray[2][-1])

        if(decisionArray[-2]=="+"):
            listarray[2].append(listarray[3][-1]+listarray[2][-1])
            listarray[1].append(listarray[2][-1]-listarray[1][-1])

        if(decisionArray[-1]=="+"):
            listarray[1].append(listarray[2][-1]+listarray[1][-1])
        listarray[0].append(listarray[0][-1]+listarray[1][-1])

        print(listarray)
        break



#Start Program Here

arrayOfArrays=[]
Array1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281
,283,293,307,311,313,317,331,337,347,349
,353,359,367,373,379,383,389,397,401,409
,419,421,431,433,439,443,449,457,461,463
,467,479,487,491,499,503,509,521,523,541
,547,557,563,569,571,577,587,593,599,601
,607,613,617,619,631,641,643,647,653,659
,661,673,677,683,691,701,709,719,727,733
,739,743,751,757,761,769,773,787,797,809
,811,821,823,827,829,839,853,857,859,863
,877,881,883,887,907,911,919,929,937,941
,947,953,967,971,977,983,991,997,1009,1013
]
print(len(Array1))
ArrayStore=[]

arrayOfArrays.append(Array1)

while (len(Array1)!=1):
    ArrayStore=calculate_nextlayer(Array1)
    arrayOfArrays.append(ArrayStore)
    Array1=ArrayStore

i=len(arrayOfArrays)-1
while (i>0):
    print(arrayOfArrays[i][-1])
    i=i-1
print(arrayOfArrays[0][-1])

#print()
#find_prime(arrayOfArrays)

#print(arrayOfArrays[0])

