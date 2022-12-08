digits = [ ]
count = 0
calc_inp = int(input("How many numbers would you like to add or multiply?"))
total = 0
while count < calc_inp:
    num = int(input("Type an integer: "))
    count += 1
    digits.append(num)
calc_op = input("Choose to multiply '*' or add '+': ")

for n in digits:
    if calc_op == "+":
        total += n
    elif calc_op == "*":
        if total == 0:
            total = n
        else:
            total *= n

print(total)


