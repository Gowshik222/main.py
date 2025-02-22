# inisialize 3 list
l1={10,20,30,40,50}
l2={20,40,50,60,70}
l3={40,60,70,80,20}
l1.intersection_update(l2)
l1.intersection_update(l3)
print("the duplicates are:",l1)