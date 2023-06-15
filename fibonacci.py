a = int(input('a value is:'))
b = int(input('b value is: '))
fibonacci_sequence = []
fibonacci_sequence.append(b)
while b < 34:
    a, b = b, a + b
    fibonacci_sequence.append(b)
print(' '.join(str(num) for num in fibonacci_sequence))

# a value is:0
# b value is:1
# output:1 1 2 3 5 8 13 21 34



