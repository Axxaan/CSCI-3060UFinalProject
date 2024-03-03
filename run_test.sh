#!/bin/bash

# Define directories
test_cases_dir="TestCases"
output_dir="Outputs"
result_file="test_results.log"

# Ensure the 'TestCases' directory exists
if [ ! -d "$test_cases_dir" ]; then
    echo "Error: 'TestCases' directory does not exist."
    exit 1
fi

# Ensure the 'Outputs' directory exists
if [ ! -d "$output_dir" ]; then
    echo "Creating 'Outputs' directory..."
    mkdir -p "$output_dir"
fi

# Create or clear results file
echo "" > "$result_file"

# Loop over each test case directory
for dir in $test_cases_dir/*/; do
   
    test_case_name=$(basename "$dir")

    # Loop over each input file within the test case directory's 'Input' subdirectory
    for input_file in "$dir"Input/*.txt; do
        input_file_name=$(basename "$input_file")

        # Run the program with input and output files as arguments
        echo "Running test for $input_file_name in $test_case_name..."

        expected_output="$dir"Output/"${input_file_name%.txt}".txt
        actual_output="$output_dir/${test_case_name}${input_file_name%.txt}.out"

        ./FrontEnd/FrontEnd.exe "currentaccounts.txt" "availablegames.txt" "gamescollection.txt" "transout.atf" < "$input_file" > "$actual_output"

        # Compare the actual output with the expected output, ignoring all whitespace and blank lines
        if diff -B -w -q "$expected_output" "$actual_output" > /dev/null; then
            # If files are the same, log as passed and append the pass message to the actual_output file
            echo "Test case $test_case_name $input_file_name: PASSED" >> "$result_file"
            echo "Test case $test_case_name $input_file_name: PASSED" > "${actual_output}_temp"
            cat "$actual_output" >> "${actual_output}_temp"
            mv "${actual_output}_temp" "$actual_output"
        else
            # If files differ, log as failed
            echo "Test case $test_case_name $input_file_name: FAILED" >> "$result_file"
            # Append the fail statement at the start of the actual_output file
            echo "Test case $test_case_name $input_file_name: FAILED" > "${actual_output}_temp"
            # Append the diff output to the actual_output file
            diff -B -w "$expected_output" "$actual_output" >> "${actual_output}_temp"
            # Now prepend the initial fail message to the actual output file for clarity
            cat "$actual_output" >> "${actual_output}_temp"
            mv "${actual_output}_temp" "$actual_output"
        fi


    done
done

echo "All tests have been run. Results are saved in $result_file."
