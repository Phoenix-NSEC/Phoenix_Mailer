import pandas as pd
import json 


def csv_praser(file_name,file):
    if(file_name.endswith('.csv')):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    emails = list(df.loc[:,'Email Address'])
    names = list(df.loc[:,'Name'])
    mydict = {k:v for k,v in zip(names,emails)}
    jdict = json.dumps(mydict)
    return jdict

