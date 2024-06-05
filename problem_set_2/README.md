# Problem Set X: Valid Parentheses

## Problem Description
Given a string containing only parentheses '(' and ')', determine if the string has valid parentheses. A string is considered to have valid parentheses if all opening parentheses have a corresponding closing parenthesis in the correct order.

## Solution Overview
The solution uses a stack-like approach to validate the parentheses. It maintains a list to keep track of the indices of opening parentheses. Whenever an opening parenthesis is encountered, its index is pushed onto the stack. When a closing parenthesis is encountered, it checks if there is a matching opening parenthesis by popping the last index from the stack. If the stack is empty when a closing parenthesis is encountered or if there are remaining indices in the stack after processing all the characters, the string is considered invalid. Otherwise, the string is considered valid.

## Instructions to Run the Code
1. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory where the file is saved.
4. Run the code by executing the command: `python valid_parentheses.py`.
5. The output will be either "True" if the string has valid parentheses or "False" if the string has invalid parentheses.