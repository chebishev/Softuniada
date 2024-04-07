def has_consecutive_digits(number):
    prev_digit = number % 10
    number //= 10
    while number:
        current_digit = number % 10
        if abs(current_digit - prev_digit) != 1:
            return False
        prev_digit = current_digit
        number //= 10
    return True


start = int(input())
end = int(input()) + 1


def consecutive_digits_generator(start, end):
    for number in range(start, end):
        if has_consecutive_digits(number):
            yield number


# Print the result using the generator
for number in consecutive_digits_generator(start, end):
    print(number)
