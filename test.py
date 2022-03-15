test = [1,2,3,4,5,6,7,8]
hist = []
def testing(arr, ele):
    i = 0
    while i < len(arr):
        if arr[i] == ele:
            break
        i+=1 
    return [ele, i]

hist.append(testing(test,2))
hist.append(testing(test,8))
print(hist)