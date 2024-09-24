import threading
import time

# Simulate an I/O-bound task, such as downloading or processing a file
def simulate_io_task(file_name, duration):
    """Simulates an I/O-bound task (e.g., downloading or processing a file)."""
    print(f"Starting task for {file_name}...")
    time.sleep(duration)  # Simulate a time-consuming I/O operation
    print(f"Finished task for {file_name}!")

# Function to run multiple I/O tasks using threading
def run_io_tasks(file_names, duration_per_task):
    """Run multiple I/O-bound tasks concurrently using threads."""
    threads = []
    
    # Create and start a thread for each file
    for file_name in file_names:
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration_per_task))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Example file names (these could be chunk names or files hosted on GitHub)
    file_names = ["numbers.txt", "smallNumbers.txt", "largeNumbers.txt"]
    
    # Simulate running I/O tasks for each file concurrently (e.g., 3 seconds per task)
    run_io_tasks(file_names, 3)
