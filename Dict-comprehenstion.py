cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
populations = [8336817, 39776830, 2716000, 2320268, 1680992, 1584138]


sq_nums = {num: num * num for num in range(1, 6)}
print(sq_nums)

words_with_len = {word: len(word) for word in cities}
print(words_with_len)

# Filtering with Dictionary Comprehension:
scores = {"Alice": 95, "Bob": 88, "Charlie": 92, "David": 78, "Eva": 97}
score_above_90 = {student: score for student, score in scores.items() if score > 90}
print(score_above_90)

exclude_below_80 = {
    name: mark for name, mark in scores.items() if mark not in range(1, 81)
}
print(exclude_below_80)


# Dictionary Comprehension with Conditionals:
celsius_temperatures = {"New York": 20, "Los Angeles": 25, "Chicago": 15, "Houston": 30}
in_fahrenheit = {
    city: (temp * 9 / 5) + 32 for city, temp in celsius_temperatures.items()
}
print(in_fahrenheit)

ever_or_odd = {num: "even" if num % 2 == 0 else "odd" for num in range(0, 11)}
print(ever_or_odd)

names = ["Alice", "Bob", "Charlie", "Eby"]
ages = [25, 30, 35, 7]
is_adult = {name : "is adult" if age >18 else "not adult" for name,age in zip(names,ages)}
print(is_adult)


# Combining Comprehensions:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
older_than_25 = {name: age for name ,age in zip(names,ages) if age > 25}
print(older_than_25)


# Advanced Dictionary Comprehension:
students = [{"name": "Alice", "scores": [85, 92, 88]},
            {"name": "Bob", "scores": [78, 90, 85]},
            {"name": "Charlie", "scores": [92, 94, 89]}]
avg_score = {student["name"] : sum(student["scores"])/len(student["scores"]) for student in students}
print(avg_score)


books = [
    {"title": "Book1", "author": "Author1", "year": 2020},
    {"title": "Book2", "author": "Author2", "year": 2019},
    {"title": "Book3", "author": "Author1", "year": 2021},
    {"title": "Book4", "author": "Author3", "year": 2018},
    {"title": "Book5", "author": "Author2", "year": 2017},
]
all_books_by_author = {book["author"]: [b["title"] for b in books if b["author"] == book["author"]] for book in books}
print(all_books_by_author)