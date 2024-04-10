# Imagine you're a gardener tracking how many new plant sprouts you observe each day for a week. Here's a neat line plot that shows your observations. Can you discern how the number of sprouts has changed over the course of the week? Click Run to view the plot in action!

import matplotlib.pyplot as plt

# A beginner gardener's weekly record of new plant sprouts
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sprouts_count = [3, 4, 9, 13, 18, 22, 29]

# Plotting the number of new sprouts each day of the week
plt.plot(week_days, sprouts_count)
plt.title('Number of New Plant Sprouts Over a Week')
plt.xlabel('Day of the Week')
plt.ylabel('Sprouts Count')
plt.show()

# Now, let's further personalize your garden plant chart. Could you add a title "Weekly Plant Growth" and label the axes "Days" (x-axis) and "Height in Inches" (y-axis) to make your chart even clearer?

# Simulating weekly plant heights as they grow each day
days = range(1, 8)  # Days of the week
height_growth = [2, 2.5, 3, 3.5, 4, 4.5, 5]  # Corresponding heights for each day

plt.plot(days, height_growth)  # Plot a line graph
# Add a title and labels for both axes below:
plt.title('Weekly Plant Growth')
plt.xlabel('Days')
plt.ylabel('Height in Inches')

# Show the plot
plt.show()

# Now, let's plot a journey of a different kind. We've tracked rainfall in a garden over a week. Your task is to write code that plots these rain readings on a line graph.

# For x axis, use a range from 1 to 7 inclusive.

# May your plot be as clear as a crisp, starry night!

# Weekly rainfall amounts in inches
rainfall = [0.75, 0.5, 0.2, 0, 1.2, 0.8, 0.3]
# TODO: define X array
days = range(1, 8)  # Days of the week

# TODO: Use the plot function to create a line graph of the rainfall, with day numbers on the x-axis.
plt.title('Garden Rainfall Over a Week')
plt.xlabel('Day')
plt.ylabel('Rainfall (inches)')
plt.plot(days, rainfall)
plt.show()

# Let's solidify your skills by creating a complete plot from scratch. Your mission is to create a line plot that charts the water consumption of garden plants over a week, complete with labels and a title.

# Data for weekly water consumption (in gallons) of the garden plants
days = [1, 2, 3, 4, 5, 6, 7]
water_consumption = [5, 5.5, 6, 6.5, 6, 5.7, 5.5]

# TODO: Use the plot function to create a line plot of the water consumption
plt.plot(days, water_consumption)

# TODO: Add a title to the plot
plt.title('Water consumption of garden plants over a week')
# TODO: Label the x-axis as 'Day' and the y-axis as 'Water Consumption (gallons)'
plt.xlabel('Day')
plt.ylabel('Water Consumption (gallons)')

# TODO: Display the plot with the appropriate function
plt.show()