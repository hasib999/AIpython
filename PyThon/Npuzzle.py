def getInvCount(arr):
  inv_count = 0
  for i in range(16-1):
    for j in range(16):
      if (arr[i] > arr[j]):
        inv_count += 1
  # print(inv_count)
  return inv_count

def IsSolvable(puzzle):
  invCount=getInvCount(puzzle)
  return (invCount%2!=0)

puzzle=[6,1,10,2,7,11,4,14,5,0,9,15,8,12,13,3]
n=len(puzzle)
if(IsSolvable(puzzle)):
  print("Solvable")
else:print("Not Solvable")