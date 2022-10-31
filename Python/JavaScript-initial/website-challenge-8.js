// Browser Only - Do not want to deal with JSDOM just yet
const numberString = document.querySelector("#content > div.problem_content > p.monospace.center").innerText.replaceAll('\n', '')
const lengthLimit = 13

let largestNumYet = 0
for (let starterNumber = 0; starterNumber < numberString.length - lengthLimit; i++) {
    const dealingString = numberString.substring(starterNumber, starterNumber + lengthLimit).split('')
    if (dealingString.includes('0')) continue;
    largestNumYet = Math.max(largestNumYet, dealingString.map(strNum => parseInt(strNum)).reduce((product, value) => product * value))
}