import pandas as pd
df=pd.DataFrame(
    {
     "Attendees":['pavan','sandeep','reddy','ganesh','sai','asha'],
     "numbers":[4,7,41,26,7,4],
     "Gender":['m','m','m','m','m','f']
     }
    )
print(df)
df_rollnumbers=df['numbers']
print(df_rollnumbers)
print("Max Roll :",df['numbers'].max())
print("Min Roll :",df['numbers'].min())
fil=df['numbers']>10
print(fil)
filter2=df['Gender']!='m'
print(filter2)
#approch 1
f1=df[df['numbers']>10]
print(f1)
print(pd.DataFrame(f1))