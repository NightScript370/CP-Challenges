def recursPerm(nums):
    result = []

    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        currentNum = nums[i]
        remainingNums = nums[:i] + nums[i + 1:]
        remainingNumsPermuted = recursPerm(remainingNums)
        for j in range(len(remainingNumsPermuted)):
            permutedArray = [currentNum] + remainingNumsPermuted[j]
            result.append(permutedArray)
    return result


def permuteNumCompat(number):
    return [int(x) for x in str(number)]


def permute(number):
    permNum = permuteNumCompat(number)
    numArr = [int("".join([str(y) for y in x])) for x in recursPerm(permNum)]
    return numArr


def isPermute(primNum, checkAgainstNum):
    return checkAgainstNum in permute(primNum)


print(isPermute(177, 772))