
 This is a program that finds the shortest path a knight can take between two points on a standard 8x8 chessboard. In chess, knights move in an L-shape: 2 squares along one dimension, 1 square along the other.
 
 ![knight-moves](https://user-images.githubusercontent.com/27274397/211841486-af58f1e4-e8a0-4f8a-bc1c-bf2386d022b7.png)

Functional Requirements:

To write a command-line executable that reads instructions from standard input (stdin).
Instructions are lines (separated by newlines) in the following format:

D4 G7
D4 D5

The first of the space-separated values is the knight's starting position, the second is the knight's target position.
For each line in the input, the program will print (to standard out) the shortest path it found. So for the example above, it should print e.g.:

D4 F5 G7
D4 F5 E7 D5

