#!/bin/bash


# Define Colours
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

merge_daily_transactions() {
    input_folder="storage/daily_transactions"
    output_folder="storage"
    
    transactions=()
    for file_name in "$input_folder"/*; do
        transactions+=("$(cat "$file_name")")
    done

    merged_file_path="$output_folder/merged_daily_transactions.txt"
    printf "%s\n" "${transactions[@]}" > "$merged_file_path"
} 

# Check if distribution-system.exe exists in the current directory
if [ ! -f "distribution-system.exe" ]; then
    echo -e "${RED}Error: distribution-system.exe not found in the current directory. Make sure to do ${GREEN}make build${NC} before running tests"
    exit 1
fi
list_subdirs() {
    for dir in "$1"/*/
    do
        dir=${dir%*/}
        echo "${dir}"
    done
}

# Arrays to hold the directories
declare -a dirs

if [ ! -d "storage/daily_transactions" ]; then
    mkdir "storage/daily_transactions"
fi

# Remove existing daily transaction files
rm -f storage/daily_transactions/dtf_test_*

# Parse all arguments
for arg in "$@"
do
    
    if [ "$arg" == "all" ]; then
        for dir in testing/cases/*/
        do
            dirs+=($(list_subdirs "$dir"))
        done
    fi
    
done

for dir in "${dirs[@]}"; do
    result_dir="testing/tests/${dir#testing/cases/}_$(date +%Y%m%d%H%M%S)"
    mkdir -p "$result_dir"

    # Read the first line of the input file as the command
    cmd=$(head -n 1 "$dir/input.txt")

    # Create a named pipe
    mkfifo pipe

    # Start the system with all commands from the input file in the background
    sed '1d' "$dir/input.txt" | tee "$result_dir/test.txt" > pipe &

    # Run the command with the named pipe as input
    $cmd < pipe 2>&1 | tee -a "$result_dir/results.txt"

    # Remove the named pipe
    rm pipe

    # Copy the output.txt file
    cp "$dir/output.txt" "$result_dir/"

    # Copy the daily transaction file if it exists
    if [ -f "$dir/daily_transaction.txt" ]; then
        cp -p "$(find storage/daily_transactions -maxdepth 1 -type f -printf '%T@ %p\n' | sort -n | tail -1 | cut -f2- -d' ')" "$result_dir/merged_daily_transactions.txt"
        cp "$dir/daily_transaction.txt" "$result_dir/"
    fi

    # Copy the merged daily transaction file to the daily transactions directory
    cp "$result_dir/merged_daily_transactions.txt" "storage/daily_transactions/dtf_$(date +%Y%m%d%H%M%S).txt"

    # Merge the daily transactions
    merge_daily_transactions
done