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