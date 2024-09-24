import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import multiprocessing
import asyncio


def main():
    # Step 1: Generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)
    generate_numbers.generate_numbers_file("largeNumbers.txt", 10000, 100000, 10000000000)
    generate_numbers.generate_numbers_file("smallNumbers.txt", 10000, 1, 1000000)


    
    # Step 2: Read numbers from file
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Step 3: Run multiprocessing task to find primes
    print("Running multiprocessing task...")
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    print(f"Prime numbers found: {primes}")

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    file_names = ["numbers.txt", "smallNumbers.txt", "largeNumbers.txt"]

    threading_task.run_io_tasks(file_names, 3)

    # Step 5: Run async tasks
    print("Running async I/O tasks to write primes to files...")
    prime_chunks = [primes[i:i+5] for i in range(0, len(primes), 5)]  # Chunk size of 5
    file_data_pairs = [
        (f"numbers.txt", chunk) 
        for i, chunk in enumerate(prime_chunks)
    ]
    
    asyncio.run(async_task.run_async_tasks(file_data_pairs, duration_per_task=2))

if __name__ == "__main__":
    main()
