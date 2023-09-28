#for Potential method of Amortized Analysis
l=[]
cost=0
balance=0
def push(a):
    initialsize=len(l)
    l.append(a)
    currentsize=len(l)
    print("push operation")
    print("cost=1+currentstate-previoussate")
    print(f"cost=1+{currentsize}-{initialsize}")
    print(f"cost={1+currentsize-initialsize}")
def pop():
    initialsize=len(l)
    l.pop(len(l)-1)
    currentsize=len(l)
    print("pop operation")
    print("cost=1+currentstate-previoussate")
    print(f"cost=1+{currentsize}-{initialsize}")
    print(f"cost={1+currentsize-initialsize}")
def multipop(n):
    initialsize=len(l)
    for i in range(n):
        l.pop(len(l)-1)
    currentsize=len(l)
    print("multipop operation")
    print("cost=k+currentstate-previoussate")
    print(f"cost={n}+{currentsize}-{initialsize}")
    print(f"cost={5+currentsize-initialsize}")

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
