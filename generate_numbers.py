import random

# Function to create a file

def generate_numbers_file(filename, num_numbers, min_value, max_value):
    """Generates a file with random numbers."""
    with open(filename, "w") as f:
        for _ in range(num_numbers):
            number = random.randint(min_value, max_value)
            f.write(f"{number}\n")   # Each number followed by a newline character
    print(f"File '{filename}' with {num_numbers} random numbers generated.")
  
# Create a numbers.txt file with this function  
generate_numbers_file("numbers.txt", 1000, 1000, 10000000)
generate_numbers_file("largeNumbers.txt", 1000, 1000000, 10000000000)
generate_numbers_file("smallNumbers.txt", 1000, 1, 10000)

