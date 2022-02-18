class Solution:
    def twoSum(self, nums, target) :
        for i in nums :
            for j in nums:
                if i+j==target:
                    return [nums.index(i),nums.index(j)]



Psudo code
[2,7,11,15]
target = 9 


2  =  target -2 (7) , check if target-2 
exists in list ,
if yes :return its index , already you have 
current items index



[2,7,11,15]
target = 26


2 -->   target-2 = 24  , check if exists (NO)
7 --> targert - 7 = 19 (NO)
11 --> targer-11 = 15(YES) --Break







