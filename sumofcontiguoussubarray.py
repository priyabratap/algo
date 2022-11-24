# // Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
# // Input: [2, 1, 5, 1, 3, 2], k=3 
# // Output: 9
# //Explanation: Subarray with maximum sum is [5, 1, 3]

def maxSum(arr, n, k):
    # k must be smaller than n
    if (n < k):
        print("Invalid")
        return -1
     
    maxs = 0
    cur_sum = 0
    fsubarr = []
    for i in range(n):
        cur_sum += arr[i]
        if i <= k-1 :
            print("if")
            maxs=cur_sum
            fsubarr.append(arr[i])
        if i >= k:
            cur_sum = 0
            subarr=[]
            # print("maxs,cur_sum",maxs,cur_sum)
            for j in range(k):
            	cur_sum += arr[i-j]
            	print("i",i,"j",j,"arr[i-j]", arr[i-j])
            	subarr.append(arr[i-j])
            
            if cur_sum > maxs:
                maxs = cur_sum
                fsubarr = subarr
                
    print("final sub array with max sum",fsubarr)
    return maxs
 
# input
arr = [2, 9, 5, 21, 3, 2,6,8,9]
k = 3
n = len(arr)

print("array length",n)
print("-----------------------------")
print("maxsum",maxSum(arr, n, k))
