# dash_crm_sync

# Company Matching Script
This Python script is designed to process a CSV file containing information about company names, parent-child relationships, and similarity scores, and output the matching results in JSON format. The script aims to simplify the structure of the matching results for easier analysis, manipulation and to determine matching entities in CRM-DASH. 

## Purpose
The primary purpose of this script is to match companies based on their similarity scores and create a structured output that represents the parent-child relationships between companies along with their similarity scores.

## Input Format
The script expects the input data to be in a CSV file with the following columns:

Account Name CRM: The name of the company in the CRM system.
Parent ID: An optional field representing the parent company's ID. This field can be used to establish parent-child relationships.
Account Name DASH: The name of the company in another system (e.g., DASH).
Similarity: A similarity score indicating how closely the two company names match.

## Output Format
The script generates two types of output:

### 1. JSON Output
The matching results are stored in a JSON file. The structure of the JSON output is as follows:
``` json
{
    "1st Bank": {
        "id": null,  # Parent company's ID (can be assigned later)
        "child-companies": [
            {
                "id": null,  # Child company's ID (can be assigned later)
                "similarity": 0.8284,  # Similarity score
                "companyName": "(blank)"  # Name of the child company
            },
            {
                "id": null,
                "similarity": 0.6318,
                "companyName": "3411 1st Avenue Point, LLC "
            }
        ]
    },
    "Another Parent Company": {
        "id": null,
        "child-companies": [
            {
                "id": null,
                "similarity": 0.95,
                "companyName": "Another Matching Company"
            },
            {
                "id": null,
                "similarity": 0.75,
                "companyName": "Yet Another Matching Company"
            }
        ]
    },
    ...
}
```
### 2. Dictionary Output
The script also prints the matching results as a dictionary in the console. Each entry in the dictionary represents a parent company with its child companies and similarity scores.

## Usage
Ensure you have Python installed on your system.

Place the input CSV file named dict.csv in the same directory as the script.

Run the script using a Python interpreter.

The script will process the input data, match companies based on similarity scores, and generate the JSON output.

## Note

The Fuzzy Lookup is done in Excel. Ask Phil for details. 

Assign IDs to both parent and child companies, which can be useful for further analysis or integration with other systems.

You can adjust the similarity threshold (threshold) in the script to control which matches are considered.

The script uses various encodings to read the CSV file, ensuring compatibility with different file formats.


