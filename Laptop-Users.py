'''
Here is the Python code to create a line plot: relationship between age and income.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Create two separate dataframes for users with and without laptops
laptop_users = data[data['Has Laptop'] == 'yes']
no_laptop_users = data[data['Has Laptop'] == 'no']

# Plot line graph
plt.plot(laptop_users['Age'], laptop_users['Income'], color='blue', label='Has Laptop')
plt.plot(no_laptop_users['Age'], no_laptop_users['Income'], color='red', label='No Laptop')

# Set axis labels and title
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Relationship between Age and Income')

# Add legend
plt.legend()

# Show plot
plt.show()

'''
Here is the python code to create this line plot: relationship between Age and Income for Laptop Users by Region
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Group data by Region and Age, calculate mean Income for each group
grouped_data = data.groupby(['Region', 'Age']).mean().reset_index()

# Create separate datasets for City and Countryside regions
city_data = grouped_data[grouped_data['Region'] == 'city']
countryside_data = grouped_data[grouped_data['Region'] == 'countryside']

# Plot line for City region
plt.plot(city_data['Age'], city_data['Income'], color='blue', label='City')

# Plot line for Countryside region
plt.plot(countryside_data['Age'], countryside_data['Income'], color='red', label='Countryside')

# Set axis labels and title
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Relationship between Age and Income for Laptop Users by Region')

# Add legend
plt.legend()

# Display plot
plt.show()


'''
Here is the python code to create this line plot: relationship between Income and Occupation for Laptop Users
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Group data by Occupation, calculate mean Income for each group
grouped_data = data.groupby('Occupation').mean().reset_index()

# Plot the line
plt.plot(grouped_data['Occupation'], grouped_data['Income'], color='green')

# Set axis labels and title
plt.xlabel('Occupation')
plt.ylabel('Income')
plt.title('Relationship between Income and Occupation for Laptop Users')

# Display plot
plt.show()

'''
Here is the python code to create this line plot: relationship between Age and Income for Laptop Users by Occupation
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Group data by Occupation and Age, calculate mean Income for each group
grouped_data = data.groupby(['Occupation', 'Age']).mean().reset_index()

# Plot the lines
colors = {'banker': 'green', 'officer': 'blue', 'student': 'red', 'teacher': 'orange'}
for occupation in ['banker', 'officer', 'student', 'teacher']:
    filtered_data = grouped_data[grouped_data['Occupation'] == occupation]
    plt.plot(filtered_data['Age'], filtered_data['Income'], color=colors[occupation], label=occupation)

# Set axis labels and title
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Relationship between Age and Income for Laptop Users by Occupation')
plt.legend()

# Display plot
plt.show()

'''
Here is the python code to create bar plot: number of Laptop Users and Non-Laptop Users by Region
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Count number of Laptop Users and Non-Laptop Users by Region
region_counts = data.groupby(['Region', 'Has Laptop'])['Age'].count().reset_index()

# Pivot table to put count of laptop users in new column
region_counts = region_counts.pivot(index='Region', columns='Has Laptop', values='Age')

# Plot the bar plot
ax = region_counts.plot(kind='bar', stacked=True)

# Set axis labels and title
ax.set_xlabel('Region')
ax.set_ylabel('Number of Users')
ax.set_title('Number of Laptop Users and Non-Laptop Users by Region')

# Display plot
plt.show()

'''
Here is the python code to create scatter plot: relationship between Age and Income for Laptop Users
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("laptop-users.csv")

# Filter data for Laptop Users
laptop_users = data[data['Has Laptop'] == 'yes']

# Plot the scatter plot
plt.scatter(laptop_users['Age'], laptop_users['Income'])

# Set axis labels and title
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Relationship between Age and Income for Laptop Users')

# Display plot
plt.show()

'''
Here is the python code to create scatter plot: Relationship between age and income for laptop users by gender
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.scatter(laptop_users[laptop_users['Gender'] == 'male']['Age'], laptop_users[laptop_users['Gender'] == 'male']['Income'], alpha=0.5, color='blue', label='Male')
plt.scatter(laptop_users[laptop_users['Gender'] == 'female']['Age'], laptop_users[laptop_users['Gender'] == 'female']['Income'], alpha=0.5, color='red', label='Female')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Relationship between Age and Income for Laptop Users by Gender')
plt.legend()

'''
Here is the python code to create scatter plot: Relationship between income and occupation for laptop users
'''
import pandas as pd
import matplotlib.pyplot as plt

plt.scatter(laptop_users['Income'], laptop_users['Occupation'], alpha=0.5)
plt.xlabel('Income')
plt.ylabel('Occupation')
plt.title('Relationship between Income and Occupation for Laptop Users')
