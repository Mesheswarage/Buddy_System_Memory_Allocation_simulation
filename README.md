# Memory Management Program

This program simulates memory allocation and deallocation using a buddy memory allocation system. It dynamically allocates and merges memory blocks based on the nearest power of 2 to optimize memory usage.

## Features
- **Memory Initialization**: Start with a specified total memory size.
- **Memory Allocation**: Allocate memory for processes of specific sizes, splitting memory blocks as needed.
- **Memory Deallocation**: Deallocate memory and merge adjacent free blocks of the same size.
- **Visual Display**: View the status of all memory slots (free or allocated) along with their sizes and starting addresses.

## How It Works
1. **Nearest Power of 2**: The program rounds up block sizes to the nearest power of 2 to ensure efficient memory allocation.
2. **Buddy System**:
   - If a free block is larger than the requested size, it is split into smaller blocks.
   - Deallocated blocks are merged with their "buddies" (adjacent blocks of the same size) to form larger blocks.
3. **Memory Slots Display**: The program sorts and displays memory blocks, showing their status (free or allocated), size, and starting address.

## How to Run
1. Ensure you have Python installed on your system.
2. Copy the code into a file named `memory_manager.py`.
3. Run the program using:
   ```bash
   python memory_manager.py
   ```
4. Follow the on-screen prompts to allocate or deallocate memory.

## Functions
### `allocate_initial_memory(total_memory_size)`
Initializes the free and allocated memory lists.
- **Parameters**: Total memory size (integer).
- **Returns**: Free memory and allocated memory lists.

### `allocate(free_memory, allocated_memory, process_size)`
Allocates memory for a process of the specified size.
- **Parameters**:
  - `free_memory`: List of free memory blocks.
  - `allocated_memory`: List of allocated memory blocks.
  - `process_size`: Size of the process to allocate.
- **Returns**: Starting address of the allocated block or `None` if allocation fails.

### `deallocate(free_memory, allocated_memory, deallocate_address)`
Deallocates memory at the specified starting address and merges free blocks if possible.
- **Parameters**:
  - `free_memory`: List of free memory blocks.
  - `allocated_memory`: List of allocated memory blocks.
  - `deallocate_address`: Starting address of the block to deallocate.
- **Returns**: Updated free memory list.

### `merge_free_memory(free_memory)`
Merges adjacent free blocks of the same size.
- **Parameters**: List of free memory blocks.
- **Returns**: Updated free memory list.

### `nearest_power_of_2(size)`
Finds the smallest power of 2 greater than or equal to the given size.
- **Parameters**: Size (integer).
- **Returns**: Nearest power of 2 (integer).

### `print_memory(free_memory, allocated_memory)`
Displays the current status of memory blocks.
- **Parameters**:
  - `free_memory`: List of free memory blocks.
  - `allocated_memory`: List of allocated memory blocks.

## Example Interaction
```plaintext
Memory Slots (Size - Status):
1024 - free - Starting address - 0

Would you like to allocate or deallocate memory? (Type 'allocate', 'deallocate', or 'exit'): allocate
Enter the process size to allocate: 200
Process of size 200 allocated at address 0

Memory Slots (Size - Status):
512 - free - Starting address - 512
256 - free - Starting address - 256
256 - allocated - Starting address - 0
...
```
