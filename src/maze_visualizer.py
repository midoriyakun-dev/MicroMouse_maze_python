import matplotlib.pyplot as plt
import numpy as np

# Function to load mazes from saved_mazes.txt
def load_saved_mazes(filename="saved_mazes.txt"):
    with open(filename, "r") as f:
        raw = f.read().strip()
    maze_blocks = raw.split('\n\n')  # Each maze is separated by a blank line
    mazes = []
    for block in maze_blocks:
        rows = block.strip().split('\n')
        maze = [list(row) for row in rows]
        mazes.append(maze)
    return mazes

def visualize_maze(maze, depth_map=None):
    """
    maze: list of lists, each cell is '#', ' ', 'M', or 'E'
    depth_map: 2D numpy array or list of lists with same shape as maze, or None
    """
    mapping = {'#': 0, ' ': 1, 'M': 2, 'E': 3}
    grid = np.array([[mapping.get(cell, 1) for cell in row] for row in maze])

    # Set up color map: 0=black (wall), 1=white (path), 2=blue (start), 3=red (end)
    from matplotlib import colors
    cmap = colors.ListedColormap(['black', 'white', 'blue', 'red'])
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap=cmap, interpolation='none')
    plt.axis('off')

    # Overlay depth map if provided
    if depth_map is not None:
        depth_map = np.array(depth_map)
        # Use a transparent colormap for the depth overlay
        plt.imshow(depth_map, cmap='viridis', alpha=0.5, interpolation='none')
        plt.colorbar(label='Depth/Distance')

    plt.show()

# Example usage:
# maze = [
#     ['#', '#', '#', '#'],
#     ['#', 'M', ' ', '#'],
#     ['#', ' ', 'E', '#'],
#     ['#', '#', '#', '#']
# ]
# depth_map = [
#     [0, 0, 0, 0],
#     [0, 1, 2, 0],
#     [0, 2, 3, 0],
#     [0, 0, 0, 0]
# ]
# visualize_maze(maze, depth_map)

# Function to let user pick a maze to play
def pick_maze(mazes):
    print("Saved Mazes:")
    for idx, maze in enumerate(mazes):
        print(f"Maze #{idx+1}:")
        for row in maze:
            print(''.join(row))
        print()
    while True:
        try:
            choice = int(input(f"Enter the maze number to play (1-{len(mazes)}): "))
            if 1 <= choice <= len(mazes):
                return mazes[choice-1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid integer.")



# Visualize the maze with optional depth map overlay

