test = [x for x in range(100)]
for index,num in enumerate(test): 
    print(index)
    if index%2:
        index-=1