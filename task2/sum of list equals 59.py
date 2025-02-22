#sum of list equals 59
list=[10,20,30,9]
new_list=[]
for i in range(len(list)):
    m=list[i]+list[i+1]+list[i+2]
    if m==59:
        new_list=[list[i],list[i+1],list[i+2]]
        print(new_list)
        break
    else:
        i+=1    