from collections import deque
from typing import List, Tuple

def convert_coordinates_toalpha(N: int) -> str:
    alpha_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
    return alpha_dict.get(N, "Invalid input")

def convert_coordinates_tonumber(c: str) -> int:
    number_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    return number_dict.get(c.upper(), "Invalid input")

def isvalid_move(pos: Tuple[int, int]) -> bool:
    """
    Check if the move is valid or not
    """
    return 1 <= pos[0] < 9 and 1 <= pos[1] < 9

def generate_moves(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Generate all possible moves
    """
    x, y = pos
    moves = [(x + i, y + j) for i, j in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]]
    return [move for move in moves if isvalid_move(move)]

def shortest_knight_path(start: Tuple[int, int], end: Tuple[int, int]) -> None:
    path_exist = False
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        pos, path = queue.popleft()

        if pos == end:
            path_exist = True
            for i in path:
                print(convert_coordinates_toalpha(i[0])+str(i[1]),end=" ")
            break
        

        for move in generate_moves(pos):
            if move not in visited:
                visited.add(move)
                new_path = path + [move]
                queue.append((move, new_path))
    if not path_exist:
        print("No path exist between given points")

starting,ending=map(str,(input("Enter starting and ending coordinates (x1y1) (x2y2)  of the knight:")).split(" "))
start_c = [x for x in s]
end_c=[x for x in e]
start_x=convert_coordinates_tonumber(start_c[0])
start_y=int(start_c[1])
end_x=convert_coordinates_tonumber(end_c[0])
end_y=int(end_c[1])
start = (start_x, start_y)
end = (end_x, end_y)
shortest_knight_path(start, end)
