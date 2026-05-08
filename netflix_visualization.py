import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv("cleaned_netflix_dataset.csv")

# Create figure
plt.figure(figsize=(12,6))

# Create line chart with markers
plt.plot(
    df["Title"],
    df["Rating"],
    marker="o",
    linestyle="--",
    color="red",
    linewidth=3,
    markersize=8
)

# Graph title and labels
plt.title("Netflix Ratings Analysis", fontsize=16)
plt.xlabel("Shows / Movies", fontsize=12)
plt.ylabel("Ratings", fontsize=12)

# Rotate names
plt.xticks(rotation=45)

# Add grid
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Save graph
plt.savefig("netflix_graph.png")

# Show graph
plt.show()