import pandas as pd

Names = ["Yahia", "Mahmoud", "Ali", "ibrahim", "Hassanain"]
c1 = ["Email:hhhhhaha","Telephone:2023", "Mobile:111111", "Skype:1", "Skype:1"]
c2 = ["Mobile:2222222", "Email:xxxxxx","Telephone:2023", "Skype:2", "Skype:2" ]
c3 = ["Email:2025", "Messenger:zzzzz", "Twitter:333333", "Skype:3", "Skype:3"]


d = {'Names': Names, 'c_1': c1, 'c_2':c2, 'c_3':c3}
df = pd.DataFrame(data=d)

def split_contacts(data, index):

  data = data.set_index('Names')
  
  row_contacts = []
  
  for i in data.iloc[index].values:
    row_contacts.append(i.split(':'))
  
  return row_contacts

def convert_to_dict(data):
  result = {}
  counter = {}

  for key, value in data:
    count = counter.get(key, 0) + 1
    counter[key] = count
    result[f"{key}_{count}"] = value

  return result

def organize_df(df):
  
  df_in_dict = {}
  
  for i in range(len(df)):
    df_in_dict[f"{df['Names'].iloc[i]}"] = convert_to_dict(split_contacts(df,i))
  
  df_organized = pd.DataFrame(df_in_dict)\
    .sort_index().T.reset_index().rename(columns={'index': 'Names'})
  
  return df_organized

print(organize_df(df))