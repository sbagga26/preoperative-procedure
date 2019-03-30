#this program is basically for finding out the pre-operative procedure that needs to be performed according
#to the data provided by the user and using our database to find out 

#!/usr/bin/python36

import xlrd
import pandas as pd
from variables import *
df=pd.read_excel('/root/Desktop/Project/Metadata.xlsx',sheet_name='Surgical Grade {}'.format(sg)) #edit the location of your metafile downloaded
col=df[age]=='Y'
print (df[col]['Test'])

if diabetes=='ON' or hypertension=='ON' or asthma=='ON' or thyroid=='ON' or copd=='ON' or meds=='ON':
	df=pd.read_excel('/root/Desktop/Project/Metadata.xlsx',sheet_name='Chronic Illness') #edit the location of your metafile downloaded

	if diabetes=='ON':
		col=df['Diabetes']=='Y'
		print(df[col]['Test'])
	if hypertension=='ON':
		col=df['Hypertension']=='Y'
		print(df[col]['Test'])
	if asthma=='ON':
		col=df['Asthma']=='Y'
		print(df[col]['Test'])
	if thyroid=='ON':
		col=df['Thyroid']=='Y'
		print(df[col]['Test'])
	if copd=='ON':
		col=df['COPD']=='Y'
		print(df[col]['Test'])
	if meds=='ON':
		col=df['Medications']=='Y'
		print(df[col]['Test'])

elif asa==2:
	df=pd.read_excel('/root/Desktop/Project/Metadata.xlsx',sheet_name='ASA 2') #edit the location of your metafile downloaded
	if reg=='cvs':
		col=df['CVS']=='Y'
		print(df[col]['Test'])
	elif reg=='rs':
		col=df['RS']=='Y'
		print(df[col]['Test'])
	elif reg=='renal':
		col=df['Renal']=='Y'
		print(df[col]['Test'])

elif asa==3:
	df=pd.read_excel('/root/Desktop/Project/Metadata.xlsx',sheet_name='ASA 3') #edit the location of your metafile downloaded
	if reg=='cvs':
		col=df['CVS']=='Y'
		print(df[col]['Test'])
	elif reg=='rs':
		col=df['RS']=='Y'
		print(df[col]['Test'])
	elif reg=='renal':
		col=df['Renal']=='Y'
		print(df[col]['Test'])
