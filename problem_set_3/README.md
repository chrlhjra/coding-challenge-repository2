# Longest Increasing Subsequence

## Problem Description
Given a list of numbers, find the length of the longest increasing subsequence.

## Solution
The solution uses dynamic programming. It creates a list `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. By comparing each element with the elements before it and updating `dp` accordingly, the solution finds the length of the longest increasing subsequence.

## Instructions to Run the Code
1. Make sure you have Python installed on your system.
2. Save the code in a file with a .py extension (e.g., longest_subsequence.py).
3. Open a terminal or command prompt and navigate to the directory where the file is saved.
4. Run the following command to execute the code: python longest_subsequence.py
5. The program will output the length of the longest increasing subsequence for the given list of numbers.