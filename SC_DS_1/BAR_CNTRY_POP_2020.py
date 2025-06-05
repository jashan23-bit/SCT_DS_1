# Importing necessary libraries for data manipulation and plotting
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame with top 10 most populated countries in 2020
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

# Loading the data into a pandas DataFrame
df = pd.DataFrame(data)

# Defining a list of custom colors to visually distinguish each country in the bar chart
colors = [
    '#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0',
    '#FFB6C1', '#F0E68C', '#DDA0DD', '#87CEFA', '#FFA07A'
]

# Plotting a bar chart to compare populations of the top 10 countries
plt.figure(figsize=(12, 6))
plt.bar(df['Country Name'], df['Population_2020'], color=colors)

# Adding titles and labels for clarity
plt.title('Top 10 Most Populated Countries in 2020')
plt.xlabel('Country')
plt.ylabel('Population')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Adding grid lines for visual clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Making layout tighter for display
plt.tight_layout()

# Displaying the plot
plt.show()
