import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


#Loading the pickle file
model = open("LinearRegressionModel.sav", "rb")
regressor = pickle.load(model)


st.title("Welcome!")


#Basic Information
basicinformation = st.container()
basicinformation.write("Basic Information:")
col1,col2,col3 = basicinformation.columns(3)
sex = col1.selectbox('Gender',('Male','Female'))
age = col2.number_input('Age', min_value=15, max_value=22, value=15)
address = col3.selectbox('Address',('Urban','Rural'))


#Academic Information
academic_info = st.container()
academic_info.write("Academic Information")

col1,col2,col3,col4 = academic_info.columns((1,1,1,1))
school = col1.selectbox('School',('Gabriel Pereira','Mousinho da Silveira'))
reason = col2.selectbox('Reason',('Close to Home','Reputation','Course Preference','other'))
studytime = col3.selectbox('Weekly Study Time',('Less than 2 hours','2 to 5 hours','5 to 10 hours','Greater than 10 hours'))
traveltime = col4.selectbox('Travel Time',('Less than 15 minutes','15 to 30 minutes','30 min to 1hr','Greater than 1hr'))

col1,col2,col3 = academic_info.columns(3)
schoolsupp = col1.selectbox('Extra Educational Support',('yes','no'))
paidclasses = col2.selectbox('Paid classes',('yes','no'))
extracurract = col3.selectbox('Extra Curricular Activites',('yes','no'))

col1,col2,col3,col4 = academic_info.columns(4)
nursery = col1.selectbox('Attended Nursery',('yes','no'))
higheredu = col2.selectbox('Wants to take Higher Edu.',('yes','no'))
failuers = col3.number_input('No. of past classes failuers', min_value=0, max_value=100, value=0)
absence = col4.number_input('No. of School absences', min_value=0, max_value=100, value=0)


#Personal Information
personal_info = st.container()
personal_info.write("Personal Information")

col1,col2,col3 = personal_info.columns(3)
internet = col1.selectbox('Internet access at home',('yes','no'))
health = col2.number_input('Health Status',min_value=1, max_value=5, value=3)
romantic = col3.selectbox('In a Romantic Relationship',('yes','no'))

col1,col2,col3,col4 = personal_info.columns(4)
freetime = col1.number_input('Free time after School',min_value=1, max_value=5, value=3)
goout = col2.number_input('Going out with friends',min_value=1, max_value=5, value=3)
workalc = col3.number_input('Workday alcohol comsumption',min_value=1, max_value=5, value=3)
weekalc = col4.number_input('Weekend alcohol comsumption',min_value=1, max_value=5, value=3)


#Family Information
family_info =st.container()
family_info.write("Family Information")

col1,col2,col3 = family_info.columns(3)
famsize = col1.selectbox('Family Size',('Less than or equal to 3','Greater than 3'))
parentstatus = col2.selectbox('Parents cohabitation status',('Living Together','Apart'))
guardian = col3.selectbox('Students Guardian',('Mother','Father','other'))

col1,col2,col3,col4 = family_info.columns(4)
medu = col1.selectbox("Mother's Education ",('None','Primary Education','5th to 9th Grade','Secondary Education','Higher Education'))
fedu = col2.selectbox("Father's Education ",('None','Primary Education','5th to 9th Grade','Secondary Education','Higher Education'))
mjob = col3.selectbox("Mother's Job",('Teacher','Healthcare','Civil Services','At Home','Other'))
fjob = col4.selectbox("Father's Job",('Teacher','Healthcare','Civil Services','At Home','Other'))

col1,col2 = family_info.columns(2)
familysupp = col1.selectbox('Family Educational Support',('yes','no'))
famrel = col2.number_input('Quality of family relationships',min_value=1, max_value=5, value=3)


#Grades Information
grades_info = st.container()
grades_info.write("Grades")

col1,col2 = grades_info.columns(2)
g1 = col1.number_input('First period Grade',min_value=0, max_value=20, value=3)
g2 = col2.number_input('Second period Grade',min_value=0, max_value=20, value=3)


