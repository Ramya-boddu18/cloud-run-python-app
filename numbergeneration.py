import random

def generate_random_numbers(count, start, end):
  """Generates a list of random numbers within a specified range.

  Args:
    count: The number of random numbers to generate.
    start: The starting value of the range (inclusive).
    end: The ending value of the range (inclusive).

  Returns:
    A list of random integers.
  """
  if not isinstance(count, int) or count < 0:
    raise ValueError("Count must be a non-negative integer.")
  if not isinstance(start, int) or not isinstance(end, int):
    raise TypeError("Start and end must be integers.")
  if start > end:
    raise ValueError("Start must be less than or equal to end.")

  random_numbers = []
  for _ in range(count):
    random_numbers.append(random.randint(start, end))
  return random_numbers

# Generate 7 random numbers between 1 and 50
random_numbers = generate_random_numbers(7, 1, 50)
print(random_numbers)

#Example of error handling.
try:
  random_numbers = generate_random_numbers(-1, 1, 50)
except ValueError as e:
  print(f"Error: {e}")

try:
  random_numbers = generate_random_numbers(7, 51, 1)
except ValueError as e:
  print(f"Error: {e}")

try:
  random_numbers = generate_random_numbers(7, 1.5, 50)
except TypeError as e:
  print(f"Error: {e}")