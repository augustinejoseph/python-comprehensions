# Comprehensions

## Difference between Comprehension, Lambda, map() and filter()

| Feature |	Python comprehensions |	Lambda expressions |	map() |	filter() |
| :--- | :--- | :--- | :--- | :---|
|Definition |	A concise and expressive way to create new sequences from existing sequences. |	A function that is defined without a name. |	A function that applies a function to each element of an iterable and returns a new iterable. |	A function that filters an iterable and returns a new iterable containing only the elements that satisfy a condition. |
| Syntax |	[expression for x in iterable if condition] |	lambda arguments: expression |	map(function, iterable) |	filter(function, iterable)

## Comprehension
* Comprehensions can be used to write complex code in a single line.
* They are efficient. Comprehensions are often faster than equivalent code that uses loops.
* They are flexible. Comprehensions can be used to create a wide variety of sequences, including lists, dictionaries, and sets.

```
[expression for x in iterable if condition]

nums = [1,2,3,4,5,6,7,8,9,10]
[x ** x for x in nums if x %2 ==0]
```

## Differences between generator, set, list, and dictionary comprehensions in Python:

| Comprehension Type     | Syntax                  | Output Type      | Purpose                                       | Lazy Evaluation | Example                                                   |
|------------------------|-------------------------|------------------|-----------------------------------------------|-----------------|-----------------------------------------------------------|
| List Comprehension     | `[expression for item in iterable if condition]`  | List             | Create a new list based on an iterable with optional filtering. | No              | `[x**2 for x in range(10) if x % 2 == 0]`                |
| Set Comprehension      | `{expression for item in iterable if condition}`   | Set              | Create a new set with unique elements from an iterable with optional filtering. | No              | `{x % 5 for x in range(10)}`                               |
| Dictionary Comprehension | `{key_expression: value_expression for item in iterable if condition}` | Dictionary | Create a new dictionary by specifying key-value pairs based on an iterable with optional filtering. | No | `{x: x**2 for x in range(10) if x % 2 == 0}` |
| Generator Comprehension | `(expression for item in iterable if condition)`   | Generator Object | Create an iterable generator for on-the-fly value generation from an iterable with optional filtering. | Yes | `(x**2 for x in range(10) if x % 2 == 0)`                |

Key Points:

- List comprehensions, set comprehensions, and dictionary comprehensions return lists, sets, and dictionaries, respectively, which store all values in memory.
- Generator comprehensions return generator objects, which are memory-efficient and use lazy evaluation.
- Generator comprehensions are useful when working with large datasets or when you want to generate values on-the-fly.
- All types of comprehensions support optional filtering using the `if` clause.
- Sets and dictionary comprehensions ensure uniqueness of values and keys, respectively.



# QUESTIONS
#### Question:
Can you use a generator comprehension to generate an infinite sequence of numbers?

#### Answer:
Yes, you can use a generator comprehension to generate an infinite sequence of numbers. For example, to generate an infinite sequence of natural numbers, you can write `(x for x in itertools.count(start=1))` using the itertools.count function.