# Crossword Composer

This project contains implementation of Crossword Composer problem in Python.
For a given grid and specific dictionary which contains list of words in English, the software trys to fill all the
white cells in the grid with letters where each columns or row are formed by a word in the dictionary.

## Project Main Structure:

1. algorithms folder:
    - contains two main files, a_star.py and csp.py.
    - a_star.py is the a* algorithm implementation.
    - csp.py contains a wrapper class that use a library: python-constraint.
2. helpers:
    - dictionary: contains implementation of all helper methods and indexing needed by the algorithms
    - gridBuilder: contains methods of building grids arrays, wordslist and convertions between them.
3. models:
    - word: the basic object of a word of the grid.
    - node: represnet the node or state in A* algorithm
    - position: represent the x,y coordinates in the grid.
    - direction: has two values: Across/Down.
4. resources:
    - words(2)(small).txt:  are the dictionaries.

and finally one main file, main.py.

## Custom A* Solvers

1. Start Solver: determine the way of how the first word in the grid will be selected.
    - Least-Possibilities:  The word in the grid that have the least number of words in the dictionary.
    - Most-Intersects: The word in the grid that have most intersects with other words.
2. Process Solver: determine the way of how the algorithm will select the next word in the grid from a current state.
    - Active-Word: Continue from the active word in the grid which has been filled previously and check it’s crosswords.
    - Another-Word: Continue from another word in the grid which is not related to previous filled word.

## Dictionary Indexing

- Indexed by word-length
- Indexed by first-character
- And in addition to previous indexing operations, we indexed our dictionary in the following way:
  List of <Key-Value> pairs, where the key correspond to the following string format: “Index_letter_length” for example:
  “4_R_7”: correspond to all words the have at the forth index the letter “R” and it’s length equal to 7.
- The last index approach is very powerful for this kind of problems.
