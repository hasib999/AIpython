def cum_sum(list1):
    total=0
    result=[]
    for val in list1:
        total+=val
        result.append(total)
    return result
list=[1,2,3]
print(cum_sum(list))
