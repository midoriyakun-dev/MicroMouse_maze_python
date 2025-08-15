"""
import sys
sys.path.append('./src')
from RandomMaze import RandomMaze, generate_maze, print_maze       # otherwise move BOT to root directory and use this import
"""

from RandomMaze import RandomMaze, generate_maze, print_maze # As both files are in the same directory, this import should work without issues.
import random

def BOTinMaze():
    pass



def ReadMaze():
    with open("saved_mazes.txt", "r") as f:
        mazes = f.read().strip().split('\n\n')
        for maze in mazes:
            print("Maze:")
            print(maze)
            print()