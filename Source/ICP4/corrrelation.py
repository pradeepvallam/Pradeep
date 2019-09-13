import pandas as pd
train_df = pd.read_csv('E:\python\Python_Lesson4\Python_Lesson4/train_preprocessed.csv')

out = train_df['Survived'].corr(train_df['Sex'])

print('correlation between survived and sex is: ',out)

