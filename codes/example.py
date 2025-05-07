import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary of Individuals')
plt.show()