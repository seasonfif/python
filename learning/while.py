#!/usr/bin/python
# coding=utf-8
import random
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        # 跳出本次循环
        continue
    if count == 7:
        # 跳出整个循环
        break
    print count
print "finish"

a = 0
while a <= 10:
    a += 1
    b = random.randint(1, 10)
    print b

# var = 1
# while var:
# 	num = raw_input("Enter a number:")
# 	print "the number is :", num

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        odd.append(number)
    else:
        even.append(number)
print numbers
print even
print odd
