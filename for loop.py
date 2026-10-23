 1. Print numbers 1 to 10
for i in range(1, 11): print(i)

 2. Print numbers 1 to 20
for i in range(1, 21): print(i)

 3. Print even numbers
for i in range(2, 21, 2): print(i)

 4. Print odd numbers
for i in range(1, 20, 2): print(i)

 5. Print numbers in reverse
for i in range(10, 0, -1): print(i)

 6. Print multiplication table of 2
for i in range(1, 11): print(2, "x", i, "=", 2*i)

 7. Print multiplication table of 5
for i in range(1, 11): print(5, "x", i, "=", 5*i)

 8. Print multiplication table of 10
for i in range(1, 11): print(10, "x", i, "=", 10*i)

 9. Sum numbers from 1 to 10
print(sum(range(1, 11)))

 10. Sum numbers from 1 to 100
print(sum(range(1, 101)))

 11. Print squares from 1 to 10
for i in range(1, 11): print(i*i)

 12. Print cubes from 1 to 10
for i in range(1, 11): print(i**3)

 13. Print characters of a word
for ch in "Python": print(ch)

 14. Print each fruit
for fruit in ["Apple", "Mango", "Banana"]: print(fruit)

 15. Print each letter in a name
for ch in "Rahul": print(ch)

 16. Print multiples of 3
for i in range(3, 31, 3): print(i)

 17. Print multiples of 4
for i in range(4, 41, 4): print(i)

 18. Print numbers divisible by 5
for i in range(1, 51):
    if i % 5 == 0: print(i)

 19. Print numbers divisible by 3
for i in range(1, 31):
    if i % 3 == 0: print(i)

 20. Print numbers greater than 5
for i in range(1, 11):
    if i > 5: print(i)

 21. Print numbers less than 5
for i in range(1, 11):
    if i < 5: print(i)

 22. Print positive numbers
for i in [-3, -1, 0, 2, 5]:
    if i > 0: print(i)

 23. Print negative numbers
for i in [-3, -1, 0, 2, 5]:
    if i < 0: print(i)

 24. Count numbers from 1 to 10
print(len(list(range(1, 11))))

 25. Find the largest number
print(max([10, 25, 7, 40, 15]))

 26. Find the smallest number
print(min([10, 25, 7, 40, 15]))

 27. Print factorial of 5 using a loop
fact = 1
for i in range(1, 6): fact *= i
print(fact)

 28. Print factorial of 7 using a loop
fact = 1
for i in range(1, 8): fact *= i
print(fact)

 29. Count vowels in a word
print(sum(1 for ch in "education" if ch in "aeiou"))

 30. Count letters in a word
print(sum(1 for ch in "Python"))

 31. Print a list with index
for i, item in enumerate(["A", "B", "C"]): print(i, item)

 32. Print the first five multiples of 6
for i in range(1, 6): print(6*i)

 33. Print a countdown
for i in range(5, 0, -1): print(i)

 34. Print numbers using while loop
i = 1
while i <= 10: print(i); i += 1

 35. Print even numbers using while loop
i = 2
while i <= 20: print(i); i += 2

 36. Print odd numbers using while loop
i = 1
while i < 20: print(i); i += 2

 37. Print numbers from 10 to 1 using while
i = 10
while i > 0: print(i); i -= 1

 38. Print a word three times
for i in range(3): print("Hello")

 39. Print stars five times
for i in range(5): print("*")

 40. Print a simple number pattern
for i in range(1, 6): print(str(i)*i)

 41. Print a square pattern
for i in range(5): print("*****")

 42. Print a triangle pattern
for i in range(1, 6): print("*"*i)

 43. Print reverse triangle
for i in range(5, 0, -1): print("*"*i)

 44. Print the alphabet A to E
for ch in "ABCDE": print(ch)

 45. Print numbers divisible by 2 or 3
for i in range(1, 21):
    if i % 2 == 0 or i % 3 == 0: print(i)

 46. Print numbers not divisible by 2
for i in range(1, 11):
    if i % 2 != 0: print(i)

 47. Double numbers from 1 to 10
for i in range(1, 11): print(i*2)

 48. Add numbers in a list
total = 0
for i in [10, 20, 30, 40]: total += i
print(total)

 49. Print squares of even numbers
for i in range(2, 11, 2): print(i**2)

 50. Print numbers until 5 using break
for i in range(1, 11):
    if i > 5: break
    print(i)