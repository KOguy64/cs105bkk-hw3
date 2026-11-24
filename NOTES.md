# HW3 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
Tried generating the report (in write_report) as a lot of list comprehensions
Cited the walks.py README directly when writing tests

## What broke, and how did you fix it?
Didn't work since walks is a generator and returns a single-use iterator. Fixed it by caching it through steps_per_day (since we don't need
any other information)
Called good_row() directly in the tests. That broke, but I still used copy.deepcopy so that the test wouldn't pass because of pass by reference

## What would you do differently next time?
Read the instructions more thoroughly, and take the time to understand generators and decorators more before going through 
