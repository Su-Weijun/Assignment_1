import pandas as pd
import sys

def clean_data(contact_info_file, other_info_file, output_file):
    # (1) Merge the two input data files based on the ID of each respondent.
    df_contact = pd.read_csv(contact_info_file)
    df_other = pd.read_csv(other_info_file)
    merged_df = pd.merge(df_contact, df_other, left_on='respondent_id', right_on='id')

    # (2) Drop any rows with missing values.
    cleaned_df = merged_df.dropna()

    # (3) Drop rows if the job value contains 'insurance' or 'Insurance'.
    cleaned_df = cleaned_df[~cleaned_df['job'].str.contains('insurance', case=False)]

    # (4) Write the cleaned data to the file specified by the output_file argument.
    cleaned_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']].to_csv(output_file, index=False)

if __name__ == '__main__':
    contact_info_file = sys.argv[1]
    other_info_file = sys.argv[2]
    output_file = sys.argv[3]
    clean_data(contact_info_file, other_info_file, output_file)