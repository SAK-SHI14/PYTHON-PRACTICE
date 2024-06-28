import matplotlib.pyplot as plt

# GRADES DISTRIBUTION OF STUDENTS
grades=["A","B","C","D","F"]  
distribution=[20,30,25,10,15]  

plt.pie(distribution,labels=grades,autopct="%1.2f%%")
plt.title("Grades Distribution of Students")
plt.show() 

#USING ADDITIONAL FEATURES : COLORS,EXPLODE,SHADOW,STARTANGLE
labels=['Facebook', 'Instagram', 'Twitter', 'LinkedIn']
sizes=[30, 20, 15, 35]
colors=['blue', 'purple', 'lightblue', 'gray']
explode=[0, 0, 0, 0.1]  
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title("Social Media Usage")
plt.show()

#LINE CHART 
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]  # days of the week
temperature = [25, 27, 28, 30, 29, 28, 27]  # temperature in Celsius

plt.plot(days, temperature, color="blue")
plt.title("Temperature Over the Week")  
plt.xlabel("Days of the Week")  
plt.ylabel("Temperature (°C)")  
plt.show()

#Passing the x array and function values for the y axis
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**2

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values
y = f(x)

# Create the plot
plt.plot(x, y)

# Add title and labels
plt.title('Plot of y = x^2')
plt.xlabel('x')
plt.ylabel('y')

# Display the plot
plt.show()

#MULTIPLE LINE PLOT 
import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values
x = np.linspace(0, 10, 100)

# Create three arrays of y values
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the three lines
ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')
ax.plot(x, y3, label='sin(x) + cos(x)')

# Add a legend
ax.legend()

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Create arrays of x and y values
x = np.linspace(0, 10, 100)
y = np.sin(x)

x1 = np.linspace(0, 10, 100)
y1 = np.cos(x1)

x2 = np.linspace(0, 10, 100)
y2 = np.sin(x2) + np.cos(x2)

x3 = np.linspace(0, 10, 100)
y3 = np.sin(x3) * np.cos(x3)

# Create subplots
plt.subplot(2, 2, 1)
plt.plot(x, y, 'y')
plt.title('Sine Wave')

plt.subplot(2, 2, 2)
plt.plot(x1, y1, color="red", marker="o")
plt.title('Cosine Wave')

plt.subplot(2, 2, 3)
plt.plot(x2, y2, 'g')
plt.title('Sine + Cosine Wave')

plt.subplot(2, 2, 4)
plt.plot(x3, y3, 'b', linestyle='--', marker='s')
plt.title('Sine * Cosine Wave')

# Show the plot
plt.tight_layout()
plt.show()

#BAR CHART
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')
plt.show()

#LINE CHART + BAR CHART
import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values1 = [10, 20, 30, 40]
values2 = [40, 30, 20, 10]

x = np.arange(len(categories))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.bar(x, values1, color='b')
ax2.plot(x, values2, marker='o', color='r')

ax1.set_ylabel('Bar Values', color='b')
ax2.set_ylabel('Line Values', color='r')
ax1.set_title('Combination of Line Chart and Bar Chart')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

plt.show()

import matplotlib.pyplot as plt

# Data for the chart
years_x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Sales of Apple products
apple_y = [350, 380, 420, 450, 480, 510, 550, 580, 610, 640, 670]

plt.bar(years_x, apple_y, color='r', label='Apple Products')

# Sales of Samsung products
samsung_y = [300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]

plt.plot(years_x, samsung_y, color='g', linewidth=3, marker='o', label='Samsung Products')

# Sales of Huawei products
huawei_y = [250, 280, 310, 340, 370, 400, 430, 460, 490, 520, 550]

plt.plot(years_x, huawei_y, color='b', linewidth=3, marker='X', label='Huawei Products')

plt.title('Sales of Mobile Phones by Year')
plt.xlabel('Years')
plt.ylabel('Sales (Millions)')

plt.legend()

plt.grid(True)

plt.show()

import matplotlib.pyplot as plt

# Data for the chart
years_x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

# Sales of Toyota cars
toyota_y = [20000, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000, 38000, 40000]

plt.bar(years_x, toyota_y, color='r', label='Toyota')

# Sales of Honda cars
honda_y = [18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000, 38000]

plt.bar(years_x, honda_y, color='g', label='Honda')

# Sales of Ford cars
ford_y = [15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000]

plt.bar(years_x, ford_y, color='b', label='Ford')

plt.title('Car Sales by Year')
plt.xlabel('Years')
plt.ylabel('Sales')

plt.legend()

plt.grid(True)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

cities_x = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# create a range
x_indexes = np.arange(len(cities_x))  # numpy array with range from (0,m)
width = 0.25

# Average House Prices by City
ny_y = [540000, 690000, 270000, 190000, 240000, 280000, 220000, 640000, 290000, 1100000]

