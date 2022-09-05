function recursivePermute(nums) {
    let result = [];
  
    if (nums.length === 0) return [];
    if (nums.length === 1) return [nums];
  
    for (let i = 0; i < nums.length; i++) {
        const currentNum = nums[i];
        const remainingNums = nums.slice(0, i).concat(nums.slice(i + 1));
        const remainingNumsPermuted = recursivePermute(remainingNums);
        for (let j = 0; j < remainingNumsPermuted.length; j++) {
            const permutedArray = [currentNum].concat(remainingNumsPermuted[j]);
            result.push(permutedArray);
        }
    }
    return result;
}

function permuteNumCompat (number) {return number.toString().split('').map(num=>parseInt(num))}

function permute (number) {
    const permuteNumber = permuteNumCompat(number);
    const numberArrayResponse = recursivePermute(permuteNumber).map(arrayOfNums=>parseInt(arrayOfNums.map(num=>num.toString()).join('')))
    return Array.from(new Set(numberArrayResponse))
}

function isPermute (primNum, checkAgainstNum) {return permute(primNum).includes(checkAgainstNum)}

isPermute(177, 717)