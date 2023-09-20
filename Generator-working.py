def square_generator(n):
    for i in range(n):
        print(f"Generator is at state {i} and about to yield {i**2}")
        yield i**2
        print(f"Generator has yielded {i**2}, now pausing...")

# Create a generator object
gen = square_generator(5)

# Manually iterate through the generator to observe the pausing
gen_iterator = iter(gen)
for _ in range(5):
    value = next(gen_iterator)
    print(f"Main program received {value}")
