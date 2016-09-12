# A partial string equality analyzer

### What this shit is?

It is a little algorythm, that compares two strings, and calculates their `equality percent`. What is `equality percent`? It is a measure that indicates, how two string are similar. 

### How to use this?

It's written in python, and it is easy. In it's current state, it's just a function that takes two strings and returns floating point number that indicates `equality percent`.

Maybe, I'll work it out and make more usable at unix-like system. 

### Requirements

The lowest version of Python I tested it on was 2.7.

### How to determine, how similar strings are, using this algorythm?

It's easy:
- The equal strings will return `0`
- Strings that have nothing in common will return `1` if first string's size is smaller than second
- If first string's size is bigger than second ones', the negative number is returned

