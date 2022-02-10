def mass_groupby(df, list_of_categoricals, target):
    
    """
    With a DataFrame and a list of categorical variables,
    iterates through list of categorical variables,
    grouping the df by each and looking at the mean target
    """
    
    for cat in list_of_categoricals:
        temp_groupby = df.groupby(cat)[target].mean().sort_values()
        print(f' Grouped By {cat}: \n {temp_groupby}\n')
        
def dummy_and_merge(df, column):
     return pd.concat([df, pd.get_dummies(df[column])],axis=1).drop(columns=column)
    
def ordinal_to_numerical(df, column):

    """
    Converts ordinal variables to numerical values
    
    Only works for scales of Excellent-Poor/NA
    """
    
    
    replace_dict = {
        'Ex':5,
        'Gd':4,
        'TA':3,
        'Fa':2,
        'Po':1
    }
    
    for key, value in replace_dict.items():
        df[column] = df[column].replace(key,value)
        
    df[column].fillna(0,inplace=True)
    
    return df[column]

def mass_ordinal_to_numerical(df, list_of_columns):
    
    """
    Use this to call ordinal_to_numerical on a list of columns
    """
    for col in list_of_columns:
        ordinal_to_numerical(df, col)
        
    return

def simple_interaction_feature(df, list_of_old_features):
    new_feature_val = 1
    for feature in list_of_old_features:
        new_feature_val = new_feature_val * df[feature]
    return new_feature_val