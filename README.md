from collections import deque
flag=0
def convert_coordinates_toalpha(N):
    if(N==1):
        return "A"
    elif(N==2):
        return "B"
    elif(N==3):
        return "C"
    elif(N==4):
        return "D"
    elif(N==5):
        return "E"
    elif(N==6):
        return "F"
    elif(N==7):
        return "G"
    else:
        return "H"
        
def convert_coordinates_tonumber(c):
    if(c=="A" or c=="a"):
        return 1
    elif(c=="B" or c=="b"):
        return 2
    elif(c=="C" or c=="c"):
        return 2
    elif(c=="D" or c=="d"):
        return 4
    elif(c=="E" or c=="e"):
        return 5
    elif(c=="F" or c=="f"):
        return 6
    elif(c=="G" or c=="g"):
        return 7
    else:
        return 8
    
def shortest_knight_path(start, end):
    # Function to check whether the move is valid or not
    def isvalid(pos):
        return 1 <= pos[0] < 9 and 1 <= pos[1] < 9

    # Function to create all possible moves
    def moves_generator(pos):
        x, y = pos
        moves = [(x + i, y + j) for i, j in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]]
        return [move for move in moves if isvalid(move)]

    
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            flag=1
            for i in path:
                print(convert_coordinates_toalpha(i[0])+str(i[1]),end=" ")
            
        for move in moves_generator(pos):
            if move not in visited:
                visited.add(move)
                new_path = path + [move]
                queue.append((move, new_path))
    if(flag==0):
        print("No path exist between given points")

s=input("Enter starting coordinates (xy) of the knight: ")
e=input("Enter ending coordinates (xy) of the knight: ")
start_c = [x for x in s]
end_c=[x for x in e]
start_x=convert_coordinates_tonumber(start_c[0])
start_y=int(start_c[1])
end_x=convert_coordinates_tonumber(end_c[0])
end_y=int(end_c[1])
start = (start_x, start_y)
end = (end_x, end_y)
shortest_knight_path(start, end)
