digits = [ ]
count = 0
calc_inp = int(input("How many numbers would you like to add or multiply?"))
while count < calc_inp:
    num = input("Type an integer: ")
    count += 1
    digits.append(num)
calc_op = input("Choose to multiply '*' or add '+': ")
if calc_op == "+":
    digits.join("+")
    print(digits)
