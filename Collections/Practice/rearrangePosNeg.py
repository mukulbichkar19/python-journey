def rearrangePosNeg(nums):
	# O(n^2)
	for i in range(0, len(nums)-1):
		if(nums[i] < 0):
			j = i+1
			while(j <= len(nums)-1):
				if(nums[j] > 0):
					break
				j += 1
			#swap 	
			if(j < len(nums)):
				temp = nums[j]
				nums[j] = nums[i]
				nums[i] = temp
	print(nums)

def rearrange2(nums):
	pos_idx = 0
	neg_idx = len(nums)-1
	#O(n)
	while(pos_idx <= neg_idx):
		if(nums[pos_idx] >= 0):
			pos_idx += 1
		elif(nums[pos_idx] < 0):
			if(nums[neg_idx] < 0):
				neg_idx -= 1
			else:
				temp = nums[neg_idx]
				nums[neg_idx] = nums[pos_idx]
				nums[pos_idx] = temp
				pos_idx += 1
				neg_idx -= 1

	print(nums)


nums = [0,1,-2,3,-5,-7,8,-4,30]
#rearrangePosNeg(nums)
rearrange2(nums)