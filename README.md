# Python Interview Prep

This is a repo for me to practice data structures and algorithms using Python to prepare for technical interviews.

## General Notes on Python

- Iterables: anything you can use "```for``` ... ```in``` ..." on (lists,strings,files).
- Generators: functions that behave like iterables in which you can iterate over ONCE to generate values.
- ```yield```: used like ```return``` in a generator and saves its state, so execution will continue at that point the next time it is called.

To use ```yield```, you must understand that when the function is called, the code in the function body does not run. The function only returns the generator object.

Then, your code will be run each time the ```for``` uses the generator.

**Now the hard part**:

The first time the ```for``` calls the generator object, it will run the code in your function from the beginning until it hits ```yield```, then return the first value of the loop. Each subsequent call will run the loop you have written in the function one more time, and return the next value, until there are no values to return.

The generator is considered empty once the function runs, but does not reach ```yield``` anymore. This is because the loop has come to an end, or because a conditional is not satisfied anymore.
