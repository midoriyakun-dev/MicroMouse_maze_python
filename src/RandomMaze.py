import random
import sys  

def RandomMaze():
    # Take a command line argument for the maze size
    # If no argument is provided, default to 10
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    #If the argument is not a valid integer, exit with an error message
    if size <= 0:                                                                   #Should I make this <=5? whats a maze size of 1,2,3,4? Not fun to play with
        print("Please provide a positive integer for the maze size.")
        sys.exit(1)
    #If the argument is larger than 100, exit with an error message
    if size > 100:
        print("Maze size too large. Please provide a size of 100 or less.")
        sys.exit(1)
    #if the argument is in between 1 and 100, generate a random maze of that size
    maze = generate_maze(size)
    # Set static start point           //The micromouse will start at (1, 1) so "S" changed to "M"
    start = (1, 1)
    maze[start[0]][start[1]] = 'M'

    # Find all possible end points not near the corners (at least 2 cells away from edges)
    possible_ends = []
    for i in range(2, size-2):
        for j in range(2, size-2):
            if maze[i][j] == ' ':
                possible_ends.append((i, j))
    if possible_ends:
        end = random.choice(possible_ends)                      #Check how random class works or we need to create our own random function
        maze[end[0]][end[1]] = 'E'                              #Make it more random HEHEHE
        

    else:
        print("No valid end point found away from corners.")
    
    print(f"Start: {start}")       # No need to print start point, but keeping it for reference 


    # Print the generated maze
    print_maze(maze)

    # Ask user if they want to save the maze
    save = input("Save this maze to file? Do yo like it for further use? (y/n): ").strip().lower()
    if save == 'y':
        with open("saved_mazes.txt", "a") as f:
            for row in maze:
                f.write(''.join(row) + '\n')
            f.write('\n')  # Separate mazes with a blank line
        print("Maze saved to saved_mazes.txt.")


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

def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print() 

if __name__ == "__main__":
    RandomMaze()

#Can I take this output and use it to represent the maze in a GUI or a wall display? Can i make it 3D rendered?? wall height color and rendering options?
#What python package to use for 2d or 3d rendering?