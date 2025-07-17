#!/bin/bash

# -------------------------------
# Bash Script: Factorial Calculator
# -------------------------------
# This script calculates the factorial of a number
# passed as a command-line argument.
#

# Check if an argument is given
if [ -z "$1" ]; then
  echo "Error: No input provided."
  echo "Usage: $0 <positive integer>"
  exit 1
fi

# Check if input is a non-negative whole number
if ! [[ "$1" =~ ^[0-9]+$ ]]; then
  echo "Error: '$1' is not a valid non-negative integer."
  echo "Please enter a positive whole number like 5 or 10."
  exit 1
fi

num=$1
factorial=1

# Loop to calculate factorial
for (( i=2; i<=num; i++ ))
do
  factorial=$((factorial * i))
done

echo "Factorial of $num is $factorial"
