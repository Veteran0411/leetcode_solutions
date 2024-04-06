// # . Two Sum
// # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # You can return the answer in any order.

var twoSum = function(nums, target) {
    const hashMap={}
    for(let i=0;i<nums.length;i++){
        let val=target-nums[i]
        if(!hashMap.hasOwnProperty(val)){
            hashMap[nums[i]]=i;
        }else{
            return [i,hashMap[val]];
        }
    }
};
var nums=[3,2,4]
var target=6
console.log(twoSum(nums,target))