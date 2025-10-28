from Stack import Stack

def solveMaze(maze, startX, startY):
    # Initialize Stack
    s = Stack()

    # Push first step, mark first step
    s.push([startX, startY])
    step_count = 1
    maze[startX][startY] = step_count

    while not s.isEmpty(): # loop that runs while stack is not empty
        position = s.peek() # take coordinates of most recent step
        x = position[0]
        y = position[1]

        moved = False # used to determine if we should start popping stacks

        # Move North
        if maze[x - 1][y] == ' ':
            step_count += 1
            x -= 1
            maze[x][y] = step_count
            s.push([x, y])
            moved = True
            continue
        
        # Move West
        if maze[x][y - 1] == ' ':
            step_count += 1
            y -= 1
            maze[x][y] = step_count
            s.push([x, y])
            moved = True
            continue
        
        # Move South
        if maze[x + 1][y] == ' ':
            step_count += 1
            x += 1
            maze[x][y] = step_count
            s.push([x, y])
            moved = True
            continue
        
        # Move East
        if maze[x][y + 1] == ' ':
            step_count += 1
            y += 1
            maze[x][y] = step_count
            s.push([x, y])
            moved = True
            continue
        
        if maze[x - 1][y] == 'G' or maze[x][y - 1] == 'G' or maze[x + 1][y] == 'G' or maze[x][y + 1] == 'G': # Check for goal
            return True

        # pop if there's no steps that can be taken at that position
        if not moved:
            s.pop()
        
    return False # Executes if no solution is found