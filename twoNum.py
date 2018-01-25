

def twoNum(nums,target):

    for i in range(0,len(nums)-1):
        print(i)
        answer = []
        answer.append(nums[i])
        b = target - nums[i]
        for j in range(i,len(nums)-1):
            if nums[j] == b:
                answer.append(nums[j])
                return answer


def twoNum1(nums, target):
    answer = []
    map = {}
    for i in range(len(nums)):
        map[nums[i]] = i
    for i in range(len(nums)):
        b = target - nums[i]
        if b in map.keys() and i != map.get(b):
            answer.append(i)
            answer.append(map.get(b))
            return answer


def twoNum2(nums, target):
    answer = []
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if (complement in map.keys()):
            answer.append(map.get(complement))
            answer.append(i)
            return answer
        map[nums[i]] = i


print(twoNum2([1,2,4,4,5,8,9],8))