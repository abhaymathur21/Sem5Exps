
import random

def hiring_problem(n):
    best = 0
    cost = -1
    hired=[]
    j=0
    applicants = [i for i in range(1,n+1)]
    for i in range(n):
        applicant = random.choice(applicants)
        applicants.remove(applicant)
        if applicant > best:
            best = applicant
            # print(best)
            hired.append(best)
            j+=1
    print("These applicants were hired at some point: ")         
    # print(applicant for applicant in hired)
    for applicant in hired:
        print(applicant)
    
    print("Cost =" , len(hired)-1)
    

n = 10
hiring_problem(n)