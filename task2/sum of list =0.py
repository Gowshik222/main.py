list=[4,2,-3,1,6]
sublist=[]
for i in range(len(list)):
    a=list[i]+list[i+1]+list[i+2]
    if a==0:
        sublist=[list[i],list[i+1],list[i+2]]
        print(sublist)
        break
    else:
        i+=1