def makingthenumber(nums,given_number):
    n = len(nums)
    for i in range(0,n):
        if nums[i]+nums[i-1] == given_number:
            return nums[i] , nums[i-1]
        else:
            print("not possible")
given_number =10
numbers =[1,4,5,6,2,8]
print(makingthenumber(given_number))
