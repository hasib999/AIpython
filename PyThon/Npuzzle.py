def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count

def solve(arr, n):
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] and arr[i] and arr[i] > arr[j]:
                count += 1
    return count % 2 == 0

arr = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]
n = len(arr)

print("Number of inversions are",
    getInvCount(arr, n))
if solve(arr, n) == 0:
    print("Solvable")
elif solve(arr, n) != 0:
    print("Not solvable")