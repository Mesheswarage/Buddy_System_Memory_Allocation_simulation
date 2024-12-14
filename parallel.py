import math
import threading

def merge_free_memory(free_memory):
    updated_free_memory = []
    for block_size, start_address in free_memory:
        updated_free_memory.append((nearest_power_of_2(block_size), start_address))

    free_memory = updated_free_memory

    free_memory.sort(key=lambda x: x[0])  

    while True:
        merged = False  
        new_free_memory = []  
        i = 0

        while i < len(free_memory):
            block_size, start_address = free_memory[i]
            same_size_index = None
            for j in range(i + 1, len(free_memory)):
                if free_memory[j][0] == block_size:
                    same_size_index = j
                    break

            if same_size_index is not None:
                _, other_start_address = free_memory[same_size_index]
                larger_block_start = min(start_address, other_start_address)
                new_free_memory.append((block_size * 2, larger_block_start))
                free_memory.pop(same_size_index) 
                merged = True 
            else:
                new_free_memory.append((block_size, start_address))

            i += 1  
        free_memory = new_free_memory

        if not merged:  
            break
    return free_memory

def nearest_power_of_2(size):
    """Get the smallest power of 2 that is greater than or equal to the given size."""
    return 2 ** math.ceil(math.log2(size))

def print_memory(free_memory, allocated_memory):
    print("\nMemory Slots (Size - Status):")
    all_slots = []

    for block_size, start_address in free_memory:
        all_slots.append((nearest_power_of_2(block_size), 'free', start_address))
    for block_size, start_address in allocated_memory:
        all_slots.append((nearest_power_of_2(block_size), 'allocated', start_address))

    all_slots.sort(key=lambda x: x[0], reverse=True)

    for block_size, status, address in all_slots:
        print(f"{block_size} - {status} - Starting address - {address}")

def allocate_initial_memory(total_memory_size):
    return [(total_memory_size, 0)], []

def allocate(free_memory, allocated_memory, process_size):
    for i, (block_size, start_address) in enumerate(free_memory):
        if block_size >= process_size:
            allocated_address = start_address
            free_memory.pop(i)
            allocated_memory.append((process_size, allocated_address))  
            while block_size // 2 >= process_size:
                half_block = block_size // 2
                free_memory.append((half_block, start_address + half_block))
                free_memory.sort()
                block_size = half_block
            print(f"Process of size {process_size} allocated at address {allocated_address}")
            return allocated_address
    print(f"Unable to allocate memory for process of size {process_size}")
    return None

def deallocate(free_memory, allocated_memory, deallocate_address):
    for i, (block_size, start_address) in enumerate(allocated_memory):
        if start_address == deallocate_address:
            deallocated_block = allocated_memory.pop(i)
            free_memory.append(deallocated_block)
            free_memory = merge_free_memory(free_memory) 
            print(f"Deallocated memory at address {deallocate_address}")
            return free_memory


total_memory = 1024  
free_memory, allocated_memory = allocate_initial_memory(total_memory)

def allocate_memory_for_process(free_memory, allocated_memory, process_size):
    allocate(free_memory, allocated_memory, process_size)

while True:
    print_memory(free_memory, allocated_memory)

    action = input("\nWould you like to allocate or deallocate memory? (Type 'allocate', 'deallocate', or 'exit'): ").strip().lower()

    if action == 'allocate':
        process_count = int(input("Enter the number of processes to allocate memory for: ").strip())
        
        threads = []
        for _ in range(process_count):
            process_size = int(input(f"Enter the process size for process {_ + 1}: ").strip())
            thread = threading.Thread(target=allocate_memory_for_process, args=(free_memory, allocated_memory, process_size))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif action == 'deallocate':
        deallocate_address = int(input("Enter the address to deallocate: ").strip())
        free_memory = deallocate(free_memory, allocated_memory, deallocate_address)
    
    elif action == 'exit':
        break
    
    else:
        print("Invalid action. Please type 'allocate', 'deallocate', or 'exit'.")
