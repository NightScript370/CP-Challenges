import random
numbersToPick = 10

def mergeIt(list1,list2):
  list3 = []
  for i in range(numbersToPick):
    if list1[i] > list2[i]:
      list3.append(list2[i])
      list3.append(list1[i])
    else:
      list3.append(list1[i])
      list3.append(list2[i])
  return list3

#list1 = []
#list2 = []

#for i in range(numbersToPick):
#  list1.append(int(str(i) + str(random.randint(0, 9))))
#  list2.append(int(str(i) + str(random.randint(0, 9))))

list1 = [random.randint(i * 10, i * 10 + 9) for i in range(numbersToPick)]
list2 = [random.randint(i * 10, i * 10 + 9) for i in range(numbersToPick)]

print(mergeIt(list1,list2))