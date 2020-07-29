count=0
sentence=input("Enter Sentence>")
vowels=["a","e","i","o","u"]
for letter in sentence:
    if letter in vowels:
        count=count+1
print(count)