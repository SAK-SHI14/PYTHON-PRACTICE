import seaborn as sns
import matplotlib.pyplot as plt

# Load the flights dataset
flights = sns.load_dataset("flights")

# Print the first few rows of the dataset
print(flights.head())

# Explore the dataset
print(flights.info())
print(flights.describe())

# Plot the monthly passenger totals
plt.figure(figsize=(10, 6))
sns.lineplot(x="month", y="passengers", data=flights)
plt.title("Monthly Passenger Totals")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.show()