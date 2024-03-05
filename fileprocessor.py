import pandas as pd

# Read DATA.dat file 
df1 = pd.read_csv("DATA.dat",delimiter='\t')

# Read data from DATA1.dat file
df2 = pd.read_csv("DATA1.dat",delimiter='\t')

# Making a new dataframe to combine data of two csv files
newdf = df1._append(df2)


# Dropping duplicates from dataframe
result = newdf.drop_duplicates()


# Adding Gross Salary  column to result CSV file which is sum of basic_salary and allowances
result["Gross Salary"] = result["basic_salary"]+result["allowances"]

# Writing the data from both files to CSV file
result.to_csv("Result.csv",index=False)

# Calculating mean or Average of basic salary

average_gross_salary=result["Gross Salary"].mean()


#Dropping duplicates to calculate 2nd highest salary
 
unique_gross_salaries = result['Gross Salary'].drop_duplicates()

# Selecting 2nd Highest Gross salary value
second_highest_salary = result['Gross Salary'].sort_values(ascending=False).iloc[1]



with open("Result.csv","a") as f:
    f.write(f"Second Highest Salary={second_highest_salary},average salary={average_gross_salary},,,,,,")

print("Result.csv file generated Successfully.")


