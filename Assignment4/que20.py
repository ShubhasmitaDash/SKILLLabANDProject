# Given a list, find the index where the sum of the left part equals the sum of the
#right part.
#Input: [1, 7, 3, 6, 5, 6]
#Expected Output: 3 (because [1+7+3] = [5+6])
list=[1,7,3,6,5,6]
for i in range(len(list)):
    if sum(list[:i])==sum(list[i+1:]):
        print(i)
        break
else:
    print(-1)
