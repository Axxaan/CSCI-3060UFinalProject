#!/bin/bash

# Define the number of times to run the daily script
NUM_RUNS=5

# Loop to run the daily script multiple times
for ((i = 1; i <= NUM_RUNS; i++)); do
    echo "Running daily script: Run $i"
    ./daily.sh
done



# Copy the Merged Daily Transactions file from the same Daily run
cp storage/merged_daily_transactions.txt phase6/

# Copy the New Available Games File after each of the five Daily runs made by your Weekly script
cp storage/available_games.txt phase6/

# Define the path to the cases folder
CASES_FOLDER="testing/cases"

# Define the path to the phase6 folder
PHASE6_FOLDER="phase6"

# Function to collect input.txt files
collect_input_files() {
    # Iterate through each subdirectory in the cases folder
    for category_folder in "$CASES_FOLDER"/*; do
        # Check if the item is a directory
        if [ -d "$category_folder" ]; then
            # Iterate through each subdirectory in the category folder
            for sub_folder in "$category_folder"/*; do
                # Check if the item is a directory
                if [ -d "$sub_folder" ]; then
                    # Check if the subdirectory contains an input.txt file
                    if [ -f "$sub_folder/input.txt" ]; then
                        # Print the category folder name
                        echo "Category: $(basename "$category_folder")"
                        # Print the subdirectory name
                        echo "Subdirectory: $(basename "$sub_folder")"
                        # Print the contents of the input.txt file
                        cat "$sub_folder/input.txt" >> "$PHASE6_FOLDER/combined_input.txt"
                        # Add a separator for clarity
                        echo "--------------------------------------------"
                    fi
                fi
            done
        fi
    done
}


# Collect and print the input files
collect_input_files