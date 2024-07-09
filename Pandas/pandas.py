import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Add a new column
df['Salary'] = [70000, 80000, 90000]
print("DataFrame with Salary column:\n", df)

# Filter rows
filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30):\n", filtered_df)

# Calculate statistics
print("Mean age:", df['Age'].mean())
