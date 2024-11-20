import os
import random
import string
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def generate_file_with_palindrome(file_path):
    # Create a random string with a 5-letter palindrome embedded in it
    letters = string.ascii_uppercase
    palindrome = ''.join(random.choices(letters, k=2)) + ''.join(random.choices(letters, k=1)) + ''.join(random.choices(letters, k=2))
    random_string = ''.join(random.choices(letters, k=995)) + palindrome
    random_string = ''.join(random.sample(random_string, len(random_string)))  # Shuffle the string
    
    with open(file_path, 'w') as file:
        file.write(random_string)

def check_palindrome(s):
    # Check for any 5-letter palindromes in the string
    for i in range(len(s) - 4):
        substring = s[i:i + 5]
        if substring == substring[::-1]:  # Check if the substring is a palindrome
            return 1  # Found a palindrome
    return 0  # No palindrome found

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return check_palindrome(content)

def create_text_files(num_files=100000):
    # Create the specified number of text files with random strings
    os.makedirs('text_files', exist_ok=True)
    for i in range(num_files):
        file_path = os.path.join('text_files', f'file_{i+1}.txt')
        generate_file_with_palindrome(file_path)

def parallel_palindrome_check(num_files=100000):
    results = []
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_file, os.path.join('text_files', f'file_{i+1}.txt')) for i in range(num_files)]
        for future in as_completed(futures):
            results.append(future.result())
    return results

def serial_palindrome_check(num_files=100000):
    results = []
    for i in range(num_files):
        file_path = os.path.join('text_files', f'file_{i+1}.txt')
        result = process_file(file_path)
        results.append(result)
    return results

def main():
    num_files = 100000  # Large number of files for testing
    create_text_files(num_files)

    # Serial check
    start_time = time.time()
    serial_results = serial_palindrome_check(num_files)
    serial_time = time.time() - start_time
    print(f'Serial results: {serial_results[:100]}...')  # Display first 100 results for brevity
    print(f'Serial processing time: {serial_time:.4f} seconds')

    # Parallel check
    start_time = time.time()
    parallel_results = parallel_palindrome_check(num_files)
    parallel_time = time.time() - start_time
    print(f'Parallel results: {parallel_results[:100]}...')  # Display first 100 results for brevity
    print(f'Parallel processing time: {parallel_time:.4f} seconds')

    # Calculate speedup and efficiency
    speedup = serial_time / parallel_time
    efficiency = speedup / os.cpu_count()  # Efficiency relative to the number of cores
    print(f'Speedup: {speedup:.2f}')
    print(f'Efficiency: {efficiency:.4f}')

if __name__ == '__main__':
    main()
