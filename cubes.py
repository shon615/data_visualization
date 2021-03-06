import matplotlib.pyplot as plt

x_values = list(range(0,5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
	edgecolor='none', s=10)

# Set chart title and label axes.
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize = 14)

# Set chart tile and label axes
#plt.axis([0, 1100, 0, 1100000])

plt.savefig('cubes_plot.png', bbox_inches="tight")

plt.show()
