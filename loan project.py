import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r"C:\Users\SJ\Desktop\Loan 2.csv")
# or
# df = pd.read_csv("C:/Users/SJ/Desktop/Loan 2.csv")

# Print the column names
print(df.columns)

# Fill null values in the 'Gender' column with the most frequent value
most_frequent_gender = df['Gender'].mode()[0]
df['Gender'].fillna(most_frequent_gender, inplace=True)

# Fill null values in the 'Income (USD)' column with the median value
df['Income (USD)'].fillna(df['Income (USD)'].median(), inplace=True)

# Fill null values in the 'Age' column with the mean value
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill null values in the 'Income Stability' column with the most frequent value
most_frequent_income_stability = df['Income Stability'].mode()[0]
df['Income Stability'].fillna(most_frequent_income_stability, inplace=True)

# Fill null values in the 'Profession' column with the most frequent value
most_frequent_profession = df['Profession'].mode()[0]
df['Profession'].fillna(most_frequent_profession, inplace=True)

# Fill null values in the 'Type of Employment' column with the most frequent value
most_frequent_type_of_employment = df['Type of Employment'].mode()[0]
df['Type of Employment'].fillna(most_frequent_type_of_employment, inplace=True)

# Fill null values in the 'Location' column with the most frequent value
most_frequent_location = df['Location'].mode()[0]
df['Location'].fillna(most_frequent_location, inplace=True)

# Fill null values in the 'Loan Amount Request (USD)' column with the median value
df['Loan Amount Request (USD)'].fillna(df['Loan Amount Request (USD)'].median(), inplace=True)

# Fill null values in the 'Current Loan Expenses (USD)' column with the median value
df['Current Loan Expenses (USD)'].fillna(df['Current Loan Expenses (USD)'].median(), inplace=True)

# Fill null values in the 'Expense Type 1' column with the most frequent value
most_frequent_expense_type_1 = df['Expense Type 1'].mode()[0]
df['Expense Type 1'].fillna(most_frequent_expense_type_1, inplace=True)

# Fill null values in the 'Expense Type 2' column with the most frequent value
most_frequent_expense_type_2 = df['Expense Type 2'].mode()[0]
df['Expense Type 2'].fillna(most_frequent_expense_type_2, inplace=True)

# Fill null values in the 'Dependents' column with the median value
df['Dependents'].fillna(df['Dependents'].median(), inplace=True)

# Fill null values in the 'Credit Score' column with the mean value
df['Credit Score'].fillna(df['Credit Score'].mean(), inplace=True)

# Fill null values in the 'No. of Defaults' column with the median value
df['No. of Defaults'].fillna(df['No. of Defaults'].median(), inplace=True)

# Fill null values in the 'Has Active Credit Card' column with the most frequent value
most_frequent_has_active_credit_card = df['Has Active Credit Card'].mode()[0]
df['Has Active Credit Card'].fillna(most_frequent_has_active_credit_card, inplace=True)

# Fill null values in the 'Property ID' column with the most frequent value
most_frequent_property_id = df['Property ID'].mode()[0]
df['Property ID'].fillna(most_frequent_property_id, inplace=True)

# Fill null values in the 'Property Age' column with the median value
df['Property Age'].fillna(df['Property Age'].median(), inplace=True)

# Fill null values in the 'Property Type' column with the most frequent value
most_frequent_property_type = df['Property Type'].mode()[0]
df['Property Type'].fillna(most_frequent_property_type, inplace=True)

# Fill null values in the 'Property Location' column with the most frequent value
most_frequent_property_location = df['Property Location'].mode()[0]
df['Property Location'].fillna(most_frequent_property_location, inplace=True)

# Fill null values in the 'Co-Applicant' column with the most frequent value
most_frequent_co_applicant = df['Co-Applicant'].mode()[0]
df['Co-Applicant'].fillna(most_frequent_co_applicant, inplace=True)

# Fill null values in the 'Property Price' column with the median value
df['Property Price'].fillna(df['Property Price'].median(), inplace=True)

# Fill null values in the 'Loan Sanction Amount (USD)' column with the median value
df['Loan Sanction Amount (USD)'].fillna(df['Loan Sanction Amount (USD)'].median(), inplace=True)