but = st.button("Predict Grade3")

if but:
    inp = []
    if school == 'Gabriel Pereira':
        inp.append(0)
    else:
        inp.append(1)
    
    if sex == 'Male':
        inp.append(1)
    else:
        inp.append(0)

    inp.append(age)

    if address == 'Urban':
        inp.append(0)
    else:
        inp.append(1)
    
    if famsize == 'Greater than 3':
        inp.append(1)
    else:
        inp.append(0)

    if  parentstatus == 'Living Together':
        inp.append(1)
    else:
        inp.append(0)

    if medu == 'None':
        inp.append(0)
    elif medu == 'Primary Education':
        inp.append(1)
    elif medu == '5th to 9th Grade':
        inp.append(2)
    elif medu == 'Seconday Education':
        inp.append(3)
    else:
        inp.append(4)
    
    if fedu == 'None':
        inp.append(0)
    elif fedu == 'Primary Education':
        inp.append(1)
    elif fedu == '5th to 9th Grade':
        inp.append(2)
    elif fedu == 'Seconday Education':
        inp.append(3)
    else:
        inp.append(4)

    if mjob == 'Teacher':
        inp.append(1)
    elif mjob == 'At Home':
        inp.append(0)
    elif mjob == 'Healthcare':
        inp.append(2)
    elif mjob == 'Civil Services':
        inp.append(3)
    else:
        inp.append(4)

    if fjob == 'Teacher':
        inp.append(1)
    elif fjob == 'At Home':
        inp.append(0)
    elif fjob == 'Healthcare':
        inp.append(2)
    elif fjob == 'Civil Services':
        inp.append(3)
    else:
        inp.append(4)

    if reason == 'Close to Home':
        inp.append(0)
    elif reason == 'Reputation':
        inp.append(1)  
    elif reason == 'Course Preference':
        inp.append(2)
    else:
        inp.append(3)

    if guardian == 'Mother':
        inp.append(0)
    elif guardian == 'Father':
        inp.append(1)
    else:
        inp.append(2)

    if traveltime == 'Less than 15 minutes':
        inp.append(1)
    elif traveltime == '15 to 30 minutes':
        inp.append(2)
    elif traveltime == '30 min to 1hr':
        inp.append(3)
    else:
        inp.append(4)
    
    if studytime == 'Less than 2 hours':
        inp.append(1)
    elif studytime == '2 to 5 hours':
        inp.append(2)
    elif studytime == '5 to 10 hours':
        inp.append(3)
    else:
        inp.append(4)

    if failuers == 0 or failuers == 1 or failuers == 2 or failuers == 3:
        inp.append(failuers)
    else:
        inp.append(4) 

    if schoolsupp == 'no':
        inp.append(0)
    else:
        inp.append(1)

    if familysupp == 'no':
        inp.append(0)
    else:
        inp.append(1)

    if paidclasses == 'no':
        inp.append(0)
    else:
        inp.append(1)

    if extracurract == 'no':
        inp.append(0)
    else:
        inp.append(1)

    if nursery == 'no':
        inp.append(0)
    else:
        inp.append(1) 

    if higheredu == 'no':
        inp.append(0)
    else:
        inp.append(1)
    
    if internet == 'no':
        inp.append(0)
    else:
        inp.append(1)

    if romantic == 'no':
        inp.append(0)
    else:
        inp.append(1)
    
    inp.append(famrel)
    inp.append(freetime)
    inp.append(goout)
    inp.append(workalc)
    inp.append(weekalc)
    inp.append(health)
    inp.append(absence)
    inp.append(g1)
    inp.append(g2)

    
    
    result = regressor.predict(np.array(inp).reshape(1,-1))
    
    
    grade3 = 0
    if result[0] > 20 :
        grade3 = 20
    else:
        grade3 = round(result[0])

    
    col1,col2 = st.columns(2)

    col1.write("Predicted Grade3:")
    col2.write(grade3)