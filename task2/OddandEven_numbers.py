
# declare the list 
list=[10,501,22,37,100,999,87,351]
#create a even and odd list
even=[]
odd=[]
for num in list :
      if num%2==0: 
        even.append(num) 
      else:
       odd.append(num)
  #print the lists     
print('even numbers=',even)
print('odd numbers=',odd)
        