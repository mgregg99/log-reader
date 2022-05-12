# Log-Reader

## Goal

Write a script that reads the access.log file from an apache server, grabs all 4xx and 5xx errors and sorts them based on type first (all 4xx before 5xx) and date/time second. This means your output should have a list of 4xx errors and a list of 5xx errors, and all 4xx errors should be printed before any 5xx error prints. The individual lists should also be sorted by date, with the most recent entries at the bottom of the list and the oldest ones at the top. Use the access.log file in the same folder on Box as this file. Write this script in Python 3
