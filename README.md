Problem:
 
To find the shortest path a knight can take between two points on a standard 8x8 chessboard. In chess, knights move in an L-shape: 2 squares along one dimension, 1 square along the other.
 
 ![knight-moves](https://user-images.githubusercontent.com/27274397/211841486-af58f1e4-e8a0-4f8a-bc1c-bf2386d022b7.png)

Functional Requirements:

To write a command-line executable that reads instructions from standard input (stdin).
Instructions are lines (separated by newlines) in the following format:

D4 G7

D4 D5

The first of the space-separated values is the knight's starting position, the second is the knight's target position.
For each line in the input, the program will print (to standard out) the shortest path it found. So for the example above, it will print like:

D4 F5 G7

D4 F5 E7 D5

Solution:

This is implemented using BFS(Breadth First Search) algorithm to find the shortest path between two coordinates (starting position and target position) on a chess board using a Knight piece.
Here is a brief overview of the algorithm:

1) Initialize a queue with the starting point and its path, and a set to store visited coordinates.

2) Dequeue the first point from the queue, and check if it is the end point. If it is, print the path and break the loop.

3) If it's not the end point, generate all possible moves from the current point and add them to the queue.

4) Mark the current point as visited, and append it to the path.

5 )Repeat steps 2-4 until the end point is found or the queue is empty. If the queue is empty and the end point is not found, print "No path exist between given points".

6) Finally, it uses the helper functions convert_coordinates_toalpha(N) and convert_coordinates_tonumber(c) to convert between numerical and alphabetic representation of the chess board coordinates.

The algorithm uses a simple yet efficient approach to find the shortest path using a modified BFS. The use of a queue and a visited set ensures that the algorithm explores all possible paths in the least amount of steps, while also avoiding revisiting previously visited coordinates.
This algorithm is implemented using Python programming language.
