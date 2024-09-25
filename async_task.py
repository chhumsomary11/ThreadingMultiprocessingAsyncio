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
    print("Async I/O tasks completed.")


