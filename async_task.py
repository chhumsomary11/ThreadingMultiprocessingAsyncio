import asyncio

# Simulate asynchronous file writing
async def async_write_to_file(filename, data, duration):
    """Simulates writing data to a file asynchronously."""
    print(f"Starting to write to {filename}...")
    await asyncio.sleep(duration)  # Simulate the time taken to write (non-blocking)
    
    # Write the data to the file
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
    
    print(f"Finished writing to {filename}!")

# Function to run multiple asynchronous file write tasks
async def run_async_tasks(file_data_pairs, duration_per_task):
    """Run multiple asynchronous file write tasks."""
    tasks = []
    
    # Create an async task for each file
    for filename, data in file_data_pairs:
        task = asyncio.create_task(async_write_to_file(filename, data, duration_per_task))
        tasks.append(task)
    
    # Run all async tasks concurrently
    await asyncio.gather(*tasks)

# Main function to write primes asynchronously
if __name__ == "__main__":
    # Assume primes were found in Part 1
    primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]  # Example primes list

    # Split primes into chunks for multiple file writing
    prime_chunks = [primes[i:i+5] for i in range(0, len(primes), 5)]  # Split into chunks of 5

    # Example file names for each chunk
    file_data_pairs = [
        ("data/processed_data/primes_1.txt", prime_chunks[0]),
        ("data/processed_data/primes_2.txt", prime_chunks[1])
    ]

    # Simulate asynchronous file writing with a delay of 2 seconds for each file
    asyncio.run(run_async_tasks(file_data_pairs, 2))
