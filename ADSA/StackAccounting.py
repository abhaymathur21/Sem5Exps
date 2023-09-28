#for Accounting method of Amortized Analysis

l=[]
cost=0
balance=0
def push(a):
    global cost
    global balance
    cost+=1
    balance+=1
    l.append(a)
    print("After push operation balance:",balance,"cost:",cost)
def pop():
    l.pop(len(l)-1)
    global balance
    balance-=1
    print("After pop operation balance:",balance,"cost:",cost)
def multipop(n):
    global balance
    balance-=n
    for i in range(n):
        l.pop(len(l)-1)
    print("After multipop operation balance:",balance,"cost:",cost)

print(l)
push('A')
print(l)
push('B')
print(l)
push('C')
print(l)
pop()
print(l)
push('D')
print(l)
push('E')
print(l)
push('F')
print(l)
push('G')
print(l)
multipop(5)
print(l)

