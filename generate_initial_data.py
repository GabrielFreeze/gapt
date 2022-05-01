import os
import pandas as pd

read_path = os.path.join(os.getcwd(),'data')
write_path = os.path.join(os.getcwd(),'data')

#Original datset received from https://www.kaggle.com/datasets/vinicius150987/titanic3
filename = 'titanic_original.csv'
df = pd.read_csv(os.path.join(read_path,filename))

#Rename columns
df.columns = ['Pclass','Survived','Name','Sex','Age','SibSp','Parch',
              'Ticket','Fare','Cabin','Embarked','Boat','Body','Home.dest']

#Rearrange columns
new_columns = ['Survived','Pclass','Name','Sex','Age','SibSp','Parch',
              'Ticket','Fare','Cabin','Embarked','Boat','Body','Home.dest']
df = df[new_columns]

#Drop unused columns
df = df.drop(['Boat','Body','Home.dest'],1)

#Drop rows with no information
df = df.dropna(how='all')


#Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

#Save new dataset
df.to_csv(os.path.join(write_path,'titanic.csv'), index=False)


