# Import pandas
import pandas as pd

# Create python dictionary of name, age and country
data = {'Name': ['Ese Amadasun', 'Treasure Amadasun', 'Evans Amadasun', 'Vanessa Amadasun'],
        'Age': [48, 16, 14, 8],
        'Country': ['Nigerian', 'United States', 'Canada', 'United Kingdom']
        }

# Convert the dictionary to a dataframe
converted_df = pd.DataFrame(data)

# Display the dataframe
print(converted_df)