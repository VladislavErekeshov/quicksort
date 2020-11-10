def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = nums[0]
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
array = [10, 5, 2, 3]
q = list(quicksort(array))

print(q)