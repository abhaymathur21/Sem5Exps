#for Aggregate method of Amortized Analysis
array=[]
arraysize=1
cost=0
totalcost=0
no=int(input("Enter the number of elements: "))
print("Element","Size","Cost",sep="\t")

for i in range(1,no+1):
    cost=0
    if len(array)==arraysize:
        cost=arraysize
        arraysize*=2
        
    cost+=1
    array.append(i)
    totalcost+= cost
    print(i,arraysize,cost,sep="\t")
    
print("The total cost is: ", totalcost)
print("Amortized Cost is: ", totalcost/no)