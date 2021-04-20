# import pandas
import pandas as pd

# read csv data
df1 = pd.read_excel('ICICI_mar_post_data.xlsx')
df2 = pd.read_excel('vashi_final_till_31_mar.xlsx')

inner_join = pd.merge(df1,
                      df2,
                      on='barcode',
                      how='left')
print(inner_join)
inner_join.to_excel("test.xlsx")
