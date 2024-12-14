import math
import tkinter as tk
# Initialize Tkinter window
root = tk.Tk()
root.title("Memory Allocation Visualization")
root.geometry("400x600")

# Define colors for different block sizes
COLORS = {
    256: "#FFEB3B",  # Yellow for 256 block size
    512: "#4CAF50",  # Green for 512 block size
    1024: "#2196F3",  # Blue for 1024 block size
    2048: "#FF5722"  # Red for 2048 block size
}

# Memory visualization canvas
canvas = tk.Canvas(root, width=400, height=600, bg="white")
canvas.pack()

def nearest_power_of_2(size):
    """Get the smallest power of 2 that is greater than or equal to the given size."""
    return 2 ** math.ceil(math.log2(size))

def plot_memory(free_memory, allocated_memory, total_memory_size):
    canvas.delete("all")  # Clear the canvas before redrawing

    # Draw the memory blocks in a vertical layout
    current_y = 20  # Starting Y position for drawing blocks
    for block_size, start_address in free_memory:
        color = COLORS.get(block_size, "#D3D3D3")  # Default to light gray if no specific color
        canvas.create_rectangle(
            50, current_y, 350, current_y + 30,
            fill=color, outline="black"
        )
        canvas.create_text(200, current_y + 15, text=f"{block_size} - Free", fill="black")
        current_y += 40

    # Draw allocated memory blocks
    for block_size, start_address in allocated_memory:
        color = COLORS.get(block_size, "#D3D3D3")  # Default to light gray if no specific color
        canvas.create_rectangle(
            50, current_y, 350, current_y + 30,
            fill=color, outline="black"
        )
        canvas.create_text(200, current_y + 15, text=f"{block_size} - Allocated", fill="black")
        current_y += 40

    # Update the Tkinter window
    root.after(100, root.update())  # Forces Tkinter to update the canvas

# Example memory management functions
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
            plot_memory(free_memory, allocated_memory, total_memory)  # Update visualization after allocation
            return allocated_address
    return None  # Unable to allocate memory

def deallocate(free_memory, allocated_memory, deallocate_address):
    for i, (block_size, start_address) in enumerate(allocated_memory):
        if start_address == deallocate_address:
            deallocated_block = allocated_memory.pop(i)
            free_memory.append(deallocated_block)
            free_memory.sort()  # Merge free memory
            plot_memory(free_memory, allocated_memory, total_memory)  # Update visualization after deallocation
            return free_memory
    return free_memory  # Address not found, no change

# Simulate memory allocation and visualization
total_memory = 2048
free_memory, allocated_memory = allocate_initial_memory(total_memory)

# Initial visualization
plot_memory(free_memory, allocated_memory, total_memory)

# Simulate memory allocation and update the visualization
root.after(500, allocate, free_memory, allocated_memory, 200)  # Allocate 200 memory
root.after(1000, allocate, free_memory, allocated_memory, 256)  # Allocate 256 memory
root.after(1500, deallocate, free_memory, allocated_memory, 0)  # Deallocate memory at address 0

# Start the Tkinter main loop
root.mainloop()
