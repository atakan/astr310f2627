import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn visual style
sns.set_theme(style="whitegrid")

# Load arrays from the file
with open("random_data.npy", "rb") as f:
    x = np.load(f)
    y = np.load(f)

# Plot using Seaborn lineplot with blue lines and red circle markers
ax = sns.lineplot(
    x=x,
    y=y,
    color="blue",
    marker="o",
    markerfacecolor="red",
    markeredgecolor="red",
    label="random points",
)

# Set plot title
plt.title("An example plot")

# Optional: Command to save the plot as a PDF
# plt.savefig("example_plot.pdf", format="pdf", bbox_inches="tight")

# Display the plot
plt.show()
