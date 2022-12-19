import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the grid with a random initial state
grid = np.random.randint(2, size=(100, 100))

def update_grid(grid):
    # Create a copy of the grid to store the updated state
    new_grid = grid.copy()

    # Iterate over each cell in the grid
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count the number of live neighbors
            neighbors = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if (ii >= 0 and ii < grid.shape[0] and
                        jj >= 0 and jj < grid.shape[1] and
                        (ii, jj) != (i, j)):
                        neighbors += grid[ii, jj]

            # Apply the rules of the game to update the cell
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1

    return new_grid

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='summer', vmin=0, vmax=1, interpolation='nearest')

# Define the animation function
def animate(i):
    global grid
    grid = update_grid(grid)
    im.set_data(grid)
    return im,

# Create the animation using the FuncAnimation function
anim = FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
