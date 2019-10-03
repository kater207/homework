def sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
arr = [407, 192, 901, 308, 271, 24, 436, 433, 822, 527, 805, 385, 144, 792, 487]  
sort(arr)  
print(arr)


arr = [961, 523, 949, 328, 794, 913, 352, 595,613, 931, 721, 674, 364, 140, 719]
n = len(arr)
for j in range(0,n-1):
    for i in range(0,n-j-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i + 1] = arr[i + 1], arr[i]
print(arr)


arr = [310, 464, 475, 922, 592, 800, 426, 430, 279, 137, 170, 440, 555, 658, 520]
minimum = arr[0]
index_of_min = 0

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j] < minimum:
            minimum = arr[j]
            index_of_min = j    
    minimum = arr[i+1]
    arr[i],arr[index_of_min] = arr[index_of_min],arr[i]
    
print(arr)
