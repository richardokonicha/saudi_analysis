import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Response Id': ['TOCfzxpJdjG0AfXJpIuc', 'asChH1Fz7zSLLMJtzotu', 'qhCCVWPSQw3U6Zr6UyMe'],
    'Date': ['Dec 23, 2023', 'Dec 23, 2023', 'Dec 23, 2023'],
    'Interest Level': [9, 9, 9],
    'Watching Movies': [7, 7, 5],
    'Archeological Sites': [6, 4, 7],
    'Heritage & Cultural Festivals': [5, 1, 3],
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('sample_data.xlsx', index=False)

print("Sample Excel file created: sample_data.xlsx")
