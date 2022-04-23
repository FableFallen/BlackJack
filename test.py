test = [x for x in range(100)]
for index,num in enumerate(test): 
    if index%10 == 0: print() 
    print(num+1, '\t', end = '')
