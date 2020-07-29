list1=[1,2,[1,2]]
def nested_sum(l):
    sum=0
    for i in l:
        if type(i) is list:
            sum += nested_sum(i)
        else:
            sum += i
    return sum
print(nested_sum(list1))