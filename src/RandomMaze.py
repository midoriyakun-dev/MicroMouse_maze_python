import random
import sys  

def main():
    # Take a comand line argument for the maze size
    # If no argument is provided, default to 10
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    #If the argument is not a valid integer, exit with an error message
    if size <= 0:
        print("Please provide a positive integer for the maze size.")
        sys.exit(1)
    #If the argument is larger than 100, exit with an error message
    if size > 100:
        print("Maze size too large. Please provide a size of 100 or less.")
        sys.exit(1)
    #if the argument is in between 1 and 100, generate a random maze of that size
    maze = generate_maze(size)
    #Print the generated maze
    print_maze(maze)   


def generate_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    for i in range(1, size - 1, 2):
        for j in range(1, size - 1, 2):
            maze[i][j] = ' '
            if i < size - 2 and random.choice([True, False]):
                maze[i + 1][j] = ' '
            if j < size - 2 and random.choice([True, False]):
                maze[i][j + 1] = ' '
    return maze  