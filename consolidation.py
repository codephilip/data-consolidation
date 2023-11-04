import pandas as pd
import json

# Try reading the CSV file with different encodings (e.g., 'latin1' or 'ISO-8859-1')
encodings_to_try = ['utf-8', 'latin1', 'ISO-8859-1']

# Initialize the DataFrame
df = None

# Iterate through encodings and attempt to read the CSV file
for encoding in encodings_to_try:
    try:
        df = pd.read_csv('dict.csv', encoding=encoding)
        break  # Stop when successful reading is achieved
    except UnicodeDecodeError:
        pass  # Continue to the next encoding if decoding fails

# Check if the DataFrame was successfully read
if df is None:
    print("Unable to read the CSV file with any encoding.")
else:
    # Continue with the rest of the code for data processing
    # Create a dictionary to store matches
    matches = {}

    # Iterate through the DataFrame rows
    for index, row in df.iterrows():
        companyA = row['Account Name CRM']  # Update column name to 'Account Name CRM'
        companyB = row['Account Name DASH']  # Update column name to 'Account Name DASH'
        similarity_index = row['Similarity']  # Update column name to 'Similarity'

        # Define a threshold for considering a match based on your similarity index
        threshold = 0.6  # Adjust as needed

        # Create an entry for the parent company if it doesn't exist
        if companyA not in matches:
            matches[companyA] = {
                'id': None,  # getting type error. TODO: fix
                'child-companies': []
            }

        # Append the matching child company with similarity, ID, and company name
        child_company = {
            'id': None,  # getting type error. TODO: fix
            'similarity': similarity_index,
            'companyName': companyB if isinstance(companyB, str) else None
        }

        matches[companyA]['child-companies'].append(child_company)

    # Create a new DataFrame to store the results
    results_df = pd.DataFrame({
        'Company Name CRM': list(matches.keys()),  # Update column name to 'Company Name CRM'
        'Matching Companies DASH': [', '.join([child['companyName'] if child['companyName'] else '' for child in match['child-companies']]) for match in matches.values()]  # Update output column name to 'Matching Companies DASH'
    })

    # Print the results DataFrame
    print("Results in DataFrame format:")
    print(results_df)

    # Export the results DataFrame to a CSV file
    results_df.to_csv('matching_results.csv', index=False)

    # Write the results in JSON format to a file
    with open('matching_results4.json', 'w') as json_file:
        json.dump(matches, json_file, indent=4)

    # Print the results in dictionary format
    print("\nResults in Dictionary format:")
    print(matches)
