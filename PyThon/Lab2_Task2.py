fin = open('C:/Users/USER/Desktop/words.txt')

def has_no_e(word):
    return "e" not in word


def calculate_no_e_percentage():
    total_count = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            no_e_count += 1
            print(word)
        total_count += 1

    no_e_percentage = float(no_e_count) / total_count * 100
    return no_e_percentage
print(calculate_no_e_percentage(),"%")