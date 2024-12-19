import pandas as pd

#cpm_d.csv data will carry the FC values in the columns. FC needs to be calculated before
#using it for this script using Excel 

# Load the CSV file into a DataFrame
df = pd.read_csv('cpm_d.csv')

# Create a new DataFrame to store the modified values
modified_df = pd.DataFrame()
modified_df['Category'] = df.iloc[:, 0]  # Copy the first column (assumed to be categorical)

# Function to modify the values as per the given rules
def modify_values(value):
    try:
        # Attempt to convert the value to a float
        value = float(value)
        if value == 0:
            return 0  # Handle zero values
        if value < 1:
            value = -1 / value
        if value > 0:
            return value - 1
        else:
            return value + 1
    except ValueError:
        # If conversion fails, return the original value or handle as needed
        return value

# Apply the modification to each column except the first one
for column in df.columns[1:]:
    modified_df[column] = df[column].apply(modify_values)

# Save the modified DataFrame to a new CSV file
modified_df.to_csv('modified_data.csv', index=False)

print(modified_df)

