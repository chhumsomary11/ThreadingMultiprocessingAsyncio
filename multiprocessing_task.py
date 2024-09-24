import multiprocessing
import math

# Function to check if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to process a chunk of numbers to check if they are prime
def check_prime_chunk(numbers):
    """Check if numbers in the chunk are prime."""
    return [num for num in numbers if is_prime(num)]

# Function to split data into chunks and process them using multiprocessing
def find_primes_in_range(numbers, chunk_size):
    """Divide numbers into chunks and process them using multiprocessing."""
    # Create chunks of data
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Use multiprocessing Pool to process each chunk in parallel
    with multiprocessing.Pool() as pool:
        result_chunks = pool.map(check_prime_chunk, chunks)
    
    # Combine results from all chunks
    primes = [prime for result in result_chunks for prime in result]
    return primes

# Example function to read numbers from file
def read_numbers_from_file(file_path):
    """Read numbers from the file."""
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    return numbers

# Main function to demonstrate multiprocessing
if __name__ == "__main__":
    # Example file path (replace with the URL download part)
    file_path = "numbers.txt"  # This should be the path to the numbers.txt file you downloaded

    # Read the numbers from the file
    numbers = read_numbers_from_file(file_path)

    # Define the chunk size (adjust as per the number of CPUs available)
    chunk_size = len(numbers) // multiprocessing.cpu_count()

    # Find all primes in the numbers using multiprocessing
    primes = find_primes_in_range(numbers, chunk_size)

    # Output the number of primes found
    print(f"Found {len(primes)} prime numbers.")
    print(chunk_size)
    
    
      # Split primes into chunks for async file writing
    prime_chunks = [primes[i:i+5] for i in range(0, len(primes), 5)]  # Chunk size of 5
    print(prime_chunks)
