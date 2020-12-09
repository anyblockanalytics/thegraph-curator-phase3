import pandas as pd


# Useable for all DF -> Json to DF, Used to Input the Output of getGrapQuery into a DF
def graphQueryToDf(json_data):	
    df = pd.DataFrame(json_data.get(next(iter(json_data)), []))
    return df
    
# Concat Columns which have dictionaries with maindf
def concatDictColumns(df):
    for sub_dict_col in [col for col in df.columns if isinstance(df[col][0],dict)]:
        df = pd.concat([df.drop([sub_dict_col], axis=1), df[sub_dict_col].apply(pd.Series)], axis=1)
    return df


# lets say we have columns which have same name "id"
# this takes the dataframe and colName as input (df and "id")
# and renames all occurences by counting the colName+1
def renameDuplicateColName(df, colName):
    cols = []
    count = 1
    for column in df.columns:
        if column == colName:
            cols.append(f'Goods_{count}')
            count+=1
            continue
        cols.append(column)
    df.columns = cols
    return df