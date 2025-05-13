import pandas as pd
# df=pd.read_csv('dataframe.csv')
# print(df)
# new_df=df.dropna() #dropping the null value
# print(new_df)


#replacement
# df.dropna(inplace=True)
# print(df)

#keeping the in null field
# df.fillna(130,inplace=True)
# print(df)

#keeping value in calories NaN --- null value
# df.fillna({"Calories": 140}, inplace=True)
# print(df)

#calculating mean and keeping the value of mean in calories
# x= df["Calories"].mean()
# df.fillna({"Calories":x}, inplace=True)
# print(df)



df=pd.read_csv('dataframe.csv')
df.dropna(inplace=True)
df["Date"] =pd.to_datetime(df["Date"], format="mixed")
print(df)

#setting duration =45 in row 7
df.loc[7, 'Duration'] = 45
print(df)
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)
df.to_csv("Output.csv", index=False)

