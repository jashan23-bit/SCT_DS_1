# Importing libraries to work with data and create plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the data: Country names and their populations in 2020
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

# Putting the data into a table using pandas
df = pd.DataFrame(data)

# Sorting the table so countries with the smallest population come first
df = df.sort_values(by='Population_2020', ascending=True)

# Setting a nice style for the plot
sns.set_style("whitegrid")

# Making the plot area bigger so everything fits well
plt.figure(figsize=(12, 8))

# Creating a horizontal bar plot showing population for each country
barplot = sns.barplot(
    x='Population_2020',     # Population values on the x-axis
    y='Country Name',        # Country names on the y-axis
    data=df,                 # Data source is our table (df)
    palette='viridis'        # Nice color theme for the bars
)

# Adding the population numbers on each bar
for index, value in enumerate(df['Population_2020']):
    plt.text(value + 1e7, index, f'{value:,}', va='center', fontsize=10)  # Adds text next to each bar

# Giving the plot a title and labeling the axes
plt.title('Top 10 Most Populous Countries in 2020', fontsize=16, fontweight='bold')
plt.xlabel('Population', fontsize=12)
plt.ylabel('Country', fontsize=12)

# Adjusts layout so labels and plot don't overlap
plt.tight_layout()

# Showing the final plot
plt.show()

