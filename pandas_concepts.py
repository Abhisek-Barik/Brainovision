# === 1. Import pandas and numpy ===
import pandas as pd
import numpy as np

# === 2. Create a DataFrame ===
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'Salary': [50000, 60000, 70000, 80000, 65000],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# === 3. Basic DataFrame Operations ===
print("\nShape of DataFrame:", df.shape)  # (rows, columns)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 3 rows:\n", df.head(3))
print("\nDescribe numeric columns:\n", df.describe())

# === 4. Selection and Filtering ===
print("\nSelect 'Name' column:\n", df['Name'])
print("\nRows where Age > 30:\n", df[df['Age'] > 30])
print("\nSelect Name and Age where Department is 'IT':\n", df[df['Department'] == 'IT'][['Name', 'Age']])

# === 5. Adding and Modifying Columns ===
df['Tax'] = df['Salary'] * 0.1  # Add a new column
df['Net Salary'] = df['Salary'] - df['Tax']
print("\nDataFrame with Tax and Net Salary:\n", df)

# === 6. Sorting Data ===
print("\nSort by Age:\n", df.sort_values(by='Age'))
print("\nSort by Salary descending:\n", df.sort_values(by='Salary', ascending=False))

# === 7. Grouping and Aggregation ===
print("\nAverage salary by department:\n", df.groupby('Department')['Salary'].mean())

# === 8. Handling Missing Data ===
df.loc[2, 'Salary'] = np.nan  # Introduce a missing value
print("\nWith missing value:\n", df)
print("\nDrop rows with any NaN:\n", df.dropna())
print("\nFill NaN with mean salary:\n", df.fillna(df['Salary'].mean()))

# === 9. Merging DataFrames ===
dept_info = pd.DataFrame({
    'Department': ['HR', 'Finance', 'IT'],
    'Manager': ['Lisa', 'Mark', 'John']
})
merged_df = pd.merge(df, dept_info, on='Department', how='left')
print("\nMerged with department info:\n", merged_df)

# === 10. Pivot Table ===
pivot = pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
print("\nPivot table of average salary per department:\n", pivot)

# === 11. Exporting and Importing Data ===
df.to_csv('employees.csv', index=False)
loaded_df = pd.read_csv('employees.csv')
print("\nLoaded from CSV:\n", loaded_df)

# === 12. Apply Custom Function ===
df['Salary Category'] = df['Salary'].apply(lambda x: 'High' if x >= 70000 else 'Low')
print("\nWith Salary Category:\n", df)

# === 13. Reset and Set Index ===
df_indexed = df.set_index('Name')
print("\nDataFrame with Name as index:\n", df_indexed)
print("\nReset index:\n", df_indexed.reset_index())

# === 14. Value Counts and Unique ===
print("\nUnique Departments:", df['Department'].unique())
print("\nDepartment Counts:\n", df['Department'].value_counts())

# === 15. DataFrame from CSV URL ===
# Sample: Load a dataset from URL (optional, needs internet)
# url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
# df_remote = pd.read_csv(url)
# print("\nRemote DataFrame:\n", df_remote.head())