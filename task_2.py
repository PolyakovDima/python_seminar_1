number = 123

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

digit_sum = digit1 + digit2 + digit3

print("Сумма цифр трёхзначного числа", number, "=", digit_sum)

def sum_of_digits(number):
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    digit_sum = digit1 + digit2 + digit3
    return digit_sum

number = 123
result = sum_of_digits(number)

print("Сумма цифр трёхзначного числа", number, "=", digit_sum)

def sum_of_digits(number):
    num_str = str(number)

    digit_sum = sum(int(digit) for digit in num_str)

    return digit_sum

number = 123
result = sum_of_digits(number)
print("Сумма цифр трехзначного числа", number, ":", result)
