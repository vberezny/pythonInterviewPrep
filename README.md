# Python Interview Prep

This is a repo for me to practice data structures and algorithms in Python to pass a technical interview

## General Notes on python

- Iterables: anything you can use "for .. in .. " on (lists,strings,files)
- Generators: an iterable you can iterate over ONCE, generate values on the fly
- yield: keyword that is used like RETURN, except the function will return a generator. To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

Then, your code will be run each time the for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.
