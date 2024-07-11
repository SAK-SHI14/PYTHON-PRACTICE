#BAR PLOT
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

flights = sns.load_dataset("flights")

plt.figure(figsize=(10,6))
sns.barplot(x="month", y="passengers", data=flights)
plt.title("Monthly Passengers")
plt.show()