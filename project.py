# ------ Importing Packages -------
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns

# ------ Configuring Main Page -------

st.set_page_config(page_title= 'Average Time Spent By A User On Social Media',
                   page_icon= ':bar_chart:',
                   layout = 'centered')

df = pd.read_csv('dummy_data.csv')

print(df.head(5))

st.title('Data Project 1:')
st.header('Average Time Spent By A User On Social Media')
st.write('by: Lexin Deang')
st.caption('Kaggle Dataset Link : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')

# Replace 'Lifestlye' with Lifestyle due to misspelling
df.replace({'Lifestlye':'Lifestyle'}, inplace = True)


tab1, tab2 = st.tabs(['EDA', 'Visualization'])

# -------- Exploratory Data Analysis --------
with tab1:
    st.header('Exploratory Data Analysis')
    
    # ------ Sidebar Creation -------

    profession = st.sidebar.multiselect(
        'Select the profession:',
        options = df['profession'].unique(),
        default = df['profession'].unique()
    )

    location = st.sidebar.multiselect(
        'Select the location:',
        options = df['location'].unique(),
        default = df['location'].unique()
    )

    gender = st.sidebar.multiselect(
        'Select the gender:',
        options = df['gender'].unique(),
        default = df['gender'].unique()
    )

    interests = st.sidebar.multiselect(
        'Select the interests:',
        options = df['interests'].unique(),
        default = df['interests'].unique()
    )

    demographics = st.sidebar.multiselect(
        'Select the demographics:',
        options = df['demographics'].unique(),
        default = df['demographics'].unique()
    )
    # *** Selection ***
    query_multiline = '''
        profession == @profession &
        location == @location &
        gender == @gender &
        interests == @interests &
        demographics == @demographics
    '''

    query_multiline = query_multiline.replace('\n', '')

    # Customized Dataframe Based on selections
    df_selection = df.query(query_multiline)

    st.dataframe(df_selection)

# -------- Visualization --------
with tab2: 

    # ------ Main Page -------
    st.title(':bar_chart: Time Spent Correlations')
    st.markdown('###')
    
    profession_str = ', '.join(profession)
    location_str = ', '.join(location)
    gender_str = ', '.join(gender)
    interests_str = ', '.join(interests)
    demographics_str = ', '.join(demographics)
    
    st.markdown(f"""
                 The data refers to the professions of `{profession_str}`\
                     at `{location_str}` who are `{gender_str}`,\
                         who have interests in `{interests_str}`, \
                             under the demographics of\
                                 `{demographics_str}`. """)
            
    average_income = round(df_selection['income'].mean(),1)
    average_time_spent = round(df_selection['time_spent'].mean(), 1)
    total_home_owners = len(df[df['isHomeOwner'] == False])


    left_col, middle_col, right_col = st.columns(3)
    with left_col: 
        st.subheader(':dollar: Income Average:')
        st.subheader(f'$ {average_income}')
    with middle_col: 
        st.subheader(':clock2: Average Time')
        st.subheader(f'{average_time_spent} hours')
    with right_col: 
        st.subheader(':house: Homeowners')
        st.subheader(total_home_owners)