plt.bar(x_indexes - width,
        ny_y,
        color='r',
        width=width,
        label='New York')

# Average House Prices by City
la_y = [490000, 620000, 230000, 170000, 210000, 240000, 200000, 580000, 250000, 1000000]

plt.bar(x_indexes,
        la_y,
        color='g',
        width=width,
        label='Los Angeles')

ch_y = [440000, 590000, 200000, 150000, 190000, 210000, 180000, 520000, 220000, 900000]

plt.bar(x_indexes + width,
        ch_y,
        color='b',
        width=width,
        label='Chicago')

# Setting chart title and labels
plt.title('Average House Prices (USD) by City')
plt.xlabel('City')
plt.ylabel('Average House Price (USD)')

# Set the x-axis ticks to the cities
plt.xticks(ticks=x_indexes, labels=cities_x)

# Adding legend
plt.legend()

# Show plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create the scatter plot
plt.scatter(x, y, color='blue', label='Data Points')

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add legend
plt.legend()

# Show the plot
plt.show()

#customized scatter plot
import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create the scatter plot
plt.scatter(x, y, marker='s', s=100, c='green', alpha=0.5, label='Data Points')

# Add title and labels
plt.title('Customized Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add legend
plt.legend()

# Show the plot
plt.show()

#histogram
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(1000)

# Create the histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add title and labels
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(1000)

# Create the histogram
plt.hist(data, bins=50, range=(-3,3), density=True, histtype='step', orientation='horizontal', color='red', edgecolor='black', alpha=0.7)

# Add title and labels
plt.title('Customized Histogram Example')
plt.xlabel('Frequency')
plt.ylabel('Value')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.arange(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)

# Create the area plot
plt.plot(x, y1, label='Series 1')
plt.fill_between(x, y1, alpha=0.3)

plt.plot(x, y2, label='Series 2')
plt.fill_between(x, y2, alpha=0.3)

plt.plot(x, y3, label='Series 3')
plt.fill_between(x, y3, alpha=0.3)

# Add title and labels
plt.title('Area Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add legend
plt.legend()

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.arange(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)

# Create the area plot
plt.plot(x, y1, label='Series 1')
plt.fill_between(x, y1, alpha=0.5, color='blue', label='Series 1')

plt.plot(x, y2, label='Series 2')
plt.fill_between(x, y2, alpha=0.5, color='green', label='Series 2')

plt.plot(x, y3, label='Series 3')
plt.fill_between(x, y3, alpha=0.5, color='red', label='Series 3')

# Add title and labels
plt.title('Customized Area Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add legend
plt.legend()

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]

# Create the box plot
plt.boxplot(data)

# Add title and labels
plt.title('Box Plot Example')
plt.xlabel('Groups')
plt.ylabel('Values')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]

# Create the box plot
fig, ax = plt.subplots()
ax.boxplot(data, vert=False, patch_artist=True, showfliers=False)

# Format the box plot
ax.set_title('Formatted Box Plot Example')
ax.set_xlabel('Values')
ax.set_ylabel('Groups')

# Customize the box plot
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
ax.set_yticks([])

# Change the box plot colors
boxes = ax.artists[0]['boxes']
for box in boxes:
    box.set_facecolor('lightblue')

# Change the whisker colors
whiskers = ax.artists[0]['whiskers']
for whisker in whiskers:
    whisker.set_color('black')

# Change the median colors
medians = ax.artists[0]['medians']
for median in medians:
    median.set_color('red')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data1 = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]
data2 = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]
data3 = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]

# Create the box plot
fig, ax = plt.subplots()
ax.boxplot([data1, data2, data3], vert=False, patch_artist=True, showfliers=False)

# Format the box plot
ax.set_title('Multi-Dataset Box Plot Example')
ax.set_xlabel('Values')
ax.set_ylabel('Groups')

# Customize the box plot
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
ax.set_yticks([])

# Change the box plot colors
boxes = ax.artists[0]['boxes']
for i, box in enumerate(boxes):
    box.set_facecolor(['lightblue', 'lightgreen', 'lightyellow'][i])

# Change the whisker colors
whiskers = ax.artists[0]['whiskers']
for i, whisker in enumerate(whiskers):
    whisker.set_color(['black', 'black', 'black'][i])

# Change the median colors
medians = ax.artists[0]['medians']
for i, median in enumerate(medians):
    median.set_color(['red', 'green', 'blue'][i])

# Add a legend
legend_labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']
legend_handles = [plt.Line2D([0], [0], marker='s', color='w', label=label, markerfacecolor=color, markersize=12) for label, color in zip(legend_labels, ['lightblue', 'lightgreen', 'lightyellow'])]
plt.legend(handles=legend_handles, loc='upper right')

# Show the plot
plt.show()