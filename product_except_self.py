#type: array
#skill learn: iterate loop in reverse
#for i in range(len(list)-1, -1, -1)
 
def productExceptSelf(nums):
	L = [0] * len(nums)
	R = [0] * len(nums)
	result = [0] * len(nums) 
	L[0] = 1
	
	for i in range(1, len(nums)):
		x = nums[i-1] * L[i-1]
		L[i] = x
	
	R[len(nums)-1] = 1
	
	for i in range(len(nums)-2, -1, -1):
		y = nums[i+1] * R[i+1]
		R[i] = y
	
	for i in range(0, len(nums)):
		result[i] = L[i] * R[i]
	
	return result

n = [1,2,3,4]
print("expected: [24,12,8,6]")
print(productExceptSelf(n))
n2 = [4,5]
print("expected: [5,4]?")  
print(productExceptSelf(n2))      