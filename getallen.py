print("Input five integers:")
nums = list(map(int, input().split()))
nums.sort()
print("After sorting the said ntegers:")
print(*nums)