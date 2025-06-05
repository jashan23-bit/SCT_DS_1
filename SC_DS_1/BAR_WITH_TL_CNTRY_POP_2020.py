# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Creating population dataset for the top 10 most populous countries in 2020
data = {
    'Country Name': [
        'China', 'India', 'United States', 'Indonesia', 'Pakistan',
        'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'
    ],
    'Population_2020': [
        1439323776, 1380004385, 331002651, 273523621, 220892331,
        212559409, 206139589, 164689383, 145912025, 128932753
    ]
}

# Loading the data into a DataFrame for analysis
df = pd.DataFrame(data)

# Setting up custom colors for each country bar
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb6c1', '#f0e68c', '#dda0dd', '#87cefa', '#ffa07a'
]

# Creating a bar chart to show population with a line graph overlaid
plt.figure(figsize=(12, 6))

# Bar chart - visualizing population values
bars = plt.bar(
    df['Country Name'], df['Population_2020'], 
    color=colors, edgecolor='black', label='Population'
)

# Line graph on top of the bars - to show population trend
plt.plot(
    df['Country Name'], df['Population_2020'], 
    marker='o', color='black', linewidth=2, label='Trend'
)

# Title and labels
plt.title('Population of Top 10 Most Populous Countries (2020)')
plt.xlabel('Country')
plt.ylabel('Population')

# Rotating country names for better readability
plt.xticks(rotation=45)

# Adding a legend to explain bar and line
plt.legend()

# Improving layout so nothing gets cut off
plt.tight_layout()

# Display the chart
plt.show()
