import random

#list_ = random.randint(0, 20)
list_ = ["1", "2", "3", "1", "5", "2", "7", "3", "5", "1"]
list_ = "".join(list_)
count_ = 0

for i in list_:
    if list_.count(i) >= 2:
        list_ = list_.replace(i, '', 2)
        count_ += 1
        print(list_)
print(count_)

list_ = [1, 2, 2, 3, 5, 6, 5, 3, 3, 2, 2]
count_ = 0
for temp in list_:
    y = list_.pop(0)
    print(list_)
    if y in list_:
        count_ += 1
        list_.remove(y)
        print(list_)
        print()

print(count_)