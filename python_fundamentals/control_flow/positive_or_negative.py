#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)

if number > 0:
    print(f'{number} The number is positive.')
elif number < 0:
    print(f'{number} The number is negative.')
else:
    print(f'{number} The number is zero.')
