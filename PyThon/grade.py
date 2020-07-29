import math

grades=[]

print("Enter your Choices_")

while True:
    print("Enter grades-1 ->")
    print("List grades-2 ->")
    print("Delete grades-3 ->")
    print("Update grades-4 ->")
    print("Clear grades-5 ->")
    print("Calculate Average-7 ->")
    print("Exit-6 ->")

    choice=input("->")

    if not (len(choice)==1 and choice.isnumeric()):
        print("enter a valid choice")
        continue
    if int(choice)==6:
        break
    if int(choice) == 1:
        print("Enter grades.'e' to exit")
        while True:
            grade=input("-->")
            if grade=="e":
                break
            else:
                grade=float(grade)
                grades.append(grade)
    if int(choice)==2:
        for grade in grades:
            print(grade)
    if int(choice)==3:
        for grade in grades:
            print(grade)
        index=int(input("enter the index to delete ->"))
        if index < len(grades) -1 and index >=0:
            grades.pop(index)
        else:
            print("Invalid Index ! Try Again")
    if int(choice)==4:
        for grade in grades:
            print(grade)
        index=int(input("enter the index to update ->"))
        if index < len(grades) -1 and index >=0:
            new_grade=float(input("->"))
            grades[index]=new_grade
        else:
            print("Invalid Index ! Try Again")
    if int(choice) == 5:
        grades.clear()
    if int(choice) == 7:
        sum=0.0
        for grade in grades:
            sum=sum+grade
        average=sum/len(grades)
        print("Average",average)