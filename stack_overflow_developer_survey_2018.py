
#---Stack Overflow Survey------------------------------------------------------

# Stack Overflow is a question and answer site for professional and enthusiast
# programmers. It's built and run as part of the Stack Exchange network.
# Each month, over 50 million developers visit Stack Overflow to learn and 
# share their knowledge.

#---Working Directory----------------------------------------------------------

import os
os.getcwd()
os.chdir(r'/Users/yossigausman/Desktop/DSA/PDA/Working Directory')

#---Libraries------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 20

#---Data Loading---------------------------------------------------------------

raw_data = pd.read_csv("survey_results_public.csv", na_values='NA')
raw_data.head()

#---1.General Overview---------------------------------------------------------

#---1.1 Roles of Developers that took part in the survey-----------------------

raw_data['DevType'].value_counts(dropna=True)[:20].plot(kind='barh',
        figsize=(9,6), title="Developer Roles")

#---1.2 IDE's Data Scientists--------------------------------------------------

d_scientists = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','IDE']
d_scientists_df = pd.DataFrame(d_scientists)

d_scientists_df = d_scientists_df.dropna()

split_IDE = pd.DataFrame(d_scientists_df.IDE.str.split(';').tolist())
stacked_IDE=split_IDE.stack()

stacked_IDE.value_counts()[:15].plot(kind='barh', figsize=(9,6),
                         title="Data Scientists")

#---1.3 IDE's Developers-------------------------------------------------------

developers = raw_data.loc[raw_data.DevType != 'NA', 'IDE']
developers_df = pd.DataFrame(developers)

developers_df = developers_df.dropna()

split_IDE = pd.DataFrame(developers_df.IDE.str.split(';').tolist())
stacked_IDE=split_IDE.stack()

stacked_IDE.value_counts()[:15].plot(kind='barh', figsize=(9,6),
                         title="Developers")

#---2.Data Scientists----------------------------------------------------------

#---2.1 Data Scientists Residency----------------------------------------------

d_scientists = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','Country']
d_scientists_df = pd.DataFrame(d_scientists)

d_scientists_df = d_scientists_df.dropna()

split_Country = pd.DataFrame(d_scientists_df.Country.str.split(';').tolist())
stacked_Country=split_Country.stack()

stacked_Country.value_counts()[:15].plot(kind='barh', figsize=(9,6),
                             title="Top 15 Country of Residence")

#---2.2 Subjects in which Data Scientists took Majors--------------------------

major = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','UndergradMajor']
major_df = pd.DataFrame(major)
major_df = major_df.dropna()

major_df['UndergradMajor'].value_counts()[:15].plot(kind='barh', figsize=(9,6),
     title="Undergraduate Majors")

#---2.3 Formal Education of Data Scientists------------------------------------

form_edu = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','FormalEducation']
form_edu_df = pd.DataFrame(form_edu)
form_edu_df = form_edu_df.dropna()

form_edu_df['FormalEducation'].value_counts()[:15].plot(kind='barh',
            figsize=(9,6), title="Formal Education")


#---3. Job Satisfaction and Future Expectations--------------------------------

#---3.1 Employment Status - Data Science---------------------------------------

employment = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','Employment']
employment_df = pd.DataFrame(employment)
employment_df = employment_df.dropna()

employment_df['Employment'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0.1, 0, 0, 0, 0, 0), shadow=True)

#---3.2 Employment Status - Developers---------------------------------------

raw_data['Employment'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize':20}, title = 'Developers',
        autopct='%1.0f%%', shadow=True, explode=(0.1, 0, 0, 0, 0, 0))

#---3.3 Job Satisfaction - Data Science----------------------------------------

job_sat = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','JobSatisfaction']
job_sat_df = pd.DataFrame(job_sat)
job_sat_df = job_sat_df.dropna()

job_sat_df['JobSatisfaction'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0, 0.1, 0, 0, 0, 0, 0), shadow=True)

#---3.4 Job Satisfaction - Developers------------------------------------------

raw_data['JobSatisfaction'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Developers',
        autopct='%1.0f%%', explode=(0, 0.1, 0, 0, 0, 0, 0), shadow=True)

#---3.5 Job Search Status - Data Science---------------------------------------

job_search = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','JobSearchStatus']
job_search_df = pd.DataFrame(job_search)
job_search_df = job_search_df.dropna()

job_search_df['JobSearchStatus'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0.1, 0, 0), shadow=True)

#---3.6 Job Search Status - Developers-----------------------------------------

raw_data['JobSearchStatus'].value_counts()[:20].plot(kind='pie', figsize=(9,9),
    title="Developers",autopct='%1.0f%%',explode=(0.1, 0, 0))

#---3.7 Expectation in the upcoming years - Data Science-----------------------

hope = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','HopeFiveYears']
hope_df = pd.DataFrame(hope)
hope_df = hope_df.dropna()

hope_df['HopeFiveYears'].value_counts()[:15].plot(kind='barh',
            figsize=(9,6), title="Data Science")

#---3.8 Expectation in the upcoming years - Developers-------------------------

raw_data['HopeFiveYears'].value_counts()[:15].plot(kind='barh',
            figsize=(9,6), title="Developers")


#---4. Artificial Intelligence-------------------------------------------------

#---4.1 Data Scientists View on the Future of AI------------------------------------

AI = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','AIFuture']
AI_df = pd.DataFrame(AI)
AI_df = AI_df.dropna()

AI_df['AIFuture'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0.1, 0, 0), shadow=True)

#---4.2 Developers View on the Future of AI------------------------------------

raw_data['AIFuture'].value_counts().plot(kind='pie', figsize=(9,9),
        title="Developers", autopct='%1.0f%%',
        textprops={'fontsize':20},explode=(0.1, 0, 0), shadow=True)

#---4.3 Who Should Be Responsible for AI - Data Science------------------------

AI_resp = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','AIResponsible']
AI_resp_df = pd.DataFrame(AI_resp)
AI_resp_df = AI_resp_df.dropna()

AI_resp_df['AIResponsible'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0.1, 0, 0, 0), shadow=True)
 
#---4.4 Who Should Be Responsible for AI - Developers--------------------------

raw_data['AIResponsible'].value_counts().plot(kind='pie', figsize=(9,9),
        title="Developers", autopct='%1.0f%%',
        textprops={'fontsize':20},explode=(0.1, 0, 0, 0), shadow=True)

#---4.5 Aspects of AI Which Scares Data Scientists-----------------------------

AI_danger = raw_data.loc[raw_data.DevType == 'Data scientist or machine learning specialist','AIDangerous']
AI_danger_df = pd.DataFrame(AI_danger)
AI_danger_df = AI_danger_df.dropna()

AI_danger_df['AIDangerous'].value_counts().plot(kind='pie', figsize=(9,9),
        textprops={'fontsize': 20}, title = 'Data Science',
        autopct='%1.0f%%', explode=(0.1, 0, 0, 0), shadow=True)

#---4.6 Aspects of AI Which Scares Developers----------------------------------

raw_data['AIDangerous'].value_counts().plot(kind='pie', figsize=(9,9),
        title="Developers", autopct='%1.0f%%',
        textprops={'fontsize':20},explode=(0.1, 0, 0, 0), shadow=True)

#------------------------------------------------------------------------------