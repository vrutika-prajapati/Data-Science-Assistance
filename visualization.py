import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 12, 34, 56]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the style of the visualization
sns.set(style="whitegrid")

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Values', data=df, palette='viridis')

# Add titles and labels
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Values')

# Show the plot
plt.show()