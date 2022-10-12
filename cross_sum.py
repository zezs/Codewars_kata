def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums
    
num = int(input("Enter: "))
l = get_pos_nums(num)
print(l)
sum = 0

for i in l:
    sum += i

print(sum)

res = 3//10
print(res)