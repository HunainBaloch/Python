import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, np.nan, 40],
    'Salary': [70000, 80000, 90000, np.nan]
}
df = pd.DataFrame(data)
print("DataFrame with missing values:\n", df)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
print("DataFrame after filling missing values:\n", df)

# Group by and aggregation
grouped_df = df.groupby('Age').agg({'Salary': 'mean'})
print("Grouped and aggregated DataFrame:\n", grouped_df)
