count = 0;
numberWithCount = 0;

def collatz(number):
  arrayFill = [number]
  while number != 1:
    if number % 2 == 0:
        number = number / 2;
    else:
        number = number * 3 + 1;
    arrayFill.push(number);
  return arrayFill;

for arrayFillIndex in range(1000000 - 1, 2, -1):
  collatzArray = collatz(arrayFillIndex);
  if (count < len(collatzArray)):
    count = len(collatzArray)
    numberWithCount = collatzArray[0]

print('Number With Count:' + str(numberWithCount))
print('Operation Count:' + str(count))