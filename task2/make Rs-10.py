#takes the coins as list
list=[1,2,5,10]
# iterate for each coin
for coins in list:
    if coins==1:
        a="coins*10"
        print("for 1Rs coins",a)
    if coins==2:
        a="coins*5"
        print("for 2Rs coins",a)
    if coins==5:
        a= "coins*2"
        print("for 5Rs coins",a) 
    if coins==10:
        a="coins*1"
        print("for 10Rs coin",a)    