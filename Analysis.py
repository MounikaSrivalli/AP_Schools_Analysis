# importing the required modules
import pandas as pd
import seaborn as sns
import matplotlib as plt
# Reading CSV File
data = pd.read_csv("D:/Mentorskool/Project School/Districts/ANANTAPUR/anantapur_dist.csv")

'''cleaning the data'''
# droping the no need values
no_need=['Village/Town','Cluster','Block','District','School Shifted to New Place','Head Teacher']
data.drop(labels=no_need,axis=1,inplace=True)

# dropping all Null Values in the Data
data = data.dropna()

''' checking the shapes of the N/A having columns'''

# print(data[data['Wall']==' N/A'].shape)
# print(data[data['Library']==' N/A'].shape)
# print(data[data['Playground']==' N/A'].shape)
# print(data[data['Ramps for Disable']==' N/A'].shape)
# print(data[data['Building']==' N/A'].shape)


''' as above shows all the data in their columns Was N/A. so these are not usefull for analysis we can drop them '''
data.drop(labels=['Wall','Library','Playground','Ramps for Disable','Building'],axis=1,inplace=True)
# print(data.shape)

''' 
lets go into deeper analysis 
Pre Primary Sectin Avilable,Computer Aided Learning,Electricity
the data in these columns are same kind of data i.e yes or no type.
lets check the shape of them
'''
# print(data[data['Pre Primary Sectin Avilable']==' No'].shape)
# print(data[data['Computer Aided Learning']==' No'].shape)
# print(data[data['Electricity']==' No'].shape)

'''
Computer Aided Learning,Electricity these two columns has No value for all columns. we cant use this for analysis, we can drop them
'''

data.drop(labels=['Computer Aided Learning','Electricity'],axis=1,inplace=True)

'''
we have Total Teachers count and also we have famale and male teachers count,so these individual count doesn't make any sence
'''

data.drop(labels=['Female Teacher','Male Teachers'],axis=1,inplace=True) 

'''
Pre Primary Teachers,Head Teachers,Contract Teachers,Class Rooms,Boys Toilet,Girls Toilet,Books in Library,Computers,Total Teachers
These columns having same kind of data i.e integer type
if all rows of this columns contains 0 then that coulumn will not be usefull.
so we can check that and drop those columns
'''
# print(data[data['Pre Primary Teachers']== 0 ].shape)
# print(data[data['Head Teachers']== 0 ].shape)
# print(data[data['Contract Teachers']==0].shape)
# print(data[data['Class Rooms']== 0 ].shape)
# print(data[data['Boys Toilet']== 0 ].shape)
# print(data[data['Girls Toilet']== 0 ].shape)
# print(data[data['Books in Library']== 0 ].shape)
# print(data[data['Computers']== 0 ].shape)
# print(data[data['Total Teachers']== 0 ].shape)

'''
as the Contract Teachers,Class Rooms,Boys Toilet,Girls Toilet,Books in Library,Computers columns has all zero then we can drop them.
'''

data.drop(labels=['Contract Teachers','Class Rooms','Boys Toilet','Girls Toilet','Books in Library','Computers'],axis=1,inplace=True)

# print(data[data['Meal']== ' Meal Not Applicable' ].shape)
# print(data[data['Drinking Water']== ' None' ].shape)
''' as these two columns also not useful comparing '''
data.drop(labels=['Meal','Drinking Water'],axis=1,inplace=True)

data.groupby('Instruction Medium')
med_eng = data.loc[data['Instruction Medium'] == ' English']
med_otrs = data.loc[data['Instruction Medium'] != ' English']
med_eng_cbse = med_eng.loc[med_eng['Board for Class 10th'] == 'CBSE']
med_eng_sboard = med_eng.loc[med_eng['Board for Class 10th'] == 'State Board']
sns.set(rc={"figure.figsize":(20, 4)})
sns.barplot(data =med_eng_cbse, y= med_eng_cbse['Establishment'],x= med_eng_cbse['UDISE Code'])
