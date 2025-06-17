import matplotlib.pyplot as plt
import numpy as np

# ========= 1. Line Chart =========
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.figure(figsize=(6, 4))
plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.tight_layout()
plt.show()

# ========= 2. Bar Chart =========
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 4]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='orange')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.tight_layout()
plt.show()

# ========= 3. Histogram =========
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
bins = [0, 20, 40, 60, 80, 100]

plt.figure(figsize=(6, 4))
plt.hist(data, bins=bins, color='green', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ========= 4. Scatter Plot =========
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 4, 3, 2, 1]

plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, color='red', marker='x')
plt.title("Scatter Plot")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.grid(True)
plt.tight_layout()
plt.show()

# ========= 5. Pie Chart =========
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [40, 25, 20, 15]

plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.tight_layout()
plt.show()

# ========= 6. Subplots (2x2 Grid) =========
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# Top Left - Line
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line")

# Top Right - Bar
axs[0, 1].bar(categories, values)
axs[0, 1].set_title("Bar")

# Bottom Left - Scatter
axs[1, 0].scatter(x_scatter, y_scatter)
axs[1, 0].set_title("Scatter")

# Bottom Right - Histogram
axs[1, 1].hist(data, bins=bins)
axs[1, 1].set_title("Histogram")

plt.suptitle("Multiple Subplots")
plt.tight_layout()
plt.show()

# ========= 7. 3D Surface Plot =========
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

x_3d = np.linspace(-5, 5, 100)
y_3d = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_3d, y_3d)
Z = np.sin(np.sqrt(X**2 + Y**2))  # 3D surface function

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot")
plt.tight_layout()
plt.show()