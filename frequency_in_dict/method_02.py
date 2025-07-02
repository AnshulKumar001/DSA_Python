num=[2,4,4,5,6,7,5,4,3,2,31,12]

dict1={}
for i in range(0,len(num)):
    dict1[num[i]]=dict1.get(num[i],0)+1
print(dict1)    
