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