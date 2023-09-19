import string

nums = [x for x in range(11)]
print(nums)

sq = [x*x for x in nums]
print(sq)


alphabet = "Hello"
vowels = [x for x in alphabet if x in ["a", "e", "i", "o", "u"]]
print(vowels)


# Filtering
odd = [num for num in nums if num % 2 != 0]
print(odd)

words = ["apple", "banana", "cherry", "date", "fig"]
more_than_5 = [word for word in words if len(word) > 5]
print(more_than_5)

contains_a = [word for word in words if 'a' in word]
print(contains_a)



# List Comprehension with Conditionals:
# Write a list comprehension to create a list of squares for even numbers and cubes for odd numbers in a given list of integers.
sq_for_odd_and_cube_for_even = [num*num if num% 2 == 0 else num*num*num for num in nums]
print(sq_for_odd_and_cube_for_even)

div_by_both_3_and_5 = [num for num in range(1,101) if num % 5 == 0 and num % 3 == 0]
print(div_by_both_3_and_5)

# Nested List Comprehension:
mul_table = [ [f"{i} * {j} = {i*j}" for i in range(2,11) ] for  j in range(1, 11)]
for a in mul_table:
    print(" ".join(a))


# Words that start with vowel
sentence = "An apple a day keeps the doctor away"
start_with_vowel = [word for word in sentence.split() if word[0].lower() in "aeiou"]
print(start_with_vowel)