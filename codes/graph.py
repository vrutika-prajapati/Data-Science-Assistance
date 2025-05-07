import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Date': pd.date_range(start='1/1/2023', periods=10, freq='D'),
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o')
plt.title('Line Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()