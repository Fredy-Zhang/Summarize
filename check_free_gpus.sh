#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

username=$1

# Fetch the list of servers with running jobs for user 'fredy'
servers=$(squeue -u $username | awk '$5=="R"{print $8}')

# Prepare a file to store the results
result_file="gpu_usage_summary.txt"
echo "Free GPU servers summary:" > "$result_file"

check_gpu_usage() {
    server=$1
    echo "Checking GPU usage on $server..."

    # SSH into the server and run nvidia-smi, then check if any GPU has low memory usage indicating it is free
    output=$(ssh $username@$server 'nvidia-smi --query-gpu=name,memory.used --format=csv,noheader' | awk -F, '{if ($2+0 < 100) print "free"}')

    # Check if the output contains "free"
    if [[ $output == *"free"* ]]; then
        echo "$server has free GPUs" >> "$result_file"
    fi
}


# Loop through each server and check the GPU usage
for server in $servers
do
    check_gpu_usage $server
done

# Display the results
cat "$result_file"
