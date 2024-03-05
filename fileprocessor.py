import pandas as pd
# Read DATA.dat file 

df1 = pd.read_csv("DATA.dat",delimiter='\t')

# Read data from DATA1.dat file
df2 = pd.read_csv("DATA1.dat",delimiter='\t')

# Making a new dataframe to combine data of two csv files
newdf = df1._append(df2)

# print("Length of unique newdf",len(newdf))

# Dropping duplicates from dataframe
result = newdf.drop_duplicates()
print("Length of Unique data", len(result))


# Adding Gross Salary  column to result CSV file which is sum of basic_salary and allowances
result["Gross Salary"] = result["basic_salary"]+result["allowances"]

# Writing the data from both files to CSV file
result.to_csv("Result.csv",index=False)

# Calculating mean or Average of basic salary
# We can use mean function for average gross salary but mean function takes all rows of csv including column 
# names which slightly gives wrong result result  Hence I have used a sum function to calculate the result
#  and divide it by number of rows in dataframe
average_gross_salary=result["Gross Salary"].mean()
# Sum = result["Gross Salary"].sum()
# print("Rows are ",result.shape[0])
# average_gross_salary =  round(Sum/(result.shape[0]-1),5)
# print(average_gross_salary)

print("Length of Salaries",len(result["Gross Salary"]))

#Dropping duplicates to calculate 2nd highest salary
 
unique_gross_salaries = result['Gross Salary'].drop_duplicates()

# Selecting 2nd Highest Gross salary value
second_highest_salary = result['Gross Salary'].sort_values(ascending=False).iloc[1]

print("second_highest_salary",second_highest_salary,type(second_highest_salary))


with open("Result.csv","a") as f:
    f.write(f"Second Highest Salary={second_highest_salary},average salary={average_gross_salary},,,,,,")


