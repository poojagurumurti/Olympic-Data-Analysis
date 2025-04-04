import pandas as pd

# df = pd.read_csv('C:\\Users\\ptamragouri\\Documents\\PYTHON_COURSE\\Olympics-analysis-web-app\\athlete_events.csv')
# region_df = pd.read_csv('C:\\Users\\ptamragouri\\Documents\\PYTHON_COURSE\\Olympics-analysis-web-app\\noc_regions.csv')

def preprocess(df,region_df):
    # global df,region_df
    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on ='NOC', how ='left')
    #droppinf the duplicates
    df.drop_duplicates(inplace =True)
    #one hot encoding medals
    df= pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df