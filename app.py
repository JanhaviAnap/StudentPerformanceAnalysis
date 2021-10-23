import streamlit as st
import pickle

#Loading the pickle file
pickle_in = open("regression.pkl", "rb")
regressor = pickle.load(pickle_in)


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
romantic = col3.selectbox('In a romantic Relationship',('yes','no'))

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


def fun():
    st.write('age'+age)
    return
but = st.button("Click")

if but:
    print(age)