def searchInsert(nums,target):
    
    start = 0
    end = len(nums)
    position = "not found"
    while start <= end :
        mid = ((start + end ) // 2) + 1
        
        if mid == end and mid != target:
            break
        if nums[mid] == target:
            print(mid)
            break
        elif nums[mid] < target: 
            start = mid 
        elif nums[mid] > target:
            end = mid 
    print( position)
        
searchInsert(nums = [1,2,3,4,5,6,7,8], target = 11)