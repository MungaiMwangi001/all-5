import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Import the 3D plotting toolkit

# Sample data (x, y, z coordinates)
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [2, 3, 4, 5, 6]

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the 3D scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set labels for the axes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
