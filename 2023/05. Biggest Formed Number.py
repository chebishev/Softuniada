numbers = input().split()
numbers.sort(key=lambda x: x * 10, reverse=True)
print("".join(numbers))
