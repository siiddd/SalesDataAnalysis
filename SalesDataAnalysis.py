#Import Packages
import pandas as pd
import numpy as np
import seaborn as sns

#Import Dataset 
df = pd.read_excel(r'C:\Users\nsid4\Desktop\A2.xlsx')

#Check for missing values
df.isna().sum().sum()

#Manipulate the DataFrame for Easy Computation
df_transpose = df.transpose()
df_transpose.columns = df_transpose.iloc[0]
df_transpose.drop(df_transpose.index[0], inplace = True)
dates = df.columns[1:]
df_transpose.index = pd.to_datetime(df_transpose.index)


#Make index as Months
df_monthly_sales = df_transpose
df_monthly_sales.index = df_monthly_sales.index.strftime('%B')

#Make index as Quarters
df_quarterly_sales = df_transpose
df_quarterly_sales.index = df_quarterly_sales.index.quarter

#Monthly Sales
Monthly = df_monthly_sales.groupby([df_monthly_sales.index])

January = pd.DataFrame(Monthly.get_group('January').sum(), columns=['Jan'])
February = pd.DataFrame(Monthly.get_group('February').sum(), columns=['Feb'])
March = pd.DataFrame(Monthly.get_group('March').sum(), columns=['Mar'])
April = pd.DataFrame(Monthly.get_group('April').sum(), columns=['Apr'])
May = pd.DataFrame(Monthly.get_group('May').sum(), columns=['May'])
June = pd.DataFrame(Monthly.get_group('June').sum(), columns=['Jun'])
July = pd.DataFrame(Monthly.get_group('July').sum(), columns=['Jul'])
August = pd.DataFrame(Monthly.get_group('August').sum(), columns=['Aug'])
September = pd.DataFrame(Monthly.get_group('September').sum(), columns=['Sep'])
October = pd.DataFrame(Monthly.get_group('October').sum(), columns=['Oct'])
November = pd.DataFrame(Monthly.get_group('November').sum(), columns=['Nov'])
December = pd.DataFrame(Monthly.get_group('December').sum(), columns=['Dec'])

df_monthly_data = pd.concat([January, February, March, April, May, June, July, August, September, October, November, December], axis = 1)

#Visualize Monthly Sales Data
sns.barplot(data = df_monthly_data).set_title('Monthly Sales Data')


#Quarterly Sales
Quarterly = df_quarterly_sales.groupby([df_quarterly_sales.index])

Q1 = pd.DataFrame(Quarterly.get_group(1).sum(), columns = ['Q1'])
Q2 = pd.DataFrame(Quarterly.get_group(2).sum(), columns = ['Q2'])
Q3 = pd.DataFrame(Quarterly.get_group(3).sum(), columns = ['Q3'])
Q4 = pd.DataFrame(Quarterly.get_group(4).sum(), columns = ['Q4'])

df_quarterly_data = pd.concat([Q1, Q2, Q3, Q4],axis = 1)

#Visualize Quarterly Sales Data
sns.barplot(data = df_quarterly_data).set_title('Quarterly Sales Data')
