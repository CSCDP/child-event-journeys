import pandas as pd

# Useful dictionaries

# Events we want to include in the child journeys
journey_events = {'contact': {'List_1':'Date of Contact'},
          'early_help_assessment_start': {'List_2':'Assessment start date'},
          'early_help_assessment_end': {'List_2':'Assessment completion date'},
          'referral': {'List_3':'Date of referral'},
          'assessment_start': {'List_4':'Continuous Assessment Start Date'},
          'assessment_authorised':{'List_4':'Continuous Assessment Date of Authorisation'},
          's47': {'List_5': 'Strategy discussion initiating Section 47 Enquiry Start Date'},
          'icpc': {'List_5': 'Date of Initial Child Protection Conference'},
          'cin_start': {'List_6': 'CIN Start Date'},
          'cin_end': {'List_6': 'CIN Closure Date'},
          'cpp_start': {'List_7': 'Child Protection Plan Start Date'},
          'cpp_end': {'List_7': 'Child Protection Plan End Date'},
          'lac_start': {'List_8': 'Date Started to be Looked After'},
          'lac_end': {'List_8': 'Date Ceased to be Looked After'}}

# Abbreviations for events (for the "journeys reduced")
events_map = {'contact': 'C',
        'referral': 'R',
        'early_help_assessment_start': 'EH',
        'early_help_assessment_end': 'EH|',
        'assessment_start': 'AS',
        'assessment_authorised': 'AA',
        's47': 'S47',
        'icpc': 'ICPC',
        'cin_start': 'CIN',
        'cin_end': 'CIN|',
        "cpp_start": 'CPP',
        "cpp_end": 'CPP|',
        "lac_start": 'LAC',
        "lac_end": 'LAC|'}


# Functions

def build_annexarecord(input_file, events=journey_events):
    '''
    Creates a flat file with three columns:
    1) child unique id
    2) Date
    3) Type
    Based on events in Annex A lists defined in the events argument
    '''

    # Create empty dataframe in which we'll drop our events
    df_list = []

    # Loop over our dictionary to populate the log
    for event in events:
        contents = events[event]
        list_number = list(contents.keys())[0]
        date_column = contents[list_number]
        
        # Load Annex A list
        df = pd.read_excel(input_file, sheet_name=list_number) 
        
        # Get date column information
        df.columns = [col.lower().strip() for col in df.columns]
        date_column_lower = date_column.lower()
        if date_column_lower in df.columns:
            df = df[df[date_column_lower].notnull()]
            df['Type'] = event
            df['Date'] = df[date_column_lower]
            df_list.append(df)
        else:
            print('>>>>>  Could not find column {} in {}'.format(date_column, list_number))
    
    # Pull all events into a unique datafrane annexarecord
    annexarecord = pd.concat(df_list, sort=False)
    
    # Clean annexarecord
    # Define categories to be able to sort events
    ordered_categories = ["contact",
                      "referral",
                      "early_help_assessment_start",
                      "early_help_assessment_end",
                      "assessment_start",
                      "assessment_authorised",
                      "s47",
                      "icpc",
                      "cin_start",
                      "cin_end",
                      "cpp_start",
                      "cpp_end",
                      "lac_start",
                      "lac_end"]
    annexarecord.Type = annexarecord.Type.astype('category')
    annexarecord.Type.cat.set_categories([c for c in ordered_categories if c in annexarecord.Type.unique()], inplace=True, ordered=True)
    # Ensure dates are in the correct format
    annexarecord.Date = pd.to_datetime(annexarecord.Date)
    
    return annexarecord


def joined_string(series):
    """
    Turns all elements from a series into a string, joining elements with "->"
    """
    list_elements = series.tolist()
    return " -> ".join(list_elements)


def create_journeys(df, output_file):
    df = df[~df["Date"].isnull()]
    df = df[~df["Type"].isnull()]
    df = df.sort_values(['Date', 'Type'])
    
    # Add new column showing each event in format [00-00-0000/event]
    df["TimeEvent"] = "[" + df.Date.astype(str) + "/" + df.Type.astype(str) + "]"
    
    # Add new column showing each event in reduced form e.g. "C" for contact
    df["reduced"] = df.Type.map(events_map)
    
    # Create both long and reduced journeys
    grouped = df.groupby("child unique id")
    journey_long = grouped['TimeEvent'].apply(joined_string)
    journey_reduced = grouped['reduced'].apply(joined_string)
    
    # Create new dataframe with both long and reduced journeys
    journeys_df = pd.DataFrame({'Child journey': journey_long, 'Child journey reduced': journey_reduced}, index=journey_long.index)
    
    # Save to Excel
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    # Journeys
    journeys_df.to_excel(writer, sheet_name='Child journeys')
    # Events abbreviation
    pd.DataFrame({'Event': list(events_map.keys()), 'Reduced': list(events_map.values())}).to_excel(writer, sheet_name='Legend', index=None)
    writer.save()
    
    return print('Child journeys are done! Have a look in {}'.format(output_file))


