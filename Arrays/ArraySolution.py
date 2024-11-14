"""Two Sum"""

class TwoSum:
    """def __init__(self):
        pass
    def twosum(self,num,target):
        if num is None:
            return False
        if len(num) == 1:
            return False
        for i in range(len(num)):
            if num[i] + num[i+1]== target:
                return [i,i+1]
        return False"""

    #Optimize approach
    def twosum(self,num,target):
        d = {}
        for i in range(len(num)):
            d[num[i]] = i
        for i in range(len(num)):
            diff = target - num[i]
            if (diff in d.keys() and d[diff]!=i):
                return [i,d[diff]]
inst = TwoSum()
num = nums = [3,3]; target = 6
var= inst.twosum(num,target)
#print(var)

class RemoveDuplicates:
    def removeDuplicates(self,nums):
        nums = set(nums)
        return len(nums)

res = RemoveDuplicates.removeDuplicates(None,[1,1,2])
#print(res)

class RemoveElement:
    def removeEle(self,nums,val):
        indx = 0
        for num in nums:
            if nums[num] != val:
                nums[indx] = num
                indx += 1
        return indx

res = RemoveElement.removeEle(None,[3,2,2,3],3)
#print(res)





"""****Binary Search****"""

"""Problem: search in rotated sorted array"""

def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi)//2
        res = condition(mid)
        if res == 'found':
            return mid
        elif res == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def search_rotared_sorted_arr(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid >= 0 and nums[mid-1]==target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)
