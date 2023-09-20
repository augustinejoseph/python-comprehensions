nums = (x for x in range(1, 101))


even_nums = (num for num in nums if num%2 == 0)
print(list(even_nums))

sentence = "This is a sample sentence for generator comprehension practice."
word_lengths = (len(word) for word in sentence.split())
print(list(word_lengths))

words = ["radar", "python", "level", "racecar", "hello", "madam"]
palindromic_word = (word for word in words if word == word[::-1])
print(list(palindromic_word))
