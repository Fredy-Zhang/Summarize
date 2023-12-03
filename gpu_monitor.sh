#!/bin/bash

# Output file
log_file="gpu_memory_log.txt"

# Clear the log file if it exists or create a new one
> "$log_file"

# Infinite loop to monitor GPU memory every 1 second
while true; do
    # Run nvidia-smi to monitor GPU memory and append the result to the log file
    nvidia-smi --query-gpu=memory.used --format=csv >> "$log_file"
    
    # Sleep for 1 second
    sleep 1
done

