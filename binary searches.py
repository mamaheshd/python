def binarysearch(arr,f,r,d):
    if r>=1:
        mid=f+(r-1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,f,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        -1
arr =[2,5,7,10,12,15,20,25]
x=10
result = binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("element ispresent in indes %d" %result)
else:
    print("element not found in array")
