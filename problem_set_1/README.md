# Problem Set: Palindrome Pair 

## Problem Description
Given a list of words, find all pairs of words that form palindromes when concatenated. A palindrome is a word or phrase that reads the same forwards and backwards.

## Solution Overview
The solution uses a complete search approach to find all pairs of words that form palindromes when concatenated. It follows these steps:

1. Initialize an empty list called `pairs` to store the pairs of words that form palindromes.
2. Iterate over all possible pairs of words in the given list using nested loops.
3. For each pair of words, check if the indices are different to avoid comparing a word with itself.
4. If the indices are different, concatenate the words and check if the concatenated string is equal to its reverse.
5. If the concatenated string is a palindrome, append the pair of indices to the `pairs` list.
6. After checking all possible pairs, the `pairs` list will contain the indices of the word pairs that form palindromes.
7. The `concat` method is used to print the actual pairs of words that form palindromes by concatenating the words corresponding to the indices stored in each pair.

## Instructions to Run the Code
1. Ensure Python is installed.
2. Save the code in a Python file.
3. Run the file using the command: python filename.py.
4. The code will output the pairs of words that form palindromes.