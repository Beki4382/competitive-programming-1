n= int(input())
nums= list(map(int, input().split()))

for i in range(len(nums)):
      for j in range(i, len(nums)):
            if (nums[i] + nums[j]) % 2 != 0:
                  if nums[i] > nums[j]:
                        nums[i], nums[j]= nums[j], nums[i]
print(*nums)