# list of elements 
list=[1,2,3,4,5,6,6,5,3]
count={}
non_rep=[]
for e in list:
    if e in count:
        count[e]+=1
    else:
        count[e]=1
for e,c in count.items():
    if c==1:
        non_rep.append(e) 

print("non repeting elements",non_rep)                           