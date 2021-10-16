def linearSearch(arr,a):
    for i in range(len(arr)):
        if arr[i]==a:
            return i
    return -1
arr=[0,8,2,99,46,1,3,9,10,24,50,29,5]
print (arr)

a=int(input("which element do u want to search:"))
print("element found",linearSearch(arr,a))