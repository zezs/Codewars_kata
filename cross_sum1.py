def cross_sum1(num):
    digits = []
    while num != 0:
        right_most_digit = num % 10
        #print(right_most_digit)
        digits.append(right_most_digit)
        #print(digits)
        num = num//10
    return digits

sum = 0
num = int(input("Enter a number: "))
digits = cross_sum1(num)

for digit in digits:
    sum += digit

print(sum)