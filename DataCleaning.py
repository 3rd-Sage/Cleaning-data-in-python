# import necessary libraries
from operator import index
import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv('/Users/chinonsonnodebe/Desktop/Data Engineering/Data Cleaning Project/bank_marketing.csv')
# display initial information about the dataset
client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]
campaign = df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()
economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']]

# cleaning the education column
client['education'] = client['education'].str.replace('.', '_')
client['education'] = client['education'].replace('unknown', np.nan)

# clean the job column
client['job'] = client['job'].str.replace('.', '_')

# print(campaign)

for col in ['credit_default', 'mortgage']:
    client[col] = client[col].map({'yes': 1, 'no': 0, 'unknown': 0})
    client[col] = client[col].astype(bool)

# clean the campaign outcome columns
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1, 'no': 0, 'unknown': 0})
# convert the campaign outcome column to boolean type
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype(bool)

# clean the previous outcome column
campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 0, 'other': 0, 'unknown': 0, 'nonexistent': 0})
# convert the previous outcome column to boolean type
campaign['previous_outcome'] = campaign['previous_outcome'].astype(bool)


# create a new column called year 
campaign['year'] = '2022'

# currently the day and month columns are in integer format, we need to convert them to string format
campaign['day'] = campaign['day'].astype(str)
campaign['month'] = campaign['month'].astype(str)

# create a new column called date by combining the day, month and year columns
campaign['last_contact_date'] = campaign['day'] + '-' + campaign['month'] + '-' + campaign['year']
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'], format='%d-%b-%Y')

# drop the day, month and year columns
campaign = campaign.drop(columns=['day', 'month', 'year'])

# save the cleaned dataframes to new csv files
client.to_csv('/Users/chinonsonnodebe/Desktop/Data Engineering/Data Cleaning Project/cleaned_client_data.csv', index=False)
economics.to_csv('/Users/chinonsonnodebe/Desktop/Data Engineering/Data Cleaning Project/cleaned_economics_data.csv', index=False)
campaign.to_csv('/Users/chinonsonnodebe/Desktop/Data Engineering/Data Cleaning Project/cleaned_campaign_data.csv', index=False)