import pandas as pd
import json


def to_json1(df, orient='split'):
    return df.to_json(orient=orient, force_ascii=False)


def to_json2(df, orient='split'):
    df_json = df.to_json(orient=orient, force_ascii=False)
    return json.loads(df_json)


