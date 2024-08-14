import matplotlib.pyplot as plt

# Sample data for countries and corresponding amounts
countries = ["Switzerland", "Germany", "Nepal", "Australia", "Angola", "Denmark", "Nauru", "Spain",
             "French Polynesia", "Cyprus", "Saint Barthelemy", "Montserrat", "Samoa", "Marshall Islands",
             "Gibraltar", "Reunion", "Heard Island and McDonald Islands", "France", "Lesotho", "Kiribati"]
percentages = [5] * len(countries)  # Each country accounts for 5% of the total

# Colors for each section of the chart
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c4e17f", "#ff6666",
          "#ffb366", "#d3e398", "#b3b3ff", "#ff7f50", "#ff6f61", "#c1f0f0", "#f7a35c", "#f15c80",
          "#e4d354", "#91e8e1", "#2b908f", "#f45b5b"]

# Plot the pie chart
plt.figure(figsize=(10, 6))
plt.pie(percentages, labels=countries, autopct='%1.1f%%', startangle=140, colors=colors)

# Add title
plt.title('Distribution of Customer Countries')
plt.show()
